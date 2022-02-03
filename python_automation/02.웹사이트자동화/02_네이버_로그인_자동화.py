from selenium import webdriver
import time
import pyautogui
import pyperclip

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
browser = webdriver.Chrome("c:/chromedriver.exe")
browser.implicitly_wait(10) # 페이지가 로딩될때까지 최대 10초 기다려줌
browser.maximize_window() # 화면 최대화
browser.get(url) # 페이지 열기

# 아이디 입력창
id = browser.find_element_by_css_selector("#id") # 아이디 입력창을 찾고 id변수에 저장
id.click() # 아이디 입력창 클릭
# id.send_keys("kmc7582s@naver.com") #send_keys는 (" ")내용을 키보드로 입력 한다는 뜻이다.
pyperclip.copy("아이디")
pyautogui.hotkey("ctrl","v")
time.sleep(2) # 2초 정도 프로그램을 멈춤

# 비밀번호 입력창
pw = browser.find_element_by_css_selector("#pw")
pw.click()
# pw.send_keys("비밀번호")
pyperclip.copy("비밀번호")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 로그인 버튼
login_btn = browser.find_element_by_css_selector("#log\.login")
login_btn.click()