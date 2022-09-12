import time
import RPi.GPIO as GPIO
#import RPi.GPIO as GPIO
import argparse 

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.")

parser.add_argument("--x", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--y", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--ir", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--blue", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--uv", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")



p1,p2 = 25,24 # direction, pulse 
q1,q2 = 16,12 # direction, pulse 
ir_id = 23
blue_id = 10
uv_id = 8
s = 11

try:
    opt = parser.parse_known_args()[0]
except:
    print("error parsing")
    parser.print_help()
    sys.exit(0)

# pin setup
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(27,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)


GPIO.output(s, False)
GPIO.output(11, True)


#GPIO.output(21, False)
#GPIO.output(20, False)

# Motor and driver functions


WaitTime = .0005
print('hi')
def motor(d,p1,p2):
    n = int(abs(d)/ (2*5.625 * 1/64))
    print('motor: ', n)
    if d>0:
        A = False
    else:
        A = True


    #print(p1,A)
    GPIO.output(p1, A)

    for i in range(n):        
        GPIO.output(p2, False)
        time.sleep(WaitTime)
        GPIO.output(p2, True)
        time.sleep(WaitTime)


def UV_driver(x,y,uv,p1,p2,q1,q2,l):
    
    if uv:
        GPIO.output(uv_id,True)
        print(uv_id,'True')
    else:
        GPIO.output(uv_id,False)
        print(uv_id,'False')

    
    if blue:
        GPIO.output(blue_id,True)
        print(blue_id,'True')
    else:
        GPIO.output(blue_id,False)
        print(blue_id,'False')
        
    
    if ir:
        GPIO.output(ir_id,True)
        print(ir_id,'True')
    else:
        GPIO.output(ir_id,False)
        print(ir_id,'False')
        
        
    if x!=0 or y !=0:
        print('controlling motor...')
        GPIO.output(s, True)
        motor(x,p1,p2)
        motor(y,q1,q2)
        GPIO.output(s, False)



### main code



if opt.uv:
    uv=True
else:
    uv=False

if opt.ir:
    ir=True
else:
    ir=False
    
if opt.blue:
    blue=True
else:
    blue=False
    
    
UV_driver(x= opt.x, y=opt.y, uv=uv,ir=ir,blue=blue,p1=p1,p2=p2,q1=q1,q2=q2)
GPIO.output(11, False)
