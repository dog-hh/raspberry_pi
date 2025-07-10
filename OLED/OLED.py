# the book don't have a flie about oled_font , so if you see something like that:
# 00\x00\x00\x00\x00\x00\x00,it means the font
from machine import Pin, I2C
import ssd1306
#import framebuf   这个库我还不会用
from font8x8 import font8x8   # 与文件 font8x8.py 同目录

# 初始化 I2C 和 OLED
i2c = I2C(0, scl=Pin(1), sda=Pin(0))      # 根据你接线调整引脚
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def draw_char(oled, x, y, ch):
    """
    在 (x,y) 位置画一个 8×8 字符 ch
    """
    data = font8x8.get(ch)
    if not data:
        return
    for row in range(8):
        byte = data[row]
        for col in range(8):
            if byte & (1 << (7 - col)):
                oled.pixel(x + col, y + row, 1)

def draw_text(oled, x, y, text):
    """
    在 (x,y) 显示一行文本，字符间隔水平 8 像素
    """
    for i, ch in enumerate(text):
        draw_char(oled, x + i * 8, y, ch)

# ---- 主程序 ----
oled.fill(0)
draw_text(oled, 0, 0, "HELLO")
draw_text(oled, 0, 10, "PICO 123")
draw_text(oled, 0, 20, "ABCXYZ7890")
oled.show()