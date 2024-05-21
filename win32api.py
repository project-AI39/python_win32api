import ctypes
import time

# 仮想キーコード
keycodes = {
    "a": {"scan_code": 0x1E, "vk_code": 0x41},
    "b": {"scan_code": 0x30, "vk_code": 0x42},
    "c": {"scan_code": 0x2E, "vk_code": 0x43},
    "d": {"scan_code": 0x20, "vk_code": 0x44},
    "e": {"scan_code": 0x12, "vk_code": 0x45},
    "f": {"scan_code": 0x21, "vk_code": 0x46},
    "g": {"scan_code": 0x22, "vk_code": 0x47},
    "h": {"scan_code": 0x23, "vk_code": 0x48},
    "i": {"scan_code": 0x17, "vk_code": 0x49},
    "j": {"scan_code": 0x24, "vk_code": 0x4A},
    "k": {"scan_code": 0x25, "vk_code": 0x4B},
    "l": {"scan_code": 0x26, "vk_code": 0x4C},
    "m": {"scan_code": 0x32, "vk_code": 0x4D},
    "n": {"scan_code": 0x31, "vk_code": 0x4E},
    "o": {"scan_code": 0x18, "vk_code": 0x4F},
    "p": {"scan_code": 0x19, "vk_code": 0x50},
    "q": {"scan_code": 0x10, "vk_code": 0x51},
    "r": {"scan_code": 0x13, "vk_code": 0x52},
    "s": {"scan_code": 0x1F, "vk_code": 0x53},
    "t": {"scan_code": 0x14, "vk_code": 0x54},
    "u": {"scan_code": 0x16, "vk_code": 0x55},
    "v": {"scan_code": 0x2F, "vk_code": 0x56},
    "w": {"scan_code": 0x11, "vk_code": 0x57},
    "x": {"scan_code": 0x2D, "vk_code": 0x58},
    "y": {"scan_code": 0x15, "vk_code": 0x59},
    "z": {"scan_code": 0x2C, "vk_code": 0x5A},
    "1": {"scan_code": 0x02, "vk_code": 0x31},
    "2": {"scan_code": 0x03, "vk_code": 0x32},
    "3": {"scan_code": 0x04, "vk_code": 0x33},
    "4": {"scan_code": 0x05, "vk_code": 0x34},
    "5": {"scan_code": 0x06, "vk_code": 0x35},
    "6": {"scan_code": 0x07, "vk_code": 0x36},
    "7": {"scan_code": 0x08, "vk_code": 0x37},
    "8": {"scan_code": 0x09, "vk_code": 0x38},
    "9": {"scan_code": 0x0A, "vk_code": 0x39},
    "0": {"scan_code": 0x0B, "vk_code": 0x30},
    "enter": {"scan_code": 0x1C, "vk_code": 0x0D},
    "esc": {"scan_code": 0x01, "vk_code": 0x1B},
    "space": {"scan_code": 0x39, "vk_code": 0x20},
    "backspace": {"scan_code": 0x0E, "vk_code": 0x08},
    "tab": {"scan_code": 0x0F, "vk_code": 0x09},
    "ctrl": {"scan_code": 0x1D, "vk_code": 0x11},
    "alt": {"scan_code": 0x38, "vk_code": 0x12},
    "shift": {"scan_code": 0x2A, "vk_code": 0x10},
    "capslock": {"scan_code": 0x3A, "vk_code": 0x14},
    "f1": {"scan_code": 0x3B, "vk_code": 0x70},
    "f2": {"scan_code": 0x3C, "vk_code": 0x71},
    "f3": {"scan_code": 0x3D, "vk_code": 0x72},
    "f4": {"scan_code": 0x3E, "vk_code": 0x73},
    "f5": {"scan_code": 0x3F, "vk_code": 0x74},
    "f6": {"scan_code": 0x40, "vk_code": 0x75},
    "f7": {"scan_code": 0x41, "vk_code": 0x76},
    "f8": {"scan_code": 0x42, "vk_code": 0x77},
    "f9": {"scan_code": 0x43, "vk_code": 0x78},
    "f10": {"scan_code": 0x44, "vk_code": 0x79},
    "f11": {"scan_code": 0x57, "vk_code": 0x7A},
    "f12": {"scan_code": 0x58, "vk_code": 0x7B},
}


class KeyBdInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
    ]


class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
    ]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput), ("mi", MouseInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong), ("ii", Input_I)]


def key_down(key):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(
        keycodes[key]["vk_code"],
        keycodes[key]["scan_code"],
        0,
        0,
        ctypes.pointer(extra),
    )
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def key_up(key):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(
        keycodes[key]["vk_code"],
        keycodes[key]["scan_code"],
        0x0002,
        0,
        ctypes.pointer(extra),
    )
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def press_key(key):
    key_down(key)
    time.sleep(0.1)
    key_up(key)


def mouse_move(x, y):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def lpress():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def lrelease():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def rpress():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def rrelease():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0010, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def rclick():
    rpress()
    time.sleep(0.1)
    rrelease()


def lclick():
    lpress()
    time.sleep(0.1)
    lrelease()
