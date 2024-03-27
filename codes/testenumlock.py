from win32api import GetKeyState
from win32con import VK_CAPITAL
from win32con import VK_NUMLOCK


# if GetKeyState(VK_CAPITAL) == 1:
#     print ("CAPS Lock is on.")
# elif GetKeyState(VK_CAPITAL) == 0:
#     print ("CAPS Lock is off.")

if GetKeyState(VK_NUMLOCK) == 1:
    print ("NUM LOCK is on.")
elif GetKeyState(VK_NUMLOCK) == 0:
    print ("NUM LOCK is off.")