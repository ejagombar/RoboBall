from printrun.printcore import printcore
# from printrun import gcoder
import time
# or p.printcore('COM3',115200) on Windows
p = printcore('/dev/ttyUSB0', 115200)
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
    p.send("G0 Z18")

def setup():
    print("Connecting...")
    while not p.online:
        time.sleep(0.1)

    print("Connected")

    print("Turning off Fans")
    # p.send_now("M107")
    # If you need to interact with the printer:
    # this will send M105 immediately, ahead of the rest of the print
    # p.send_now("M105")

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

# Fan On
# p.send("M106 S255")
# p.send("G04 S1")
# p.send("M107")
# p.send("G04 S1")

# p.send("M18")
# p.send("G04 S4")
# p.send("M17")

# kickFront()
# p.send("G04 S1")

def move(front, back):
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

# i = 0
# while 1:
#     i = i + 1
#     p.send("G0 X" + str(i % XMAX))

#     p.send("G0 Y" + str(i % YMAX))
#     time.sleep(0.01)

# p.pause()  # use these to pause/resume the current print
# p.resume()
# p.disconnect()  # this is how you disconnect from the printer once you are done
