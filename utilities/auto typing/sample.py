\ Comment uses a leading '\'
\ Line by Line, use 'esc' for next line
import pyperclip
import pyautogui
import auto_coding


` Multiline writes, comments for multiline can be written here
def auto_type(s, interval=0.1):
    for c in s:
        pyperclip.copy(c)
        pyautogui.hotkey("ctrl","v")
        auto_coding.wait(interval)
`

\ Chinese is also possible!
# 中文註解!
if __name__ == "__main__":
    s = "中文和English夾雜"
    auto_type(s)

\ TRY ME WITH A BLANK FILE!!
