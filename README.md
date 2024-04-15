# Micropython Fontlib
A simple micropython library for using 1bit bitmaps as fonts, I made it for a monocrome screen (pcd8544 nokia screen)  but you should work with any monocrome screens through (framebuffer)[https://docs.micropython.org/en/latest/library/framebuf.html] 

# How to use it
add fontlib.py and a 1bit font .bmp file to your micropython device, then use the library to modify a framebuffer:
```python
import framebuf
import fontlib

screen_width = 85
screen_height = 85
spce = 1 # characters spacing
pos_x = 0 # X position on the frame buffer to print the text
pos_y = 0 # Y position on the frame buffer to print the text

five = fontlib.font("five (5,5).bmp") # Loads font to ram 

buffer = bytearray((screen_height // 8) * screen_width)
fbuf = framebuf.FrameBuffer(buffer, screen_width, screen_height, framebuf.MONO_VLSB)
fbuf.fill(0)
fontlib.prt("The Quick Gray",0,0,1,fbuf,five) # prints text using font
```
see the examples folder for a exemple on how to use it with a Nokia 5110 LCD Display

# How create new fonts
add a bitmap font, and rename it similary to the others in the Bitmaps folder then run the 'BitmapDictionaryGenerator.ipynb' python notebook

# TODO
- [x] Load fonts directly from 1bit bitmaps
- [ ] Support for portuguese special characters (ç,á,é,í,ó,ú,â,ê,ô,ã,õ)(Ç,Á,É,Í,Ó,Ú,Â,Ê,Ô,Ã,Õ).
- [ ] Support for color screens

# Available fonts:
[futuristic](https://opengameart.org/content/ascii-bitmap-font-futuristic) :\
<img src='./Photos/futuristic.png' width='300'>
<img src='./Bitmaps/futuristic.png (5,5).bmp' width='300' >\
five:\
<img src='./Photos/five.png' width='300'>
<img src='./Bitmaps/five (5,5).bmp' width='300'>\
[oldschool](https://opengameart.org/content/ascii-bitmap-font-oldschool) :\
<img src='./Photos/oldschool.png' width='300'>
<img src='./Bitmaps/oldschool (5,7).bmp' width='300'>\
[cellphone](https://opengameart.org/content/ascii-bitmap-font-cellphone) :\
<img src='./Photos/cellphone.png' width='300'>
<img src='./Bitmaps/cellphone (5,7).bmp' width='300'>\
icons:\
<img src='./Photos/icons.png' width='300'>
<img src='./Bitmaps/icons (5,7).bmp' width='300'>
