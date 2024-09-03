import pyautogui
import time
 
def keep_alive(interval=10, movement=100):
    try:
        while True:
            current_x, current_y = pyautogui.position()
            pyautogui.moveRel(movement, movement, duration=0.5)
            pyautogui.moveRel(-movement, -movement, duration=0.5)
            pyautogui.moveTo(current_x, current_y, duration=0.5)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Script terminated by user")

if __name__ == "__main__":
    keep_alive()