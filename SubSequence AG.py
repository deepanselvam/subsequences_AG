def subsequence(str):
    result = 0
    a_count = 0
    for i in range(len(str)):
        if str[i] == 'A':
            a_count += 1
        elif str[i] == 'G':
            result += a_count
    return result

str = input()
value = subsequence(str)
print(value)
