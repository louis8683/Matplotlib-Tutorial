'''
Date: 5/14/2020
Author: Louis
Name: Auto Coding

This program is for auto-typing a code in VS Code.

How to setup:
    In "settings.json" (CTRL+SHIFT+P -> Open Settings (JSON)), add:
        "editor.quickSuggestions": false,
        "editor.autoClosingBrackets": "never",
        "editor.formatOnType": false,

    In extensions, disable "Python" and reload.
    
    Install the "pyautogui", "pyperclip", "keyboard" module
        - In conda, run "conda install -c conda-forge pyautogui".
        - In conda, run "conda install -c conda-forge pyperclip".
        - In conda, run "pip install keyboard"

How to run:
    1. prepare the editor to type in
    2. run the code
    4. let the magic happen

    Notes: if you want to terminate the program, you have to do it FAST

Command Line Arguments:
    python auto_coding.py [filename]

Parameters:
- count_down_time:int
    count down time before typing starts
- word_interval:float
    time delay between each letter typed
- line_interval:float
    time delay between each line
- filename:str
    the default file to copy
- activate_key:str
    key for activating line by line auto typing
    default: 'esc'
- ignore_key:str
    key for detecting ignore key (used for writing comments)
    default: '\\'
- multiline_key:str
    key for detecting multiline blocks, blocks should be wrapped with the key
    default: '`'
'''

import time
import sys
import pyautogui
import pyperclip
import keyboard as kb 

# parameters
count_down_time = 0
word_interval = 0.05
line_interval = 0.2
filename = "./nothing.py"
activate_key = 'esc'
ignore_key = '\\'
multiline_key = '`'

def count_down(seconds):
    start_time = time.time()
    i = 0
    while True:
        if time.time() - start_time >= i + 1:
            if seconds - 1 > 0:
                print(f"\r{seconds-i}!", end='')
            i += 1
        if i == seconds+1:
            break
    print(f"\rGo!")



def auto_type(s, interval=word_interval):
    for c in s:
        pyperclip.copy(c)
        pyautogui.hotkey("ctrl","v")
        time.sleep(interval)


def multiline_with_indent(lines, last_indent=0):
    for line in lines:
        # Indention
        splits = line.split("    ")
        indent = 0
        for split in splits:
            if split == "":
                indent += 1
            if split != "":
                break
        print(indent)
        # concatenate the rest of the line
        line = ""
        print(splits)
        for s in splits[indent:]:
            line += s
        if last_indent > indent:
            for _ in range(last_indent - indent):
                pyautogui.keyDown('shift')
                pyautogui.press('tab')
                pyautogui.keyUp('shift')
        # Replace all '\n' with 'Enter'
        line = line.split('\n')[0]
        auto_type(line, interval=word_interval)
        pyautogui.press('enter')
        start_time = time.time()
        while time.time() - start_time < line_interval-word_interval:
            pass
        last_indent = indent


def run(lines):
    multiline = False
    multilines = []
    for line in lines:
        # Look for ignore key
        if line[0] == ignore_key:
            continue
        # Look for multiline
        if line[0] == '`':
            if multiline:
                multiline_with_indent(multilines)
                multilines = []
            elif not multiline:
                kb.wait(activate_key)
            multiline = not multiline
            continue
        # Line options
        if not multiline:
            # Remove all '\n'
            line = line.split('\n')[0]
            # Wait for key
            kb.wait(activate_key)
            # Write
            auto_type(line, interval=word_interval)
        elif multiline:
            multilines.append(line)


if __name__ == "__main__":
    # Look for filename
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    # Count Down
    count_down(count_down_time)
    # Read file
    with open(filename, "r", encoding='UTF-8') as f:
        lines = f.readlines()
    # Type
    run(lines)
