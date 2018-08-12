#character_counter
def tellText():
    for read in text:
        for i in range(97, 123): #Capital letter
            if read == chr(i):
                dice[i - 97] += 1
        for i in range(65, 91): #Small letter
            if read == chr(i):
                dice[i - 65] += 1

dice = [0] * 26

text = input("write some text\n>")
tellText()

for i in range(26):
    print(chr(i + 97), dice[i])



'''#ASCII code
for i in range(97, 123):
    print("'%s' -> ASCII %d" %(chr(i), i))

print("------------------------------")

for i in range(65, 91):
    print("'%s' -> ASCII %d" %(chr(i), i))
'''
