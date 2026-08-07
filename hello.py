import string
import time
import math

def rainbow_text(plain_text):
    """Applies a smooth lolcat-style gradient to text using ANSI colors."""
    colored_text = ""
    frequency = 0.25 
    
    for index, char in enumerate(plain_text):
        r = int(math.sin(frequency * index + 0) * 127 + 128)
        g = int(math.sin(frequency * index + 2) * 127 + 128)
        b = int(math.sin(frequency * index + 4) * 127 + 128)
        
        colored_text += f"\033[38;2;{r};{g};{b}m{char}"
        
    colored_text += "\033[0m"
    return colored_text

text = 'Hello Earth!'
temp = ''

for ch in text:
    if ch == ' ':
        temp += ' '
        continue
        
    for i in string.printable:
        current_guess = temp + i
        print(rainbow_text(current_guess), end='\r', flush=True)
        time.sleep(0.01)
        
        if i == ch:
            temp += ch
            break

print(rainbow_text(text), end='\n', flush=True)
