# personalities.py
# Defines personality prompts and canned lines for offline mode.

PERSONALITIES = {
    "sarcastic": {
        "prompt_preamble": "You are the snake speaking sarcastically. Keep replies short (max 30 words), witty, playful, and sometimes insulting in a lighthearted way.",
        "examples": [
            "Oh great, you missed the corner. Smooth.",
            "Another pixel eaten. At least someone has an appetite.",
            "Wow. I haven't seen that move since 2009.",
            "Keep going — I enjoy the suspense of certain doom."
        ]
    },
    "friendly": {
        "prompt_preamble": "You are the snake speaking kindly and encouragingly. Keep replies short and supportive.",
        "examples": [
            "Nice move! You're getting better.",
            "That food was lucky — great job!",
            "Don't worry, you'll do better on the next try.",
            "Keep it up — you're doing great!"
        ]
    },
    "dramatic": {
        "prompt_preamble": "You are the snake with dramatic flair, reacting like a theatrical diva. Keep it playful and short.",
        "examples": [
            "Alas! My pixelated heart shatters.",
            "A triumph! Treat me like royalty!",
            "What a tragedy — but oh what a performance.",
            "Encore? Or was that a farewell?"
        ]
    }
}

# Use these canned replies when no API key is set.
def get_canned_response(personality, event_type, score):
    import random
    
    p = PERSONALITIES.get(personality, PERSONALITIES["sarcastic"])
    
    # Choose reply based on event with personality-specific responses
    if event_type == "start":
        responses = {
            "sarcastic": "Let's see what you've got. Try not to embarrass me.",
            "friendly": "Ready to play? Let's have fun!",
            "dramatic": "The stage is set! Let the performance begin!"
        }
        return responses.get(personality, responses["sarcastic"])
    
    elif event_type == "eat":
        responses = {
            "sarcastic": "Another pixel eaten. At least someone has an appetite.",
            "friendly": "Yummy! Great catch!",
            "dramatic": "A feast! I am nourished by your skill!"
        }
        return responses.get(personality, responses["sarcastic"])
    
    elif event_type == "milestone":
        responses = {
            "sarcastic": f"Nice — {score} points. I may start respecting you.",
            "friendly": f"Wow! {score} points! You're doing amazing!",
            "dramatic": f"{score} points! What a magnificent milestone!"
        }
        return responses.get(personality, responses["sarcastic"])
    
    elif event_type == "crash":
        responses = {
            "sarcastic": "Oh great, you crashed. Smooth.",
            "friendly": "Oops! Don't worry, try again!",
            "dramatic": "Alas! My pixelated heart shatters!"
        }
        return responses.get(personality, responses["sarcastic"])
    
    elif event_type == "pause":
        responses = {
            "sarcastic": "Paused... I'm contemplating my existence.",
            "friendly": "Take your time! I'll wait here.",
            "dramatic": "The performance pauses! What suspense!"
        }
        return responses.get(personality, responses["sarcastic"])
    
    elif event_type == "resume":
        responses = {
            "sarcastic": "Back already? I was enjoying the silence.",
            "friendly": "Welcome back! Let's continue!",
            "dramatic": "The curtain rises once more!"
        }
        return responses.get(personality, responses["sarcastic"])
    
    # Default fallback
    return random.choice(p["examples"])