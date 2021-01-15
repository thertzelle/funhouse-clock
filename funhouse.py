import board
import neopixel
pixels = neopixel.NeoPixel(board.D6, 30, brightness=0.5, auto_write=False)

pixels.fill((255, 0, 0))
pixels.show()
