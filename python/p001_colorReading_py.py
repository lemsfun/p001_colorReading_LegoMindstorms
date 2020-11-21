from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()


# Write your program here.
hub.speaker.beep()

hub.status_light.off()
hub.light_matrix.write('L E M S')
wait_for_seconds(1)

while 1:
    hub.light_matrix.set_pixel(0, 1)
    hub.light_matrix.set_pixel(0, 2)
    hub.light_matrix.set_pixel(1, 0)
    hub.light_matrix.set_pixel(1, 1)
    hub.light_matrix.set_pixel(2, 0)
    hub.light_matrix.set_pixel(3, 0)
    hub.light_matrix.set_pixel(4, 1)
    hub.light_matrix.set_pixel(4, 2)
    hub.light_matrix.set_pixel(3, 2)
    hub.light_matrix.set_pixel(2, 3)
    hub.light_matrix.set_pixel(2, 4)
    hub.status_light.off()

    paper_scanner = ColorSensor('A')

    color = paper_scanner.get_color()

    if color == 'red' or color == 'yellow' or color == 'green' or color == 'blue' or color == 'white':
        hub.status_light.on(color)
        hub.light_matrix.write(color.upper())
        wait_for_seconds(1)
