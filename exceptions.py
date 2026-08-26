#Using exceptions to prevent crashes

print("Give two numbers to divide...")
print("Enter q to quit")

while True:
    first_number = input("Enter the first number: ")
    if first_number  == 'q':
        break
    second_number = input("Enter the second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can not divide by zero!")
    else:
        print(answer)