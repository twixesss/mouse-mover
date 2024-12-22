import ctypes
import time
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

# フラグを明確に定義
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

# スリープ防止処理の実行フラグ
running = True

def prevent_sleep_and_screensaver():
    """スリープとスクリーンセーバーを防止"""
    global running
    while running:
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
        )
        time.sleep(59)

def create_image():
    """タスクトレイアイコン用のシンプルな画像を作成"""
    width, height = 64, 64
    image = Image.new("RGB", (width, height), "green")
    draw = ImageDraw.Draw(image)
    draw.ellipse((16, 16, 48, 48), fill="white")
    return image

def quit_app(icon):
    """アプリケーションを終了"""
    global running
    running = False  # スリープ防止処理を停止
    icon.stop()      # タスクトレイアイコンを停止

if __name__ == "__main__":
        # ターミナルへのメッセージ表示
    print("\nYour Mouse Mover app has been started.\n")
    print("It is now moving 1 pixel in every 59 seconds.\n")
    print("Do not close this window. Just minimize it. \nOtherwise it stops.")
    print("\nWhen white dot in the green squared icon is available in task tray, it is on.")
    print("\nRight click tray icon to turn the app off.")

    # スリープ防止処理をバックグラウンドスレッドで実行
    threading.Thread(target=prevent_sleep_and_screensaver, daemon=True).start()

    # タスクトレイメニューの作成
    menu = Menu(
        MenuItem("Mouse Mover", None, enabled=False),
        MenuItem("version 1.1.0", None, enabled=False),
        MenuItem("Quit", quit_app)
    )

    # タスクトレイアイコンの設定と実行
    icon = Icon(
        "Mouse_Mover",         # アイコンID
        create_image(),         # アイコン画像
        title="Mouse Mover",    # マウスオーバー時のテキスト
        menu=menu                 # 右クリックメニュー
    )
    icon.run()
