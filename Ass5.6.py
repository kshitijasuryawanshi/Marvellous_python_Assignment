
def ConvertToFahrenheit(Celsius):
    Fahren=(Celsius*9/5)+32
    return Fahren

def main():
    Celsius=int(input("Enter temperature in celsius:"))
    ret=ConvertToFahrenheit(Celsius)
    print("Temperature in Fahrenheit: ",ret,"oF")




if __name__=="__main__":
    main()