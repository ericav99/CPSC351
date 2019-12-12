#By Eric Av and Cole Donovan
#Github repo name for Eric Av: CPSC351
# #Python version 3.8
import sys

class TM:
    current_state = None;
    def __init__(self, q, sigma, gamma, start_state, accept, reject):
        self.q = q
        self.sigma = sigma
        self.gamma = gamma
        self.start_state = start_state
        self.accept = accept
        self.reject = reject
        self.current_state = start_state
        return

    #Transition functions for the TM
    def trans_q1(self, input, index):
        
        if index >= len(input):
            self.current_state = 7
            self.decide()
        elif input[index] == '0':
            input[index] = ' '
            index += 1
            self.trans_q2(input, index)
        else:
            index += 1
            self.current_state = 7
            self.decide()
        return

    def trans_q2(self, input, index):
        self.current_state = 2
        
        if index >= len(input):
            self.current_state = 7
            self.decide()
        elif input[index] == '0':
            input[index] = 'x'
            index += 1
            self.trans_q3(input, index)
        elif input[index] == 'x':
            index += 1
            self.trans_q2(input, index)
        elif input[index] == ' ':
            index += 1
            self.current_state = 6
            self.decide()
        else:
            self.current_state = 7
            self.decide()
        return

    def trans_q3(self, input, index):
        self.current_state = 3
        
        if index >= len(input):
            self.current_state = 7
            self.decide()
        elif input[index] == '0':
            index += 1
            self.trans_q4(input, index)
        elif input[index] == 'x':
            index += 1
            self.trans_q3(input, index)
        elif input[index] == ' ':
            index -= 1
            self.trans_q5(input, index)
        else:
            self.current_state = 7
            self.decide()
        return
    
    def trans_q4(self, input, index):
        self.current_state = 4
        
        if index >= len(input):
            self.current_state = 7
            self.decide()
        elif input[index] == '0':
            input[index] = 'x'
            index += 1
            self.trans_q3(input, index)
        elif input[index] == 'x':
            index += 1
            self.trans_q4(input, index)
        elif input[index] == ' ':
            index += 1
            self.current_state = 7
            self.decide()
        else:
            self.current_state = 7
            self.decide()
        return

    def trans_q5(self, input, index):
        self.current_state = 5
        
        if index >= len(input):
            self.current_state = 7
            self.decide()
        elif input[index] == '0' or input[index] == 'x':
            index -= 1
            self.trans_q5(input, index)
        elif input[index] == ' ':
            index += 1
            self.trans_q2(input, index)
        else:
            self.current_state = 7
            self.self.decide()
        return

    def decide(self):
        if self.current_state == 6:
            print("Accept")
        else:
            print("Reject")
        return


    pass

#define the tuples
alphabet = ['0']
tape = ['0', 'x', ' ']
states = [1,2,3,4,5,6,7]
start = 1;
accept = [6]
reject = [7]

#loop that moves through each character in the given input_string
while True:
    # Input also to exit with cntrl-c
    try:
        input_string = input("Input string: ")
    except KeyboardInterrupt:
        sys.exit()

    inp = list(input_string)
    inp.append(" ")
    t = TM(states, alphabet, tape, start, accept, reject)
    if(input_string == "quit"):
        sys.exit()
    t.trans_q1(inp, 0)