import random
from machine import Pin, SPI
import gc9a01
import framebuf
import fontlib

spi = SPI(0, baudrate=60000000, sck=Pin(18), mosi=Pin(19))
tft = gc9a01.GC9A01(
    spi,
    dc=Pin(21, Pin.OUT),
    cs=Pin(17, Pin.OUT),
    reset=Pin(20, Pin.OUT),
    #backlight=Pin(14, Pin.OUT),
    rotation=0)

screen_width = 240
screen_height = 240
bytebuffer = bytearray(screen_width * screen_height * 2) #two bytes for each pixel
fbuf = framebuf.FrameBuffer(bytebuffer, screen_width, screen_height, framebuf.RGB565)

IBM_font = fontlib.font("IBM BIOS (8,8).bmp") # Loads font to ram 
five = fontlib.font("five (5,5).bmp")
color1 = gc9a01.color565(red=255, green=255, blue=255)
color2 = gc9a01.color565(red=139, green=0, blue=0)
color3 = gc9a01.color565(red=0, green=255, blue=0)
color4 = gc9a01.color565(red=0, green=0, blue=255)


fbuf.fill(0)
fontlib.prt("The quick",10,80,1,fbuf,IBM_font,invert = False,color=color1) # prints text using font
fontlib.prt("brown fox",10,90,1,fbuf,IBM_font,invert = False,color=color2) # prints text using font
fontlib.prt("jumps over ",10,100,1,fbuf,IBM_font,invert = False,color=color3) # prints text using font
fontlib.prt("The lazy dog ",10,110,1,fbuf,IBM_font,invert = False,color=color4) # prints text using font
tft.blit_buffer(bytebuffer,0,0,screen_width,screen_height)
