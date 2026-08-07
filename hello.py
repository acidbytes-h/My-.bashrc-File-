import string
import time
import math

def rainbow_text(plain_text):
    """Applies a smooth lolcat-style gradient to text using ANSI colors."""
    colored_text = ""
    # Lower frequency makes the color transitions smoother
    frequency = 0.25 
    
    for index, char in enumerate(plain_text):
        # Generate Red, Green, and Blue values using sine waves
        r = int(math.sin(frequency * index + 0) * 127 + 128)
        g = int(math.sin(frequency * index + 2) * 127 + 128)
        b = int(math.sin(frequency * index + 4) * 127 + 128)
        
        # Wrap the character in a truecolor terminal escape code
        colored_text += f"\033[38;2;{r};{g};{b}m{char}"
        
    # Reset color back to default at the end of the string
    colored_text += "\033[0m"
    return colored_text

text = 'Hello Earth!'
temp = ''

for ch in text:
    if ch == ' ':
        temp += ' '
        continue
        
    for i in string.printable:
        # Wrap the current guess in the rainbow function
        current_guess = temp + i
        print(rainbow_text(current_guess), end='\r', flush=True)
        time.sleep(0.01)
        
        if i == ch:
            temp += ch
            break

# Print the final completed phrase in full color on a new line
print(rainbow_text(text), end='\n', flush=True)
