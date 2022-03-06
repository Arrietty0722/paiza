import sys
import time
import threading

import pyautogui
# from paiza import main
from mod7 import main


def input_test():
    print("input_test :")
    keys = "3\n10\n4\n14"
    # keys = "10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
    keys = "10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
    print(keys)
    print("")
    print("")
    print("<< start test >>")
    # pyautogui.press(['2'])
    # pyautogui.press("enter")
    # pyautogui.press(['2', " ", "5"])
    # pyautogui.press("enter")
    # pyautogui.press(['3', " ", "4"])
    # pyautogui.press("enter")

    input_keys(keys)


def input_keys(keys):
    key_lines = keys.split("\n")
    print(f"key_lines : {key_lines}")
    for key_line in key_lines:
        string = list(key_line)
        pyautogui.press(string)
        pyautogui.press("enter")


def test():
    output_th = threading.Thread(target=main)
    input_th = threading.Thread(target=input_test)

    output_th.start()
    input_th.start()

    output_th.join()


if __name__ == "__main__":
    test()
    # input_test()
