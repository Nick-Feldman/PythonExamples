'''
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
'''

def compress(text):
    result = text[0]          #begin with first letter and counter for repeats
    count = 1

    for i in range(len(text) - 1):
        if text[i] == text[i+1]:  # see if next letter is the same and then iterate counter if it is
            count += 1
        else:
            if count > 1:            #if counter is more than one add it to string
                result += str(count)
            result += text[i + 1]     #add next letter
            count = 1
    if count > 1:
        result += str(count)

    return result

def decompress(text):
    result = text[0]
    count = 0

    for i in range(len(text) - 1):
        if text[i+1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:  # see if next letter is number
            count += 1  #keep track of amount of characters that are numbers
        else:
            if count > 0:
                result += text[(i - count)] * (int(text[(i+1-count):(i + 1)])-1)  #copy last actual letter by number of
            result += text[i+1]                                                   #number of repeats
            count = 0
    #if last digit was a number print number of copies below
    if count > 0:
        result += text[(len(text)-1 - count)]  * (int(text[(len(text)- count):(len(text))])-1) #find position of last
                                                #letter and then print number of repeats
    return result

test = "hello world!hello world!hello world!hello world!"

print(compress(test))
print(decompress(compress(test)))

test2 = "a23b5c2d11"

print(decompress(test2))
