import schedule
import time
import datetime

def Task1():
    print("Lunch Time!:")

def Task2():
    print("Wrap up work!:")

def main():
    print("Inside automation script")
    print("Current time is : ", datetime.datetime.now())

    schedule.every().day.at("13:00").do(Task1) 
    schedule.every().day.at("18:00").do(Task2) 
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()