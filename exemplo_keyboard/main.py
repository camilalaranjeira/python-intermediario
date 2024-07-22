from pynput.keyboard import  Listener
from rich.console import Console
from playsound import playsound

# Inicializa o console e as dimensões do terminal
console = Console()
width, height = console.size

# Posição inicial do robôzinho
player_x, player_y = width // 2, height // 2
emoji = "🤖"

# Desenha o robôzinho de acordo com as variáveis globais
def draw_player(key):
    console.clear()
    for y in range(height):
        if y == player_y:
            line = " " * player_x + emoji 
        else:
            line = ""
        console.print(line)

# altera as variáveis globais de posição do robôzinho
def move_player(key):
    global player_x, player_y

    try:
        if key.char == 'w' and player_y > 0:
            player_y -= 1
        elif key.char == 's' and player_y < height - 1:
            player_y += 1
        elif key.char == 'a' and player_x > 0:
            player_x -= 2
        elif key.char == 'd' and player_x < width - 2:
            player_x += 2
    except AttributeError: pass

playsound('music.wav', False)
print('Pressione qualquer tecla para começar!')
with Listener(on_press=move_player, on_release=draw_player) as listener:
    listener.join()
