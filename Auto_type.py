import time
import pyautogui

def autotype():
    text_to_type = "Hello, World!"
    delay_time = 0.1
    pyautogui.click(x=100, y=100)
    for char in text_to_type:
        pyautogui.typewrite(char)
        time.sleep(delay_time)

if __name__ == "__main__":
    time.sleep(5) # Wait 5 seconds before running
    pyautogui.PAUSE = 0.5 # Pause for 0.5 seconds between actions
    autotype()