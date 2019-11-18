if __name__ == '__main__':
        print("This program will convert Meters to inches")
        meter = input('Enter meters: ')
        metervalue = float(meter)
        inch = 39.37 * metervalue
        inchvalue = format(inch, '.1f')
        print(meter, "meters equals", inchvalue, "inches")
