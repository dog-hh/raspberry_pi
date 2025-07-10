import PicoMotorDriver 
import utime 
import machine
board = PicoMotorDriver.KitronikPicoMotor() 
#碰撞判断，如果碰上就会返回1
forward_bumper = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_DOWN) 
def forward(speed): 
    board.motorOn(1, "r", speed) 
    board.motorOn(2, "f", speed) 
def reverse(speed): 
    board.motorOn(1, "f", speed) 
    board.motorOn(2, "r", speed)  
def left(speed): 
    board.motorOn(1, "f", speed) 
    board.motorOn(2, "f", speed) 
def right(speed): 
    board.motorOn(1, "r", speed) 
    board.motorOn(2, "r", speed)    
def stop(): 
    board.motorOff(1) 
    board.motorOff(2) 
    utime.sleep(5) 
while True: 
    if forward_bumper.value() == 1: 
        print("Reverse") 
        reverse(75) 
        utime.sleep(1) 
        stop() 
        print("Left") 
        left(75) 
        utime.sleep(1) 
        stop() 
    else: 
        print("Forward") 
        forward(75) 
        utime.sleep(5)