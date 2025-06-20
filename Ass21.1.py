import psutil


def main():
    print("Automation Script for Display Process name and PID and username:")

    Procname="Ass21.1.py"

    for proc in psutil.process_iter(['pid','name','username','cmdline']):
        try:
            cmdline=proc.info['cmdline']
            if cmdline and any(Procname in arg for arg in cmdline):
                print(f"PID:{proc.info['pid']},Name:{proc.info['name']},user:{proc.info['username']}")
        except(psutil.NoSuchProcess,psutil.AccessDenied):
                pass
    

if __name__=="__main__":
    main()