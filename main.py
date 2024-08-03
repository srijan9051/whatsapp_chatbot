import webbrowser
import time
import pyautogui as pg
import pyperclip
import chatbot


name = input("Enter the name with whom you want to chat: ")
webbrowser.open("https://web.whatsapp.com/")
time.sleep(25)
print("Process started...")
pg.click(183, 284)  
time.sleep(1)
pg.write(name)
time.sleep(1)
pg.press('enter')
time.sleep(5)

while True:
    # Drag to select messages
    start_x, start_y = 662, 292  # Starting point of the drag (top-left of chat messages)
    end_x, end_y = 662, 1000  # Ending point of the drag (bottom-right, drag to this point)

    pg.moveTo(start_x, start_y)
    pg.mouseDown()
    pg.moveTo(end_x, end_y, duration=1.0)
    pg.mouseUp()

    time.sleep(1)
    pg.hotkey('ctrl', 'c')

    time.sleep(1)
    text = pyperclip.paste()
    response=chatbot.answer_anything(text)
    pg.click(773, 962)
    time.sleep(1)
    pg.write(response)
    pg.press('enter')
    time.sleep(60)
