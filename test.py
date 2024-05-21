import win32api
import time


def main():

    win32api.key_down("w")
    time.sleep(1)
    win32api.key_up("w")

    win32api.press_key("w")

    win32api.mouse_move(100, 0)
    win32api.mouse_move(0, 100)
    win32api.mouse_move(100, 100)

    win32api.lpress()
    time.sleep(1)
    win32api.lrelease()

    win32api.rpress()
    time.sleep(1)
    win32api.rrelease()

    win32api.rclick()

    win32api.lclick()


if __name__ == "__main__":
    main()
