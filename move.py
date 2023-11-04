from printrun.printcore import printcore
# from printrun import gcoder
import time
# or p.printcore('COM3',115200) on Windows
p = printcore('/dev/ttyUSB0', 115200)
# or pass in your own array of gcode lines instead of reading from a file
# gcode = [i.strip() for i in open('filename.gcode')]
# gcode = gcoder.LightGCode(gcode)

# startprint silently exits if not connected yet print("Connecting...")

print("Connecting...")
while not p.online:
    time.sleep(0.1)

print("Connected")

# If you need to interact with the printer:
# this will send M105 immediately, ahead of the rest of the print
p.send_now("M105")
p.send_now("G28")
p.pause()  # use these to pause/resume the current print
p.resume()
p.disconnect()  # this is how you disconnect from the printer once you are done
