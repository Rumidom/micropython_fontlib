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

backlight = Pin(48, Pin.OUT)
backlight.off()

five = fontlib.font("fonts/five (5,5).bmp")
futuristic = fontlib.font("fonts/futuristic (5,7).bmp")
cellphone = fontlib.font("fonts/cellphone (5,7).bmp")
oldschool = fontlib.font("fonts/oldschool (5,7).bmp")
icons = fontlib.font("fonts/icons (5,7).bmp")

fbuf.fill(0)
fontlib.prt("ç,á,é,í,ó,ú",0,4,1,fbuf,five)
fontlib.prt("â,ê,ô,ã,õ",0,16,1,fbuf,five)
fontlib.prt("Ç,Á,É,Í,Ó,Ú",0,28,1,fbuf,five)
fontlib.prt("Â,Ê,Ô,Ã,Õ",0,40,1,fbuf,five)
lcd.data(buffer)