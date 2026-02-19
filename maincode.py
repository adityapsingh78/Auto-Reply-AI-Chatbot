import pyautogui
import pyperclip
import time
import os
from openai import OpenAI

# API key from environment variable (SAFE for GitHub)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SENDER_NAME = "Friend"   # change to the other person's name


def is_last_message_from_sender(chat_log, sender_name):
    lines = chat_log.strip().split('\n')
    if not lines:
        return False
    last_line = lines[-1].lower()
    return sender_name.lower() in last_line


# Click chat icon once
pyautogui.click(1209, 1049)
time.sleep(1)


while True:

    # Select chat area
    pyautogui.moveTo(516, 201)
    pyautogui.dragTo(1859, 941, duration=1.5, button='left')
    time.sleep(0.5)

    # Copy text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    copied_text = pyperclip.paste()
    print("Copied Text:")
    print(copied_text)

    if is_last_message_from_sender(copied_text, SENDER_NAME):

        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {
                    "role": "system",
                    "content": "You are Aditya from India. You speak natural Hinglish and reply like a friendly coder."
                },
                {
                    "role": "user",
                    "content": copied_text
                }
            ]
        )

        response_text = response.choices[0].message.content

        pyperclip.copy(response_text)
        time.sleep(0.5)

        pyautogui.click(649, 990)
        time.sleep(0.3)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)

        pyautogui.press('enter')

    time.sleep(3)   # prevents CPU overload
