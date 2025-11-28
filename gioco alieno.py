from pgzero.actor import Actor
from pgzero.clock import clock
from random import randint
import pgzrun
TITLE = "Colpisci l'alieno"
WIDTH = 800
HEIGHT = 600
messaggio = ""
alieno = Actor("alieno")
vite=3
punti=0
def draw():
    if vite>0:
        screen.clear()
        screen.fill(color=(0, 215, 215))
        alieno.draw()
        screen.draw.text(messaggio, center=(400, 40), fontsize=60)
        screen.draw.text(f"vite={vite}", topright=(160, 40), fontsize=60)
        screen.draw.text(f"punti={punti}", topright=(760, 40), fontsize=60)
    else:
        screen.clear()
        screen.fill(color=(100, 0, 0))
        screen.draw.text("HAI PERSO!", center=(400, 300), fontsize=60,color=(180, 0, 0))
        
def piazza_alieno():
    alieno.x = randint(90, WIDTH-90)
    alieno.y = randint(90, HEIGHT-90)
    alieno.image = "alieno"

def on_mouse_down(pos):
    global messaggio, vite, punti
    if alieno.collidepoint(pos):
        punti+=1
        messaggio = "Bel colpo!"
        alieno.image = "esplosione"
    else:
        messaggio = "Mancato..."
        vite-=1

piazza_alieno()
clock.schedule_interval(piazza_alieno, 1.0)
pgzrun.go()