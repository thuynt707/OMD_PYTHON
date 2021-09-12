def count_char_type1(sentence):
    upper = 0
    lower = 0
    digit = 0
    letter = 0
    for i in sentence:
        if i >= 'A' and i <= 'Z':
            upper += 1
        elif i >= 'a' and i <= 'z':
            lower += 1
        elif i >= '0' and i <= '9':
            digit += 1
        letter = upper + lower
    print("Letter: " + str(letter))
    print("Upper case: " + str(upper))
    print("Lower case: " + str(lower))
    print("Digit: " + str(digit))
    char_dict = {"LETTERS": letter, "CASE": {"UPPERCASE": upper, "LOWER": lower}, "DIGIT": digit}
    return char_dict


def count_char_type2(sentence):
    upper = 0
    lower = 0
    digit = 0
    letter = 0
    for i in sentence:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
        letter = upper + lower
    print("Letter: " + str(letter))
    print("Upper case: " + str(upper))
    print("Lower case: " + str(lower))
    print("Digit: " + str(digit))
    char_dict = {"LETTERS": letter, "CASE": {"UPPERCASE": upper, "LOWER": lower}, "DIGIT": digit}
    return char_dict
