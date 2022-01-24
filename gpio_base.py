SYSFS_GPIO_OUTPUT_PATH  = "/sys/class/gpio"

#LED IR
SYSFS_LED_1_IR_PIN = "/sys/class/leds/led_1_ir_pin"
SYSFS_LED_2_IR_PIN = "/sys/class/leds/led_2_ir_pin"
SYSFS_LED_3_IR_PIN = "/sys/class/leds/led_3_ir_pin"
SYSFS_LED_4_IR_PIN = "/sys/class/leds/led_4_ir_pin"

#// LED
SYSFS_LED_1_PIN =  "/sys/class/leds/led_1_pin"
SYSFS_LED_2_PIN =  "/sys/class/leds/led_2_pin"
SYSFS_LED_3_PIN =  "/sys/class/leds/led_3_pin"
SYSFS_LED_4_PIN =  "/sys/class/leds/led_4_pin"

#// Step motor common
SYSFS_STEP_MOTOR_SLEEP = "/sys/class/leds/motor_sleep_pin"
SYSFS_STEP_MOTOR_RESET = "/sys/class/leds/motor_reset_pin"
SYSFS_STEP_MOTOR_ENABLE = "/sys/class/leds/motor_enable_pin"

#// Motor 1
SYSFS_STEP_MOTOR_1X_DIR_PIN  = "/sys/class/leds/motor_1x_dir_pin"
SYSFS_STEP_MOTOR_1X_STEP_PIN = "/sys/class/leds/motor_1x_step_pin"
SYSFS_STEP_MOTOR_1Y_DIR_PIN  = "/sys/class/leds/motor_1y_dir_pin"
SYSFS_STEP_MOTOR_1Y_STEP_PIN = "/sys/class/leds/motor_1y_step_pin"

#// Motor 2
SYSFS_STEP_MOTOR_2X_DIR_PIN  =  "/sys/class/leds/motor_2x_dir_pin"
SYSFS_STEP_MOTOR_2X_STEP_PIN = "/sys/class/leds/motor_2x_step_pin"
SYSFS_STEP_MOTOR_2Y_DIR_PIN  = "/sys/class/leds/motor_2y_dir_pin"
SYSFS_STEP_MOTOR_2Y_STEP_PIN = "/sys/class/leds/motor_2y_step_pin"

#// Motor 3
SYSFS_STEP_MOTOR_3X_DIR_PIN = "/sys/class/leds/motor_3x_dir_pin"
SYSFS_STEP_MOTOR_3X_STEP_PIN = "/sys/class/leds/motor_3x_step_pin"
SYSFS_STEP_MOTOR_3Y_DIR_PIN  = "/sys/class/leds/motor_3y_dir_pin"
SYSFS_STEP_MOTOR_3Y_STEP_PIN = "/sys/class/leds/motor_3y_step_pin"

#// Motor 4
SYSFS_STEP_MOTOR_4X_DIR_PIN  = "/sys/class/leds/motor_4x_dir_pin"
SYSFS_STEP_MOTOR_4X_STEP_PIN = "/sys/class/leds/motor_4x_step_pin"
SYSFS_STEP_MOTOR_4Y_DIR_PIN  = "/sys/class/leds/motor_4y_dir_pin"
SYSFS_STEP_MOTOR_4Y_STEP_PIN = "/sys/class/leds/motor_4y_step_pin"

MAX_BUF = 64

INPUT = 0
OUTPUT = 1

LOW  =  0
HIGH =   1

PWR_ON =  0
PWR_OFF =  1

## Implement clone funnctions as gpio.c

#/**************** INPUT ***************/
def gpio_export( gpio):

    fd = 0
    len = 0

    fd = open(SYSFS_GPIO_OUTPUT_PATH+"/export", "w")
    if (fd < 0):
        print("gpio/export")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", gpio)
    fd.write(str(gpio))
    fd.close()

    return 0


def gpio_unexport( gpio):

    fd = 0
    len = 0


    fd = open(SYSFS_GPIO_OUTPUT_PATH+"/unexport", "w")
    if (fd < 0):
        print("gpio/export")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", gpio)
    fd.write(str(gpio))
    fd.close()

    return 0


def gpio_set_dir(gpio,  direction):

    fd
    buf[MAX_BUF]

    #snprintf(buf, sizeof(buf), SYSFS_GPIO_OUTPUT_PATH  "/gpio%d/direction", gpio);
    fd = open(SYSFS_GPIO_OUTPUT_PATH+"/gpio"+gpio+"/direction","w")

    fd = open(buf, O_WRONLY)
    if (fd < 0):
        print("gpio/direction")
        return fd


    if (direction):
        fd.write("out")
    else:
        fd.write("in")

    fd.close()

    return 0


def gpio_set_value( gpio,  value):

    fd = 0
    #char buf[MAX_BUF]

    #fd = open (SYSFS_GPIO_OUTPUT_PATH"/gpio%d/value", gpio)
    fd = open (SYSFS_GPIO_OUTPUT_PATH+"/gpio"+gpio+"/value", "w")

    if (fd < 0):
        print("gpio/set-value")
        return fd


    if (value):
        fd.write("1")
    else:
        fd.write("0")

    fd.close()

    return 0



def gpio_get_value( gpio, value):

    f=0

    fd = open( SYSFS_GPIO_OUTPUT_PATH+"/gpio"+gpio+"/value", "r")

    if (fd < 0):
        print("gpio/get-value")
        return fd


    ch = fd.read()

    if (ch != '0'):
        value = 1
    else:
        value = 0


    fd.close()

    return value



def gpio_led_1_ir_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_LED_1_IR_PIN+"/brightness", "w")
    if (fd < 0):
        print("led_1_ir_pin/brightness")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0


def gpio_led_2_ir_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_LED_2_IR_PIN+"/brightness", "w")
    if (fd < 0):
        print("led_2_ir_pin/brightness")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_led_3_ir_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_LED_3_IR_PIN+"/brightness", "w")
    if (fd < 0):
        print("led_3_ir_pin/brightness")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_led_4_ir_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_LED_4_IR_PIN+"/brightness", "w")
    if (fd < 0):
        print("led_1_ir_pin/brightness")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

    #####LED ON OFF###########3

# gpio_led_1_pin
def gpio_led_1_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_LED_1_PIN+"/brightness", "w")
    if (fd < 0):
        print("led_1_ir_pin/brightness")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0


def gpio_led_2_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_LED_2_PIN+"/brightness", "w")
    if (fd < 0):
        print("led_3_pin/brightness")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_led_3_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 
    "/sys/class/leds/led_3_pin/brightness"

    fd = open(SYSFS_LED_3_PIN+"/brightness", "w")
    if (fd < 0):
        print("led_3_pin/brightness")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_led_4_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_LED_4_PIN+"/brightness", "w")
    if (fd < 0):
        perror("led_4_pin/brightness")
        return fd


    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0


    ##########Motor###########

def gpio_step_motor_sleep_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_STEP_MOTOR_SLEEP+"/brightness", "w")
    if (fd < 0):
        print("motor_sleep_pin/brightness")
        return fd

        #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_reset_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_STEP_MOTOR_RESET+"/brightness", "w")
    if (fd < 0):
        print("motor_reset_pin/brightness")
        return fd

        #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_enable_pin( value):

    fd = 0
    len = 0
    #buf[]  = value 

    fd = open(SYSFS_STEP_MOTOR_ENABLE+"/brightness", "w")
    if (fd < 0):
        print("motor_enable_pin/brightness")
        return fd

        #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0
##########################
##########Motor 1 ##########################

def gpio_step_motor_1x_dir_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_1X_DIR_PIN+"/brightness", "w")
    if (fd < 0):
        print("otor_1x_dir_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_1x_step_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_1X_STEP_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_1x_step_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0





def gpio_step_motor_1y_dir_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_1Y_DIR_PIN+"/brightness", "w")
    if (fd < 0):
        print("otor_1y_dir_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0


def gpio_step_motor_1y_step_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_1Y_STEP_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_1y_step_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

####### Motor 2 #########

def gpio_step_motor_2x_dir_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_2X_DIR_PIN+"/brightness", "w")
    if (fd < 0):
        print("otor_2x_dir_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_2x_step_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_2X_STEP_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_2x_step_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0


def gpio_step_motor_2y_dir_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_2Y_DIR_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_2y_dir_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_2y_step_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_2Y_STEP_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_2y_step_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0



##########################Motor 3 ###################3


def gpio_step_motor_3x_dir_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_3X_DIR_PIN+"/brightness", "w")
    if (fd < 0):
        print("otor_3x_dir_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_3x_step_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_3X_STEP_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_3x_step_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0


def gpio_step_motor_3y_dir_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_3Y_DIR_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_3y_dir_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_3y_step_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_3Y_STEP_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_3Y_step_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0


#############Motor 4 ######################3

def gpio_step_motor_4x_dir_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_4X_DIR_PIN+"/brightness", "w")
    if (fd < 0):
        print("otor_4x_dir_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_4x_step_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_4X_STEP_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_4x_step_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_4y_dir_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_4Y_DIR_PIN+"/brightness", "w")
    if (fd < 0):
        print("otor_4y_dir_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0

def gpio_step_motor_4y_step_pin(value):

    fd = 0
    len = 0
    #buf[]  = value

    fd = open(SYSFS_STEP_MOTOR_4Y_STEP_PIN+"/brightness", "w")
    if (fd < 0):
        print("motor_4y_step_pin/brightness")
        return fd

    #len = snprintf(buf, sizeof(buf), "%d", value)
    #write(fd, buf, len)
    fd.write(str(value))
    fd.close()

    return 0


import time

#usleep 
usleep = lambda x: time.sleep(x/1000000.0)


print("Test LED IR.\r\n")
gpio_led_1_ir_pin(HIGH)
gpio_led_2_ir_pin(HIGH)
gpio_led_3_ir_pin(HIGH)
gpio_led_4_ir_pin(HIGH)
time.sleep(1)
gpio_led_1_ir_pin(LOW)
gpio_led_2_ir_pin(LOW)
gpio_led_3_ir_pin(LOW)
gpio_led_4_ir_pin(LOW)

print("Test LED.\r\n")
gpio_led_1_pin(HIGH)
gpio_led_2_pin(HIGH)
gpio_led_3_pin(HIGH)
gpio_led_4_pin(HIGH)
time.sleep(1)
gpio_led_1_pin(LOW)
gpio_led_2_pin(LOW)
gpio_led_3_pin(LOW)
gpio_led_4_pin(LOW)



time.sleep(1)
print("Testing Motor function ")
gpio_step_motor_sleep_pin(HIGH)
gpio_step_motor_reset_pin(HIGH)
gpio_step_motor_enable_pin(LOW)
for j in range(3):
    print("Run...")
    gpio_step_motor_1x_dir_pin(HIGH)
    gpio_step_motor_1y_dir_pin(HIGH)
    gpio_step_motor_2x_dir_pin(HIGH)
    gpio_step_motor_2y_dir_pin(HIGH)
    gpio_step_motor_3x_dir_pin(HIGH)
    gpio_step_motor_3y_dir_pin(HIGH)
    gpio_step_motor_4x_dir_pin(HIGH)
    gpio_step_motor_4y_dir_pin(HIGH)
    for i in range(100):
        gpio_step_motor_1x_step_pin(HIGH)
        gpio_step_motor_1y_step_pin(HIGH)
        gpio_step_motor_2x_step_pin(HIGH)
        gpio_step_motor_2y_step_pin(HIGH)
        gpio_step_motor_3x_step_pin(HIGH)
        gpio_step_motor_3y_step_pin(HIGH)
        gpio_step_motor_4x_step_pin(HIGH)
        gpio_step_motor_4y_step_pin(HIGH)
        #time.sleep(0.001)
        #time.sleep(1)
        #time.sleep(500/1000000.0)
        usleep(50)
        gpio_step_motor_1x_step_pin(LOW)
        gpio_step_motor_1y_step_pin(LOW)
        gpio_step_motor_2x_step_pin(LOW)
        gpio_step_motor_2y_step_pin(LOW)
        gpio_step_motor_3x_step_pin(LOW)
        gpio_step_motor_3y_step_pin(LOW)
        gpio_step_motor_4x_step_pin(LOW)
        gpio_step_motor_4y_step_pin(LOW)
        #time.sleep(0.001)
        #time.sleep(500/1000000.0)
        usleep(50)
        #print("Running Motor")





gpio_step_motor_sleep_pin(LOW);