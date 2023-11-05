# from printrun import gcoder
import time

from printrun.printcore import printcore

# or p.printcore('COM3',115200) on Windows
p = printcore('/dev/ttyUSB0', 115200)
p = printcore('/dev/tty.usbserial-140', 115200)
# or pass in your own array of gcode lines instead of reading from a file
# gcode = [i.strip() for i in open('filename.gcode')]
# gcode = gcoder.LightGCode(gcode)

# startprint silently exits if not connected yet print("Connecting...")
XMAX = 40
YMAX = 32


def kickFront():
    p.send("G0 E02")
    p.send("G04 P10")
    p.send("G0 E-2")
    p.send("G04 P10")
    p.send("G0 E0")


def kickBack():
    p.send("G0 Z02")
    p.send("G04 P10")
    p.send("G0 Z-2")
    p.send("G04 P10")
    p.send("G0 Z0")

def setup():
    print("Connecting...")
    while not p.online:
        time.sleep(0.1)

    print("Connected")

    p.send("M502")
    p.send("G28 X Y")
    p.send("M204 T5000 P5000 R5000 S5000")
    p.send("M203 E5000 Z5000 X5000 Y5000")
    p.send("M201 E5000 Z5000 X5000 Y5000")
    p.send("M92 X180 Y180 E300 Z200")
    p.send("M220 S200")

    p.send("G0 Z2")
    p.send("G0 E0")

    p.send("G0 X"+str(XMAX//2))
    p.send("G0 Y"+str(YMAX//2))

def userCalibrate():
    p.send("M18")
    p.send("G04 S4")
    p.send("M17")

def turnOnLight(seconds):
    p.send("M106 S255")
    p.send("G04 S" + str(seconds))
    p.send("M107")

def moveBoth(front, back):
    if front > 100:
        front = 100
    if back > 100:
        back = 100
    if front < 0:
        front = 0
    if back < 0:
        back = 0

    front = round((front/100) * XMAX)
    back = round((back/100) * YMAX)

    p.send("G0 X" + str(front) + " Y" + str(back))

def moveFront(val):
    if val > 100:
        val = 100
    if val < 0:
        val = 0
    val = round((val/100) * XMAX)

    p.send("G0 X" + str(val))

def moveBack(val):
    if val > 100:
        val = 100
    if val < 0:
        val = 0

    val = round((val/100) * YMAX)

    p.send("G0 Y" + str(val))
