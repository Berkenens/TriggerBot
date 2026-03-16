import addy
import pymem
import keyboard
import pyautogui

pm = pymem.Pymem("cstrike_win64.exe")
client_base = pymem.process.module_from_name(
    pm.process_handle, "client.dll"
).lpBaseOfDll


#pointer
# "client.dll"+00649910 + 18 + 10 + 50

pointer_base = client_base + 0x00649910

entity_base = client_base + 0x6098C8
localplayer_base = client_base + 0x068EEC8


#loop

while True:
    try:
        lp = pm.read_ulonglong(localplayer_base)
        lt = pm.read_int(lp + 0xD8)
        addy = pm.read_ulonglong(pointer_base)
        addy = pm.read_ulonglong(addy + 0x18)
        addy = pm.read_ulonglong(addy + 0x10)
        crosshair_ID = pm.read_int(addy + 0x50)

        if crosshair_ID != 0:
            ep = pm.read_ulonglong(entity_base + (crosshair_ID-1) * 0x20)
            et = pm.read_int(ep + 0xD8)
            if keyboard.is_pressed("ALT3") and lt != et and et != 0:
             pyautogui.click()
    except Exception as e:
        print(f"Error occured {e}")

