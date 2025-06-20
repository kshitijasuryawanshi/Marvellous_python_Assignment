import schedule
import time
import datetime

def Display():
    fobj=open("Marvellous.txt","w")
    currentdate= datetime.datetime.now()
    fobj.write(str(currentdate))

def main():
    print("Inside automation script")
    
    schedule.every(1).minutes.do(Display) 
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()