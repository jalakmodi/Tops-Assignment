def read_first_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return ''.join(lines[:n])
    except FileNotFoundError:
        print("File not found.")
        return None

file_name = input("Enter the name of the file to read: ")
n = int(input("Enter the number of lines to read: "))

file_contents = read_first_n_lines(file_name, n)

if file_contents:
    print(f"First {n} lines of the file:")
    print(file_contents)
