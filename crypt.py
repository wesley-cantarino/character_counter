#crypt
def isWorld (read):
    for i in range(65, 91):  # maiusculo
        if read == chr(i):
            return True
    for i in range(97, 123):  # maiusculo
        if read == chr(i):
            return True

    return False

def descText(k):
    for read in text:  # var read varre text
        if isWorld(read) == False:
            print(read, end='')
        else:
            for i in range(97, 123):  #Capital letter
                if read == chr(i):
                    if (i - k >= 97):
                        print(chr(i - k), end='')
                    else:
                        print(chr(i - k + 26), end='')

            for i in range(65, 91):  #Small letter
                if read == chr(i):
                    if (i - k >= 65):
                        print(chr(i - k), end='')
                    else:
                        print(chr(i - k + 26), end='')


text = input("->")

k = 1
descText(k)
