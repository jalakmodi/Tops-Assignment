E_Note=[]

while True:
    print("*" * 30)
    print("Welcome To E-Note Console")
    print("*" * 30)
    print("1. For Generate Note ")
    print("2. For View Note ")
    print("3. Exit")
    print("*" * 30)

    choice=int(input("Enter Your Choice Number : "))

    if choice == 1:
        new_note=input("Enter Your Note : ")
        file = open("enote.txt", "a")
        file.write(new_note)
        file.close()
        print("Note Added Successfully.")

    elif choice == 2:
        print("Below Your Added Notes ")
        file=open("enote.txt","r")
        print(file.read())
        file.close()

    elif choice == 3:
        print("Exiting E-Note Console. Goodbye!")
        break