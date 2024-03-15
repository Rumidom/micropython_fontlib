import fonts_dictionary

def printchar(letter,xpos,ypos,spce,fbuf,font_name = "five"):
    origin = xpos
    charval = ord(letter)
    index = charval-32 #start code, 32 or space
    character = fonts_dictionary.fontdict[font_name][index]
    rows = [character[i:i+5] for i in range(0,len(character),5)]
    for row in rows:
        for bit in row:
            if bit == '1':
                fbuf.pixel(xpos,ypos,1)
            xpos+=1
        xpos=origin
        ypos+=1

def printstring(string,xpos,ypos,spce,fbuf,font_name = "five"):
    for i in string:
        printchar(i,xpos,ypos,spce,fbuf,font_name = font_name)
        xpos+=(spce+5)

