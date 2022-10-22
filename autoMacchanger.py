import time
import os

macchange = "sudo macchanger -r eth0 "

os.system(macchange)

if __name__ == "__main__":
    print(__name__)

timeout_set = bool(input("Enter your timeout : "))

while True:
    os.system(macchange)
    time.sleep(timeout_set)
