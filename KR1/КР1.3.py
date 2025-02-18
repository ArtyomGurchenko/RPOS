def capitalize_words(s):
    if 0 < len(s) < 1000:
        return ' '.join(word.capitalize() for word in s.split())
    else:
        return "String length must be greater than 0 and less than 1000 characters."

input_str = input()

output_str = capitalize_words(input_str)
print(output_str)

