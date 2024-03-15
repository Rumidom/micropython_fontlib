# micropython Fontlib
A simple micropython library that adds 4 different fonts to it, I made it for a monocrome screen (pcd8544 nokia screen)  but you should be able to modify it for color screens 

# How to use
add fontlib.py and fonts_dictionary.py to your micropython device, then use the library to modify a framebuffer:
```python
import framebuf
import fontlib

screen_width = 85
screen_height = 85
buffer = bytearray((screen_height // 8) * screen_width)
fbuf = framebuf.FrameBuffer(buffer, screen_width, screen_height, framebuf.MONO_VLSB)
fbuf.fill(0)
fontlib.printstring("The Quick Gray",0,0,1,fbuf,font_name = "futuristic")
```
see the examples folder for a exemple on how to use it with a Nokia 5110 LCD Display

# How Create new Fonts
add a bitmap font to the Bitmaps folder and run the 'BitmapDictionaryGenerator.ipynb' python notebook

# Available fonts:

