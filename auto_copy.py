import time
import pyautogui
import clipboard
from pynput import mouse

def on_click(x, y, button, pressed):
    if not pressed:
        # 等待以确保选择完成
        time.sleep(0.1)
        # 发送 Ctrl+C 复制命令
        pyautogui.hotkey('ctrl', 'c')
        
        # 等待以确保复制完成
        time.sleep(0.1)
        
        # 获取并打印复制的内容（用于调试）
        copied_text = clipboard.paste()
        print("复制的内容:", copied_text)

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
