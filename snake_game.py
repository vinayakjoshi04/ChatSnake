import pygame
import random
from utils import draw_text, render_wrapped_text

CELL = 20  # pixel size of one grid cell

class Game:
    def __init__(self, game_rect, chat_rect, personality="sarcastic", sfx=None):
        """
        game_rect: (x, y, width, height) for game area
        chat_rect: (x, y, width, height) for chat panel
        sfx: dict with 'eat' and 'crash' pygame Sound objects (optional)
        """
        self.game_rect = pygame.Rect(*game_rect)
        self.chat_rect = pygame.Rect(*chat_rect)
        self.cols = self.game_rect.width // CELL
        self.rows = self.game_rect.height // CELL
        self.reset()
        self.font = pygame.font.SysFont("consolas", 18)
        self.huge_font = pygame.font.SysFont("consolas", 28, bold=True)
        self.chat_lines = []
        self.personality = personality
        self.sfx = sfx or {}
    
    def reset(self):
        self.snake = [(5,5), (4,5), (3,5)]
        self.direction = (1, 0)  # moving right
        self.spawn_food()
        self.score = 0
        self.game_over = False
        self.paused = False
        self.last_milestone = 0  # Track last milestone
    
    def spawn_food(self):
        while True:
            x = random.randint(0, self.cols-1)
            y = random.randint(0, self.rows-1)
            if (x,y) not in self.snake:
                self.food = (x,y)
                break
    
    def set_direction(self, dx, dy):
        # Prevent reversing:
        if (dx, dy) == (-self.direction[0], -self.direction[1]):
            return
        self.direction = (dx, dy)
    
    def update(self):
        if self.paused or self.game_over:
            return None
        
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        # collisions with walls
        if not (0 <= new_head[0] < self.cols and 0 <= new_head[1] < self.rows):
            self.game_over = True
            return "crash"
        
        # self collision
        if new_head in self.snake:
            self.game_over = True
            return "crash"
        
        # move
        self.snake.insert(0, new_head)
        
        if new_head == self.food:
            self.score += 1
            self.spawn_food()
            
            # Check for milestone (every 5 points)
            if self.score > 0 and self.score % 5 == 0 and self.score != self.last_milestone:
                self.last_milestone = self.score
                return "milestone"
            
            return "eat"
        else:
            self.snake.pop()
        
        return None
    
    def toggle_pause(self):
        self.paused = not self.paused
        return "pause" if self.paused else "resume"
    
    def add_chat_line(self, text):
        # keep a short history
        self.chat_lines.append(text)
        if len(self.chat_lines) > 12:
            self.chat_lines.pop(0)
    
    def draw(self, surface):
        # draw background for game
        pygame.draw.rect(surface, (20, 20, 20), self.game_rect)
        
        # draw grid (optional)
        for x in range(self.cols):
            for y in range(self.rows):
                px = self.game_rect.x + x * CELL
                py = self.game_rect.y + y * CELL
                rect = pygame.Rect(px, py, CELL, CELL)
                # cell background subtle
                pygame.draw.rect(surface, (30,30,30), rect)
        
        # draw food
        fx = self.game_rect.x + self.food[0] * CELL
        fy = self.game_rect.y + self.food[1] * CELL
        food_rect = pygame.Rect(fx+2, fy+2, CELL-4, CELL-4)
        pygame.draw.rect(surface, (200, 60, 60), food_rect)
        
        # draw snake
        for i, (sx, sy) in enumerate(self.snake):
            px = self.game_rect.x + sx * CELL
            py = self.game_rect.y + sy * CELL
            rect = pygame.Rect(px+1, py+1, CELL-2, CELL-2)
            if i == 0:
                pygame.draw.rect(surface, (50,200,50), rect)  # head
            else:
                pygame.draw.rect(surface, (40,160,40), rect)
        
        # score
        draw_text(surface, f"Score: {self.score}", (self.game_rect.x+6, self.game_rect.y+6), self.huge_font, (255,255,255))
        
        # chat panel
        pygame.draw.rect(surface, (15,15,40), self.chat_rect)
        
        # render chat history
        render_wrapped_text(surface, "\n".join(self.chat_lines[-10:]) or "Snake: ...", (self.chat_rect.x+8, self.chat_rect.y+8, self.chat_rect.width-16, self.chat_rect.height-16), self.font, (220,220,220))
        
        # if game over
        if self.game_over:
            midx = self.game_rect.x + self.game_rect.width//2
            midy = self.game_rect.y + self.game_rect.height//2
            go_surf = self.huge_font.render("GAME OVER", True, (200,80,80))
            surface.blit(go_surf, (midx - go_surf.get_width()//2, midy - 10))
            sub = self.font.render("Press R to restart", True, (220,220,220))
            surface.blit(sub, (midx - sub.get_width()//2, midy + 30))