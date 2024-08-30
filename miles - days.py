input1 = int(input('The number of miles your car can drive in a day:'))
input2 = int(input('Total number of miles to get to your destination:'))
string1 = "The total number of days you will need to drive there is {}"
total = float(input2/input1)
print(string1.format(total))