def count_characters(S):
    char_count= {}
    for char in S:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char] = 1
    return char_count

input_str= input("Enter a string :")
print(count_characters(input_str))