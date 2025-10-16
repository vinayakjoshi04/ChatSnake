import pygame
import sys
import os
import pyttsx3
import threading
from snake_game import Game
from ai_chat import AIChat

# Constants - INCREASED SIZE
WIDTH = 1200
HEIGHT = 800
FPS = 10

def load_sounds():
    """Load eating and crash sounds, fallback to wav if mp3 fails."""
    sfx = {}
    base = os.path.join(os.path.dirname(__file__), "assets")
    eat_path = os.path.join(base, "eating.mp3")
    crash_path = os.path.join(base, "break.mp3")
    eat_fallback = os.path.join(base, "eating.wav")
    crash_fallback = os.path.join(base, "break.wav")
    
    try:
        if os.path.exists(eat_path):
            sfx['eat'] = pygame.mixer.Sound(eat_path)
        elif os.path.exists(eat_fallback):
            sfx['eat'] = pygame.mixer.Sound(eat_fallback)
        
        if os.path.exists(crash_path):
            sfx['crash'] = pygame.mixer.Sound(crash_path)
        elif os.path.exists(crash_fallback):
            sfx['crash'] = pygame.mixer.Sound(crash_fallback)
    except Exception as e:
        print("Couldn't load sounds:", e)
    
    return sfx

def get_ai_response_async(ai, event_type, score, game):
    """Get AI response in background thread to avoid blocking game"""
    def fetch():
        try:
            line = ai.get_response(event_type, score)
            game.add_chat_line("Snake: " + line)
        except Exception as e:
            print(f"AI response error: {e}")
    
    # Start thread for AI response (TTS will happen inside ai.get_response)
    thread = threading.Thread(target=fetch, daemon=True)
    thread.start()

def main():
    # Initialize pygame and mixer
    pygame.init()
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
    
    # Larger screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ChatSnake")
    clock = pygame.time.Clock()
    
    # Game and chat rectangles - INCREASED SIZE
    game_rect = (0, 0, 900, 800)
    chat_rect = (900, 0, 300, 800)
    
    # Initialize TTS engine with faster speech
    try:
        tts_engine = pyttsx3.init()
        # Faster TTS settings for smooth gameplay
        tts_engine.setProperty('rate', 180)  # Speed up speech
        tts_engine.setProperty('volume', 0.9)  # Slightly lower volume
    except:
        tts_engine = None
        print("TTS not available, continuing without audio")
    
    ai = AIChat(personality="sarcastic", use_tts=True, tts_engine=tts_engine)  # TTS ENABLED
    
    # Load sounds
    sfx = load_sounds()
    game = Game(game_rect, chat_rect, personality="sarcastic", sfx=sfx)
    
    # Start AI greeting (async to not block)
    get_ai_response_async(ai, "start", game.score, game)
    
    running = True
    speed = FPS
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    game.set_direction(0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    game.set_direction(0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    game.set_direction(-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    game.set_direction(1, 0)
                elif event.key == pygame.K_p:
                    res = game.toggle_pause()
                    get_ai_response_async(ai, "pause" if res=="pause" else "resume", game.score, game)
                elif event.key == pygame.K_r:
                    if game.game_over:
                        game.reset()
                        get_ai_response_async(ai, "start", game.score, game)
        
        # Update game
        event_type = game.update()
        if event_type:
            # Get AI response asynchronously (non-blocking)
            get_ai_response_async(ai, event_type, game.score, game)
            
            # Play sounds immediately
            if event_type == "eat" and 'eat' in sfx:
                try: 
                    sfx['eat'].play()
                except: 
                    pass
            if event_type == "crash" and 'crash' in sfx:
                try: 
                    sfx['crash'].play()
                except: 
                    pass
        
        # Draw everything
        screen.fill((10,10,10))
        game.draw(screen)
        pygame.display.flip()
        clock.tick(speed)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()