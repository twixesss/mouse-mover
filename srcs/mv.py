import pyautogui
import time
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

pyautogui.FAILSAFE = False

# マウスを動かすフラグ
running = True
icon = None

def move_mouse():
    global running, icon
    while running:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 40, y)
        pyautogui.moveTo(x, y)
        time.sleep(3)

def start_mouse_movement(icon):
    global running
    if not running:
        running = True
        update_icon(icon, "Running")
        threading.Thread(target=move_mouse, daemon=True).start()

def stop_mouse_movement(icon):
    global running
    running = False
    update_icon(icon, "Stopped")

def create_image(color):
    # シンプルなアイコンを作成
    width, height = 64, 64
    image = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(image)
    draw.ellipse((16, 16, 48, 48), fill="white")
    return image

def update_icon(icon, status):
    """アイコンを現在の状態に応じて更新"""
    color = "green" if status == "Running" else "red"
    icon.icon = create_image(color)
    icon.title = f"Mouse Mover - {status}"

def quit_app(icon):
    stop_mouse_movement(icon)
    icon.stop()

if __name__ == "__main__":
    # ターミナルへのメッセージ表示
    print("\nYour Mouse Mover app has been started.\n")
    print("It is now moving 1 pixel in every 59 seconds.\n")
    print("Do not close this window. Just minimize it. \nOtherwise it stops.")
    print("\nYou can see the status on your tasktray. \nRed means stopped, green means running.")

    # システムトレイメニューの作成
    menu = Menu(
        MenuItem("Start", lambda: start_mouse_movement(icon)),
        MenuItem("Stop", lambda: stop_mouse_movement(icon)),
        MenuItem("Quit", lambda: quit_app(icon))
    )

    # 初期状態でマウス移動を開始
    threading.Thread(target=move_mouse, daemon=True).start()

    # 初期状態のシステムトレイアイコンの設定
    icon = Icon("MouseMover", create_image("green"), "Mouse Mover - Running", menu)
    icon.run()
