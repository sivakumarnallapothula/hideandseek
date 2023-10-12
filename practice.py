import pyautogui as sk
import time
time.sleep(10)
l=1
for i in range(30):
   sk.write("Hello eyes "+str(l))
   l+=1
   sk.press("Enter")
