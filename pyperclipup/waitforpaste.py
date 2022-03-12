# Pyperclip에는 pyperclip.waitForPaste()비어 있지 않은 텍스트 문자열이 클립보드에 있을 때까지 차단하고 
# 반환하지 않는 기능도 있습니다. 그런 다음 이 문자열을 반환합니다.
# 클립보드 의 pyperclip.waitForNewPaste()텍스트가 변경될 때까지 차단됩니다.
import pyperclip
pyperclip.waitForPaste()  


pyperclip.copy('original text')
pyperclip.waitForNewPaste()  
