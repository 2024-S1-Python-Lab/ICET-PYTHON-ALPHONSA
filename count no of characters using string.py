def countchar(inputstring):
    count = {}
    for char in inputstring:
        if char in count:
             count[char] += 1
        else:
            count[char] = 1

    return count
str2  = input("enrt a string: ")
result = countchar(str2)
print(result)
            
