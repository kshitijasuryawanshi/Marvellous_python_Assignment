import schedule
import time
import datetime

def Display():
    print("Namaskar! : ")

def main():
    print("Inside automation script")
    print("Current time is : ", datetime.datetime.now())

    schedule.every().day.at("09:00").do(Display) 

    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()