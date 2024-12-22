
import ctypes
import time

def prevent_sleep_and_screensaver():
    # フラグを明確に定義
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002
    
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )
    print("スリープとスクリーンセーバーを防止しています...")

if __name__ == "__main__":
    while True:
        prevent_sleep_and_screensaver()
        time.sleep(60)
