'''
Programmer: Kaeden Lee
Date: 10.15.19
Program: Double For Loop

This program will nest a For Loop inside of another
For Loop
'''

for i in range(3):
    print("Outer For Loop: " + str(i))
    for l in range(2):
        print("     Inner For Loop: " + str(l))

print("\n***************\n")


'''
Programmer: Kaeden Lee
Date: 10.23.19
Program: For Loop + While Loop

This program will create a For Loop with a While Loop embedded into it
'''

for i in range(4):
    print("Outer For Loop: " + str(i))
    x = 6
    while x >= 0:
        print("    While Loop: " + str(x))
        x = x - 1
