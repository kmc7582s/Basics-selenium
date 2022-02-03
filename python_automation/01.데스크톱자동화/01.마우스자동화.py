from http.client import PROXY_AUTHENTICATION_REQUIRED
import pyautogui
import time

# # 1. 화면 크기 출력
# print(pyautogui.size())

# 2. 마우스 위치 출력
#time.slepp(2)
# print(pyautogui.position())

# # 3. 마우스 이동
# pyautogui.moveTo(19, 300, 2)

# # 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3 ,interval=1) #3번 클릭하는데 1초 마다 한다.

# 5. 마우스 드래그
# 595,58
# 638,53
pyautogui.moveTo(595,58, 2)
pyautogui.drag(638,53, 2)

