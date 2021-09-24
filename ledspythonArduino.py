"""
recuerda tener instalado pyfirmata
lo puedes hacer con la instrucción pip install pyfirmata
También debes grabar firmata en tu Arduino ;)
"""

import pyfirmata
import time

def parpadear(board,pin,veces,velocidad):
    for i in range(veces):
        board.digital[pin].write(1)
        time.sleep(velocidad)
        board.digital[pin].write(0)
        time.sleep(velocidad)
        
def main():
    ledRojo = 9
    ledAmarillo = 7
    velocidad = 0.1
    board = pyfirmata.Arduino('/dev/ttyUSB0')
    print("Communication Successfully started")
    parpadear(board,ledRojo,8,velocidad)    
    board.exit()

if __name__ == '__main__':
    main()