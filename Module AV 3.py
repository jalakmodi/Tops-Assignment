def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 == 0:
                raise ValueError("Even number entered. Please enter an odd number.")
            else:
                print("You entered an odd number.")
                break
        except ValueError as e:
            print(e)

# Call the function to get an odd number from the user
get_odd_number()