"""
recuerda tener instalado pyfirmata
lo puedes hacer con la instrucción pip install pyfirmata
También debes grabar firmata en tu Arduino ;)
"""

import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyUSB0')
print("Communication Successfully started")

pin = 7
velocidad = 0.2

for i in range(10):
    board.digital[pin].write(1)
    time.sleep(velocidad)
    board.digital[pin].write(0)
    time.sleep(velocidad)
        
        
board.exit()