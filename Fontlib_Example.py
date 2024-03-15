from machine import Pin,SPI
import pcd8544_fb
import framebuf
import fontlib

spi  = SPI(2, sck=Pin(13), mosi=Pin(11), miso=Pin(12))
cs = Pin(1, Pin.OUT)
dc = Pin(2, Pin.OUT)
rst = Pin(3, Pin.OUT)
lcd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)
buffer = bytearray((pcd8544_fb.HEIGHT // 8) * pcd8544_fb.WIDTH)
fbuf = framebuf.FrameBuffer(buffer, pcd8544_fb.WIDTH, pcd8544_fb.HEIGHT, framebuf.MONO_VLSB)

fbuf.fill(0)
font.printstring("The Quick Gray",0,0,1,fbuf,font_name = "cellphone")
font.printstring("Fox Jumps Over",0,8,1,fbuf,font_name = "cellphone")
font.printstring("The Lazy Dog",0,16,1,fbuf,font_name = "cellphone")
  
lcd.data(buffer)