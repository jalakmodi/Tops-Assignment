def count_strings_with_same_first_and_last(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

# Example usage:
string_list = ["level", "python", "radar", "hello", "noon", "deed"]
result = count_strings_with_same_first_and_last(string_list)

print(f"Number of strings with the same first and last character: {result}")
