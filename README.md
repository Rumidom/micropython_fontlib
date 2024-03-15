# Micropython Fontlib
A simple micropython library that adds 4 different fonts to it, I made it for a monocrome screen (pcd8544 nokia screen)  but you should be able to modify it for color screens 

# How to use
add fontlib.py and fonts_dictionary.py to your micropython device, then use the library to modify a framebuffer:
```python
import framebuf
import fontlib

screen_width = 85
screen_height = 85
spce = 1 # characters spacing
pos_x = 0 # X position on the frame buffer to print the text
pos_y = 0 # Y position on the frame buffer to print the text

buffer = bytearray((screen_height // 8) * screen_width)
fbuf = framebuf.FrameBuffer(buffer, screen_width, screen_height, framebuf.MONO_VLSB)
fbuf.fill(0)
fontlib.printstring("The Quick Gray",pos_x,pos_y,spce,fbuf,font_name = "futuristic")
```
see the examples folder for a exemple on how to use it with a Nokia 5110 LCD Display

# How create new fonts
add a bitmap font to the Bitmaps folder and run the 'BitmapDictionaryGenerator.ipynb' python notebook

# Available fonts:
futuristic:

