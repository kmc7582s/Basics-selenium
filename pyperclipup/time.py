# timeout확인할 시간(초)을 지정하는 인수도 있습니다. 
# 반환하지 않고 시간 초과가 경과하면 함수에서 PyperclipTimeoutException예외가 발생합니다.
import pyperclip
pyperclip.waitForNewPaste(5)
