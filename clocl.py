import time
import os
import shutil
from datetime import datetime


DIGITS = {
    '0': [" ██ ", "█  █", "█  █", "█  █", " ██ "],
    '1': ["  █ ", " ██ ", "  █ ", "  █ ", " ███"],
    '2': [" ██ ", "█  █", "  █ ", " █  ", "████"],
    '3': ["███ ", "   █", " ██ ", "   █", "███ "],
    '4': ["█  █", "█  █", "████", "   █", "   █"],
    '5': ["████", "█   ", "███ ", "   █", "███ "],
    '6': [" ██ ", "█   ", "███ ", "█  █", " ██ "],
    '7': ["████", "   █", "  █ ", " █  ", " █  "],
    '8': [" ██ ", "█  █", " ██ ", "█  █", " ██ "],
    '9': [" ██ ", "█  █", " ███", "   █", " ██ "],
    ':': ["    ", " ██ ", "    ", " ██ ", "    "],
    ' ': ["    ", "    ", "    ", "    ", "    "],
    'A': [" ██ ", "█  █", "████", "█  █", "█  █"],
    'P': ["███ ", "█  █", "███ ", "█   ", "█   "],
    'R': ["███ ", "█  █", "███ ", "█ █ ", "█  █"],
    'V': ["█  █", "█  █", "█  █", "█  █", " ██ "],
    'E': ["████", "█   ", "███ ", "█   ", "████"],
    'D': ["███ ", "█  █", "█  █", "█  █", "███ "],
    'O': [" ██ ", "█  █", "█  █", "█  █", " ██ "],
    'B': ["███ ", "█  █", "███ ", "█  █", "███ "],
    'C': [" ██ ", "█  █", "█   ", "█  █", " ██ "],
    'L': ["█   ", "█   ", "█   ", "█   ", "████"],
    'T': ["████", " ██ ", " ██ ", " ██ ", " ██ "],
    'U': ["█  █", "█  █", "█  █", "█  █", " ██ "],
    'S': [" ███", "█   ", " ██ ", "   █", "███ "],
    'N': ["█  █", "██ █", "█ ██", "█  █", "█  █"],
    'M': ["█   █", "██ ██", "█ █ █", "█   █", "█   █"],
    'Y': ["█   █", " █ █ ", "  █  ", "  █  ", "  █  "],
    'W': ["█   █", "█   █", "█ █ █", "██ ██", "█   █"],
    'H': ["█  █", "█  █", "████", "█  █", "█  █"],
    'K': ["█  █", "█ █ ", "██  ", "█ █ ", "█  █"],
    'F': ["████", "█   ", "███ ", "█   ", "█   "],
    'G': [" ██ ", "█   ", "█ ██", "█  █", " ██ "],
    'Z': ["████", "   █", " ██ ", "█   ", "████"],
    'J': ["  ██", "   █", "   █", "█  █", " ██ "],
    'X': ["█   █", " █ █ ", "  █  ", " █ █ ", "█   █"]
    }

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def render_ascii_text(text, font):
    lines = [""] * 5
    for char in text:
        char = char.upper()
        if char in font:
            for i in range(5):
                lines[i] += font[char][i] + "  "
        else:
            for i in range(5):
                lines[i] += "     "
    return lines

def center_lines(lines):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    return [' ' * ((width - len(line)) // 2) + line for line in lines]

def draw_ascii_clock():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%a %d %b %Y")

    time_lines = render_ascii_text(time_str, DIGITS)
    date_lines = render_ascii_text(date_str, DIGITS)

    all_lines = center_lines(time_lines + [""] + date_lines)

    clear()

    top_margin = 10
    print("\n" * top_margin)

    for line in all_lines:
        print(line)

def main():
    next_tick = time.time()
    while True:
        draw_ascii_clock()

        next_tick += 1
        sleep_time = next_tick - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            next_tick = time.time()


if __name__ == "__main__":
      main()