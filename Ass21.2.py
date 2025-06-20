import psutil
import sys

def ProcessInfo(pname):
    for proc in psutil.process_iter(['name']):
         if proc.info['name'] == pname:
            print(proc)


def main():
    ProcessInfo(sys.argv[1])

if __name__=="__main__":
    main()