import pyautogui
import time
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

# マウスを動かすフラグ
running = True

def move_mouse():
    global running
    while running:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 20, y)
        pyautogui.moveTo(x, y)
        time.sleep(5)

def start_mouse_movement():
    global running
    if not running:
        running = True
        threading.Thread(target=move_mouse, daemon=True).start()

def stop_mouse_movement():
    global running
    running = False

def create_image():
    # シンプルなアイコンを作成
    width, height = 64, 64
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), fill="blue")
    draw.ellipse((16, 16, 48, 48), fill="white")
    return image

def quit_app(icon):
    stop_mouse_movement()
    icon.stop()

if __name__ == "__main__":
    # 初期状態でマウス移動を開始
    threading.Thread(target=move_mouse, daemon=True).start()

    # システムトレイメニューの作成
    menu = Menu(
        MenuItem("Start", start_mouse_movement),
        MenuItem("Stop", stop_mouse_movement),
        MenuItem("Quit", quit_app)
    )

    # システムトレイアイコンの設定
    icon = Icon("MouseMover", create_image(), "Mouse Mover", menu)
    icon.run()

