import pyautogui
import time

def move_mouse():
    while True:
        # 現在のマウス位置を取得
        x, y = pyautogui.position()
        # マウスを1ピクセル動かす（例えば右に1ピクセル）
        pyautogui.moveTo(x + 20, y)
        # 少し元に戻して1ピクセル動かすように見せる
        pyautogui.moveTo(x, y)
        # 60秒待機
        time.sleep(5)

if __name__ == "__main__":
    move_mouse()
