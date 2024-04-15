import fonts_dictionary
import math

def reverse_Bits(n, no_of_bits):
    result = 0
    for i in range(no_of_bits):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

def getbitmap(path):
    file = open(path, "rb")
    filebytes = bytearray(file.read())
    file.close()
    imagesize = (int.from_bytes(filebytes[18:22],"little"),int.from_bytes(filebytes[22:26],"little"))
    filezise =  int.from_bytes(filebytes[2:6],"little")
    dataOffset = int.from_bytes(filebytes[10:14],"little")
    format = int.from_bytes(filebytes[28:30],"little")
    pallet = [0,1][b'\x00\x00\x00\xff\xff\xff\xff\xff' == filebytes[54:62]]
    imagedata = bytearray(reversed(filebytes[dataOffset:]))
    bytesperrow = math.ceil(imagesize[0]/8)
    rowPadding = ((4-(bytesperrow%4))%4)
    rowsize = bytesperrow +rowPadding
    if pallet:
        for i,byte_ in enumerate(imagedata):
            imagedata[i] = byte_^ 0xff
    imagerows = []
    for i,byte_ in enumerate(imagedata):
        imagedata[i] = reverse_Bits(byte_,8)
    for i in range(imagesize[1]):
        imagerows.append(bytearray(reversed(imagedata[i*rowsize:(i+1)*rowsize])))
    imagerows = tuple(imagerows)
    return (imagerows,imagesize,filezise,dataOffset,format)

def getCutTile(imagerows,tilepos,chopsize,imagesize,paddingsize = 1):
    bytesperrow = math.ceil(imagesize[0]/8)
    rowPadding = ((4-(bytesperrow%4))%4)
    rowsize = bytesperrow +rowPadding
    bitsperrow = bytesperrow*8
    bitpadding = bitsperrow-imagesize[0]
    newchopsize = (chopsize[0]+paddingsize*2,chopsize[1]+paddingsize*2)

    left = tilepos[0] * newchopsize[0]
    upper = tilepos[1] * newchopsize[1]
    cutdata = bytearray()
    k = 0
    b = 0x00
    for j in range(paddingsize,newchopsize[1]-paddingsize,1):
        for i in range(paddingsize,newchopsize[0]-paddingsize,1):
            bitindex = left+i
            currentbyte = imagerows[j+upper][bitindex//8]
            bitpos =  bitindex%8
    
            if ((currentbyte >> bitpos) & 1):
                b |= ((1 << k))
            else:
                b &= ((1 << k) ^ 0xFF)
            k +=1
            if k > 7 or ((j == newchopsize[1]-paddingsize-1) and (i == newchopsize[0]-paddingsize-1)):
                cutdata.append(b)
                b = 0x00
                k = 0
    return cutdata

def chop_image(imagepath, chopsize,paddingsize = 1):
    #like dicing an onion
    bmptup = getbitmap(imagepath)
    width,height = bmptup[1]
    num_rows = height // (chopsize[1]+paddingsize*2)
    num_cols = width // (chopsize[0]+paddingsize*2)

    cut_images = []
    for y in range(num_rows):
        for x in range(num_cols):
            cutdata = getCutTile(bmptup[0],(x,y),chopsize,bmptup[1],paddingsize = paddingsize)
            cut_images.append(cutdata)
    
    return cut_images

class font():
    def __init__(self,bmp_path):
        try:
            bmpname = bmp_path.split("/")[-1]
            szstrlist = bmpname.split(" (")[1].split(").")[0].split(",")
        except:
            raise Exception("invalid fontpath, check if file exist and fontname includes fontsize")

        self.size = (int(szstrlist[0]),int(szstrlist[1]))
        self.CharList = chop_image(bmp_path, self.size,paddingsize = 1)
    
    def getchar(self,N):
        return self.CharList[N]
    
def DrawPixels(xpos,ypos,charbytes,charsize,fbuf,invert=False):
    orig_y = ypos
    orig_x = xpos
    for byt in charbytes:
        for i in range(8):
            if ypos<charsize[1]+orig_y:
                fbuf.pixel(xpos,ypos,(invert,not invert)[((byt >> i) & 1)])
            xpos+= 1
            if xpos >= charsize[0]+orig_x:
                xpos = orig_x
                ypos += 1
            
def printchar(letter,xpos,ypos,fbuf,font,invert = False,charwidth=None):
    if charwidth == None:
        charwidth = font.size[0]
    origin = xpos
    
    charval = ord(letter)
    if charval > 127: #Todo support for portuguese special characters
        charval = 0x3f
    index = charval-32 #start code, 32 or space
    character = font.getchar(index)

    DrawPixels(xpos,ypos,character,font.size,fbuf,invert=invert)

def prt(string,xpos,ypos,spce,fbuf,font,invert=False):
    char_size = font.size
    if invert:
        string_width = (char_size[0]+spce)*(len(string)-1)+char_size[0]+1
        string_height = char_size[1]
        fbuf.rect(xpos-1, ypos-1, string_width+1, string_height+2, 1)
    for i,c in enumerate(string):
        printchar(c,xpos,ypos,fbuf,font = font,invert=invert,charwidth=char_size[0])
        xpos+=(spce+char_size[0])
        if (invert and i < len(string)-1):
            fbuf.rect(xpos-spce, ypos, spce, string_height, 1,1)