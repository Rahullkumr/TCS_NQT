# 14) Leap Year or not
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('LEAP YEAR')
        else:
            print('not LY')
    else:
        print("LEAP YEAR")
else:
    print('not LY')
