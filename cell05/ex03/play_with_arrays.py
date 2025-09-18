Original = [2, 8, 9, 48, 8, 22, -12, 2]
New = set()
for i in range(len(Original)):
    if(Original[i] > 5) :
        num = Original[i] + 2
        New.add(num)

print(f"Original array: {Original}")
print(f"New array: {New}")