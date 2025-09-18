num = float(input("Give me a number: "))
int_num = int(num)

if int_num == 0 and num == 0:   
    print(int_num)
elif num == int_num:            
    print("This number is an integer")
else:
    print("This number is a decimal.")
