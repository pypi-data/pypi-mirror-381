from pylips.speech import RobotFace
import time

robot = RobotFace()
robot.say("Hello, I am your robot face!", wait=True)

stop_loop = False
while not stop_loop:
    try:
        stop = input("Type in what you would like the robot to say (type exit to stop): ")
        robot.say(stop, wait=False)
        robot.stream_file_to_browser('default_output')
        if stop.lower() == 'exit':
            stop_loop = True
    except TimeoutError:
        robot.say("I am still here. Say 'stop' to end.", wait=True)


