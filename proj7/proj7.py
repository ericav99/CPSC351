#By Eric Av
#Github repo name: CPSC351
# #Python version 3.8
import sys

#define the tuples
alphabet = ['0','1']
states = [0,1,2,3]
start = 0;
accept = [0,1,2]

#define the transition states
transition_states = {0:{'0':3, '1':1}, 1:{'0':2, '1':2}, 2:{'0':3, '1':1}, 3:{'0':3, '1':3}}

#Input and also functionality to exit with cntrl-c
try:
    input_string = str(input("Input string: "))
except KeyboardInterrupt:
    sys.exit()

#loop that moves through each character in the given input_string
while True:
    current_state = start
    for character in str(input_string):
        if not character in alphabet:
            current_state = 3
        else:
            current_state = transition_states[current_state][character]
    if current_state in accept:
        print("Accepted")
    else:
        print("Rejected")

    #Input also to exit with cntrl-c
    try:
        input_string = input("Input string: ")
    except KeyboardInterrupt:
        sys.exit()
