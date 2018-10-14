
import math
from gpiozero import LED
global LEDs = [2,3,4,17,27,22,10,9,11,0,5,6,13,19, # LED values in clockwise order,
        26,14,15,18,23,24,25,8,7,1,12,16,20,21] # ending with the 5Vs after
global playing = 0 # Keeps track of if here is audio playing

# Note: consider max number of lights on output decice

# signal is the audio signal sent from the device
# regions are the number of regions to colorize
# lights is the number of lights in the output console. 0 if gradient is 0
# grad_type determines the direction/type of gradient.  0=left to right
# board determines whether the output will go to the board or back to the incoming device
def translation_circuit(signal, regions, lights = 0, board = False):
    # r = num_lights if num_lights < r
    vals = [len(signals)][r]

    # TODO: This is where the signal gets filtered into interpretable data
    # filtered_signal = []
    # TODO: This is where the filtered signal gets converted into RGB values

    if board:
        for i in range(1, r+1, type=float):

    return [math.random(255) for val in vals]# placeholder for random values

def translation_rgb(signal, regions, lights = 0, grad_type = 0, board = False):
    rgb_vals = [r][3]

    # TODO: This is where the signal gets filtered into interpretable data
    # filtered_signal = []
    # TODO: This is where the filtered signal gets converted into RGB values

    if
    return [[math.random(255) for val in vals] for vals in rgb_vals]# placeholder for random values

def output_lights(light_vals):
    return # TODO?
