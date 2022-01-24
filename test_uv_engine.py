import time
import sys
import argparse 
from gpio import (
gpio_led_1_pin,
gpio_led_2_pin,
gpio_led_3_pin,
gpio_led_4_pin,
gpio_led_1_ir_pin,
gpio_led_2_ir_pin,
gpio_led_3_ir_pin,
gpio_led_4_ir_pin,
gpio_step_motor_sleep_pin,
gpio_step_motor_reset_pin,
gpio_step_motor_enable_pin,
gpio_step_motor_1x_dir_pin,
gpio_step_motor_2x_dir_pin,
gpio_step_motor_3x_dir_pin,
gpio_step_motor_4x_dir_pin,
gpio_step_motor_1y_dir_pin,
gpio_step_motor_2y_dir_pin,
gpio_step_motor_3y_dir_pin,
gpio_step_motor_4y_dir_pin,
gpio_step_motor_1x_step_pin,
gpio_step_motor_2x_step_pin,
gpio_step_motor_3x_step_pin,
gpio_step_motor_4x_step_pin,
gpio_step_motor_1y_step_pin,
gpio_step_motor_2y_step_pin,
gpio_step_motor_3y_step_pin,
gpio_step_motor_4y_step_pin
)

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.")

parser.add_argument("--LED_id", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--x", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--y", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--light", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument("--ir", type=int, default=0, help="desired height of camera stream (default is 720 pixels)")


try:
    opt = parser.parse_known_args()[0]
except:
    print("error parsing")
    parser.print_help()
    sys.exit(0)

usleep = lambda x: time.sleep(x/1000000.0)

HIGH = 1
LOW = 0


def UV_driver(x=0, y=0, LED_id=0, light_on=False, ir_on=False):
  
    gpio_step_motor_sleep_pin(HIGH)
    gpio_step_motor_reset_pin(HIGH)
    gpio_step_motor_enable_pin(LOW)
    
    n_x = int(abs(x)*50)
    d_x = 0 if x > 0 else 1

    n_y = int(abs(y)*150)
    d_y = 0 if y > 0 else 1

    # LED_id 0:
    if LED_id == 0:

        # set directions
        gpio_step_motor_4x_dir_pin(d_x)
        gpio_step_motor_4y_dir_pin(d_y)
        

        print('n_x',n_x)
        # move motor x
        for i in range(n_x):
            gpio_step_motor_4x_step_pin(LOW)
            usleep(50)
            gpio_step_motor_4x_step_pin(HIGH)
            usleep(50)

        # move motor x
        print('n_y',n_y)
        for i in range(n_y):
            gpio_step_motor_4y_step_pin(LOW)
            usleep(50)
            gpio_step_motor_4y_step_pin(HIGH)
            usleep(50)

        # light on
        if light_on:
            gpio_led_4_pin(HIGH)
        else:
            gpio_led_4_pin(LOW)

        if ir_on:
            gpio_led_4_ir_pin(HIGH)
        else:
            gpio_led_4_ir_pin(LOW)

    gpio_step_motor_sleep_pin(LOW)

UV_driver(x= opt.x, y=opt.y, LED_id=opt.LED_id, light_on=opt.light, ir_on=opt.ir)