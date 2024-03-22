import fonts_dictionary

def printchar(letter,xpos,ypos,fbuf,font = "five",invert = False,charwidth = 5):
    origin = xpos
    charval = ord(letter)
    index = charval-32 #start code, 32 or space
    try:
        character = fonts_dictionary.fontdict[font][index]
    except Exception as e:
        print("Character N:",charval)
        print(e)
        
    rows = [character[i:i+charwidth] for i in range(0,len(character),charwidth)]
    rowslen = len(rows)
    orig_y = ypos
    orig_x = xpos
    for row in rows:
        for bit in row:
            if ((bit == '1') and (invert == False)):
                fbuf.pixel(xpos,ypos,1)
            if (invert == True): # inverts and adds padding
                if (bit == '0'):
                    fbuf.pixel(xpos,ypos,1)
            xpos+=1
        xpos=origin
        ypos+=1

def printstring(string,xpos,ypos,spce,fbuf,font = "five",invert=False,charwidth=5):
    character = fonts_dictionary.fontdict[font][0]
    if invert:
        string_width = (charwidth+spce)*(len(string)-1)+charwidth+1
        string_height = len(character)//charwidth
        fbuf.rect(xpos-1, ypos-1, string_width+1, string_height+2, 1)
    for i,c in enumerate(string):
        printchar(c,xpos,ypos,fbuf,font = font,invert=invert,charwidth=charwidth)
        xpos+=(spce+charwidth)
        if (invert and i < len(string)-1):
            fbuf.rect(xpos-spce, ypos, spce, string_height, 1,1)
    

