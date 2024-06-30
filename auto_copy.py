import time
from pynput import mouse, keyboard
import pyperclip

last_copied_text = ""
last_copy_time = 0
ctrl_a_pressed = False

def on_click(x, y, button, pressed):
    global last_copied_text, last_copy_time

    current_time = time.time()

    # 仅在鼠标左键释放时执行复制操作
    if button == mouse.Button.left and not pressed:
        # 发送 Ctrl+C 复制命令
        keyboard.Controller().press(keyboard.Key.ctrl)
        keyboard.Controller().press('c')
        keyboard.Controller().release('c')
        keyboard.Controller().release(keyboard.Key.ctrl)
        
        # 等待剪贴板稳定
        time.sleep(0.1)
        
        # 获取当前剪贴板内容
        current_copied_text = pyperclip.paste()
        
        # 仅在新复制的内容与上次不同的时候更新
        if current_copied_text != last_copied_text:
            last_copied_text = current_copied_text
            print("复制的内容:", current_copied_text)
        
        # 更新上次复制时间
        last_copy_time = current_time

    # 右键单击时，复制剪贴板内容并粘贴到光标位置
    elif button == mouse.Button.right and not pressed:
        # 控制右键复制操作的频率，至少间隔0.5秒
        if current_time - last_copy_time < 0.5:
            return

        # 获取当前剪贴板内容
        current_copied_text = pyperclip.paste()
        
        # 打印当前剪贴板内容（用于调试）
        print("右键复制的内容:", current_copied_text)

        # 发送 Ctrl+V 粘贴命令
        keyboard.Controller().press(keyboard.Key.ctrl)
        keyboard.Controller().press('v')
        keyboard.Controller().release('v')
        keyboard.Controller().release(keyboard.Key.ctrl)
        
        # 更新上次复制时间
        last_copy_time = current_time

def on_press(key):
    global ctrl_a_pressed
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_a_pressed = True
    except AttributeError:
        pass

def on_release(key):
    global ctrl_a_pressed, last_copied_text, last_copy_time
    if ctrl_a_pressed and key == keyboard.KeyCode.from_char('a'):
        # 发送 Ctrl+C 复制命令
        keyboard.Controller().press(keyboard.Key.ctrl)
        keyboard.Controller().press('c')
        keyboard.Controller().release('c')
        keyboard.Controller().release(keyboard.Key.ctrl)
        
        # 等待剪贴板稳定
        time.sleep(0.1)
        
        # 获取当前剪贴板内容
        current_copied_text = pyperclip.paste()
        
        # 仅在新复制的内容与上次不同的时候更新
        if current_copied_text != last_copied_text:
            last_copied_text = current_copied_text
            print("Ctrl+A 复制的内容:", current_copied_text)
        
        # 更新上次复制时间
        last_copy_time = time.time()

    # 重置 ctrl_a_pressed
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_a_pressed = False

# 启动鼠标监听器
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 启动键盘监听器
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

# 保持脚本运行
mouse_listener.join()
keyboard_listener.join()
