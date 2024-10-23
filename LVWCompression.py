

def makeDict():

    print("In makeDict")

    char = 'a'

    dic = []

    for i in range(0, 25):

        dic.append(char)

        char = chr(ord(char) + 1)

    dic.append(' ')
    dic.append('\n')

    return dic


f = open("test.txt", "r")

st = f.read()

f.close()

dic = makeDict()

word = ''

f2 = open("compTest.txt", "w")

for ch in st:

    if ch == ' ' or ch == '\n':

        for i in range(len(dic)-1, -1, -1):
            if dic[i] == ch:
                print("IN IF")

                if ch == ' ' or ch == '\n':

                    f2.write(f"{ch}~")

                    if word:

                        dic.append(word)

                        word = ''
    else:

        word += ch

f2.close()

