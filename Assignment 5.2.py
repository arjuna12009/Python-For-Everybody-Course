largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fval = float(num)
    except:
        print("Invalid input")
        continue
    if fval > largest:
        largest = int(fval)

    if smallest is None:
        smallest = int(fval)
    elif fval < smallest:
        smallest = int(fval)

print("Maximum is", largest)
print("minimum is", smallest)