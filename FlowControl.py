# age = int(input("How old are you? "))

# if (age >= 16) and (age <= 65):
#     print("Have a good day at work")
#
# if(age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# IF/ELSE CHALLENGE
# name = input("What is your name? ")
# age = int(input("How old are you? "))
#
# if age and name:
#     if 17 < age < 31:
#         print("Welcome to the holiday {}".format(name))
#     else:
#         print("Sorry, this holiday is for 18-30 year old people")

# FOR LOOPS
# number = "9,223,972,456,765"
# cleanedNumber = ''

# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {} ".format(newNumber))
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber += char
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

# CONTINUE, BREAK, ELSE
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         continue
#     print("Buy " + item)

# CHALLENGE - Take in IP address, count number of segments and length of each segment
ipAddress = input("What is your IP address? ")
segments = 1
segmentLength = ''
tracker = 0

for i in range(0, len(ipAddress)):
    if ipAddress[i] != '.':
        tracker += 1
    if ipAddress[i] == '.':
        segments += 1
        segmentLength += str(tracker) + ', '
        tracker = 0

segmentLength += str(tracker)

print("There are {} segments".format(segments))
print("The segments lengths are {}".format(segmentLength))