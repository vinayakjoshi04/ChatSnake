import os
import requests
import threading
import queue
from dotenv import load_dotenv
from personalities import PERSONALITIES, get_canned_response

# Load GEMINI API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not set. Using canned responses.")

class AIChat:
    def __init__(self, personality="sarcastic", use_tts=False, tts_engine=None):
        self.personality = personality if personality in PERSONALITIES else "sarcastic"
        self.use_tts = use_tts
        self.tts_engine = tts_engine
        self.tts_queue = queue.Queue()
        
        # Start TTS worker thread
        if self.use_tts and self.tts_engine:
            self.tts_worker_thread = threading.Thread(target=self._tts_worker, daemon=True)
            self.tts_worker_thread.start()

    def _tts_worker(self):
        """Worker thread that processes TTS queue"""
        while True:
            try:
                text = self.tts_queue.get(timeout=1)
                if text and self.tts_engine:
                    try:
                        self.tts_engine.say(text)
                        self.tts_engine.runAndWait()
                    except Exception as e:
                        print(f"TTS error: {e}")
                self.tts_queue.task_done()
            except queue.Empty:
                continue

    def _speak_text(self, text):
        """Add text to TTS queue"""
        if self.use_tts and self.tts_engine:
            self.tts_queue.put(text)

    def _build_prompt(self, event_type, score):
        preamble = PERSONALITIES[self.personality]["prompt_preamble"]
        return f"{preamble}\nEvent: {event_type}\nScore: {score}\nRespond in 1 short witty sentence (max 15 words)."

    def get_response(self, event_type, score):
        """
        Get AI response for given event type.
        Uses Gemini 2.0 Flash API if key present, else returns canned response.
        """
        # Fallback to canned response (instant)
        if not GEMINI_API_KEY:
            text = get_canned_response(self.personality, event_type, score)
            self._speak_text(text)
            return text

        prompt = self._build_prompt(event_type, score)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.8,
                "maxOutputTokens": 40,
                "topP": 0.95,
                "topK": 40
            }
        }

        try:
            response = requests.post(url, json=data, headers=headers, timeout=3)
            response.raise_for_status()
            result = response.json()
            text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
            
            if len(text) > 100:
                text = text[:97] + "..."
                
        except Exception as e:
            print(f"Gemini API error (using fallback): {e}")
            text = get_canned_response(self.personality, event_type, score)

        # Speak the text (queued)
        self._speak_text(text)

        return text