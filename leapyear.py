#this is my first program

#January.27.2018

integer = int(raw_input("Please enter an integer that represents a year: "));

if integer % 4 == 0:
    print ("This is a leap year")
elif integer % 4==0 and integer % 100==0:
        print ("This is a leap year")
elif integer % 4 != 0:
    print ("This is not a leap year")
else:
    print ("This is not a valid input")
