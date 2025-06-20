import schedule
import time
import datetime

def MySchedule():
    print("Inside MySchecule function at : ",datetime.datetime.now())

def main():
    print("Inside automation script")
    print("Current time is : ", datetime.datetime.now())

    schedule.every(1).minute.do(MySchedule)

    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()