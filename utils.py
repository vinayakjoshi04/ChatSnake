# utils.py
import pygame
import textwrap

def draw_text(surface, text, pos, font, color=(255,255,255)):
    """Simple wrapper to blit text."""
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

def render_wrapped_text(surface, text, rect, font, color=(255,255,255), line_spacing=4):
    """
    Draw wrapped text inside rect (x, y, w, h).
    """
    x, y, w, h = rect
    lines = []
    wrapper = textwrap.TextWrapper(width=30)
    for paragraph in text.split("\n"):
        lines.extend(wrapper.wrap(paragraph))
        lines.append("")
    cy = y
    for line in lines:
        if cy + font.get_height() > y + h:
            break
        if line.strip() == "":
            cy += font.get_height() // 2
            continue
        surf = font.render(line, True, color)
        surface.blit(surf, (x, cy))
        cy += font.get_height() + line_spacing
