#By Eric Av and Cole Donovan
#Github repo name for Eric Av: CPSC351
# #Python version 3.8
import sys

#define the tuples
alphabet = ['0','1']
states = [0,1,2,3,4,5,6,7,8,9]
start = 0;
current_state = start
accept = [8]

#define the transition states
transition_states = {0:{'0':1, '1':9}, 1:{'0':2, '1':9}, 2:{'0':3, '1':9}, 3:{'0':9, '1':4},
                     4:{'0':5, '1':5}, 5:{'0':6, '1':5}, 6:{'0':7, '1':5}, 7:{'0':8, '1':4},
                     8:{'0':9, '1':9}, 9:{'0':9, '1':9}}

#Input and also functionality to exit with cntrl-c
f = open("proj9-3.txt", "r")
if f.mode == "r":
    input_string = f.read()
else:
    sys.exit()
#loop that moves through each character in the given input_string

for character in str(input_string):
    if not character in alphabet:
        current_state = 9
    else:
        current_state = transition_states[current_state][character]
if current_state in accept:
    print("Accepted")
else:
    print("Rejected")

