
reader = open("input", "r")
writer = open("output", "w")

garbage = reader.readline()
textlist = reader.readlines()
text = ""
for i in range(0, len(textlist)):
    text = text + textlist[i].strip()

sp = [0] * len(text)
count = 0

for i in range (1, len(text)):
    for j in range (i, len(text)):
        if (text[i:j + 1] == text[0:j - i + 1]):
            if ((i + count) >= len(text)):
                break
            if (sp[i + count] == 0):
                sp[i + count] = count + 1
            count = count + 1
        else:
            count = 0
            break

msg = ""

for i in range(0, len(sp)):
    msg = msg + str(sp[i]) + " "

msg = msg[:-1]
writer.write(msg)

reader.close()
writer.close()
