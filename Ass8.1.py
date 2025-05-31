import threading


def Even():
    for i in range(1,21):
        if(i%2==0):
            print(i,end=" ")
    

def Odd():
    for i in range(0,20):
        if(i%2!=0):
            print(i,end=" ")

def main():
    T1=threading.Thread(target=Even)
    T2=threading.Thread(target=Odd)
    T1.start()
    print(end="\n")
    T2.start()


if __name__=="__main__":
    main()
        