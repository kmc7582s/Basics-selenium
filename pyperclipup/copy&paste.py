# 텍스트를 클립보드에 복사하려면 문자열을 pyperclip.copy(). 클립보드에서 
# 텍스트를 붙여넣으려면 호출 pyperclip.paste()하면 텍스트가 문자열 값으로 반환됩니다.
import pyperclip
pyperclip.copy('Hello, world!')
pyperclip.paste()
