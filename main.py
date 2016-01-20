from FibClock import *
import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 5       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


if __name__ == "__main__":
    print "werk ik wel?"
    fade = 10
    test = klok(fade, 30)
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(test.timeRGB[i][0], test.timeRGB[i][1], test.timeRGB[i][2]))
    strip.show()
    while True:
        if test.new_time():
            for j in range(int(fade/0.1)):
                #print "FADING "
                if j != 0:
                    #k = float(j)
                    #print 'Prev', test.prev_timeRGB, 'Now', test.timeRGB, 'j', j, 'fade', fade
                    time.sleep(0.1)
                    for i in range(strip.numPixels()):
                            prop = j/(fade / 0.1)
                            #print prop
                            RED = int(test.prev_timeRGB[i][0] - (test.prev_timeRGB[i][0] - test.timeRGB[i][0])*prop)
                            GREEN = int(test.prev_timeRGB[i][1] - (test.prev_timeRGB[i][1] - test.timeRGB[i][1])*prop)
                            BLUE = int(test.prev_timeRGB[i][2] - (test.prev_timeRGB[i][2] - test.timeRGB[i][2])*prop)
                            #print RED, GREEN , BLUE
                            strip.setPixelColor(i, Color(RED, GREEN, BLUE))
                    strip.show()

