def read_file(file_name):
    try:
        with open(file_name, 'r+') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
           print("File not found.")
           return None

file_name = input("Enter the name of the file to read: ")
file_contents = read_file(file_name)

if file_contents:
    print("Contents of the file:")
    print(file_contents)
