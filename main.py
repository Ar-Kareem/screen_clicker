import time
import json
from pathlib import Path

import pyautogui

version = '1.0.0'

def get_files_in_folder(folder):
    flds = Path(folder)
    return [f for f in flds.iterdir() if f.is_file()]

def locate_on_screen(imgs, confidence=0.9):
    for img in imgs:
        res = pyautogui.locateCenterOnScreen(str(img), confidence=confidence)
        if res is not None:
            print(f'Found: file:"{img.stem}" location:{res}')
            return res
    print('Nothing found...')
    return None

def print_start():
    start_str = f"""\n     <<< Starting script v{version} >>>\n"""
    print(start_str)

def load_settings():
    return json.load(open("settings.json"))

def get_image_prog(img_fldr, sleep_time=1, confidence=0.9):
    print("<<< main image loop started >>>")
    imgs = get_files_in_folder(img_fldr)
    assert len(imgs) > 0, "No images found in folder"
    def _single_loop():
        time.sleep(sleep_time)
        res = locate_on_screen(imgs, confidence)
        if res is None:
            return
        x, y = res
        # pyautogui.moveTo(x, y, duration=1)
        pyautogui.click(x, y)
    return _single_loop

def get_kbm_prog(commands, sleep_time):
    valid_functions = {
        "press": pyautogui.press,
        "hotkey": pyautogui.hotkey,
        "keyDown": pyautogui.keyDown,
        "keyUp": pyautogui.keyUp,
        "moveTo": pyautogui.moveTo,
        "click": pyautogui.click,
        "sleep": time.sleep,
    }
    def _single_loop():
        time.sleep(sleep_time)
        for cmd in commands:
            cmd_type, cmd_args, cmd_kwargs = cmd.get('type'), cmd.get('args', []), cmd.get('kwargs', {})
            if cmd_type in valid_functions:
                valid_functions[cmd_type](*cmd_args, **cmd_kwargs)
            else:
                print(f"Invalid command type: {cmd_type}")
    return _single_loop

def main():
    try:
        print_start()
        settings = load_settings()
        progs = []
        for user_prog_name, user_prog_args in settings['programs'].items():
            if user_prog_args['type'] == 'image_clicker':
                res = get_image_prog(
                    img_fldr=user_prog_args["img_fldr"],
                    sleep_time=user_prog_args["sleep_time"],
                    confidence=user_prog_args["confidence"],
                )
                progs.append(res)
            elif user_prog_args['type'] == 'keyboard_mouse_manager':
                res = get_kbm_prog(
                    commands=user_prog_args['commands'],
                    sleep_time=user_prog_args["sleep_time"],
                )
                progs.append(res)
            else:
                print(f"Invalid program type: {user_prog_args['type']}")
        while True:
            for prog in progs:
                prog()
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
