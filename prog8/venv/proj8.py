from pip._vendor.distlib.compat import raw_input
#By Eric Av
#Github repo name: CPSC351
#Python version 3.8

true = 0
oneFalse = 0
def main():
    global true
    global oneFalse #Begins with a one is a reject variable
    length = 0;
    while(length==0):
        transition = [[[1], [4]], [[1], [2]], [[3], [2]], [[4], [4]]]
        #transition with account for $ going to state 4
        booleanToStart = 1
        #PDA transition of T = { 0^n1^n | n >= 0}
        input = raw_input("Type in a string of 1's and 0's to see if it is an acceptable string: ")
        input = list(input)
        for index in range(len(input)):
            if input[index] == '0':
                input[index] = '0'
            if input[index] == '1':
                input[index] = '1'
            if input[index] == '$': #$ transition
                input[index] = '$'
            if input[index] != '0' and input[index] != '1': #error checking out of bounds
                booleanToStart = 0
        final = "02" # final state when popping of the stack to decide whether or not it is a reject or accept
        start = 0
        i = 0
        if booleanToStart == 1:
            simulate(transition, input, final, start, i)
        if true == 0 or booleanToStart == 0 or oneFalse == 1:
            print("Result with " + input.__str__() + ": rejected")
        elif true == 1:
            print("Result with " + input.__str__() + ": accepted")
        true = 0
        oneFalse = 0

def simulate(transition, input, final, state, i):
    global true
    global oneFalse
    for j in range (len(input)):
        if[input[j] == '0' or input[j] == '1' or input[j] == '$']:
            for each in transition[state][int(input[j])]:
                if each < 4:
                    state = each
                    if j == len(input)-1 and (str(state) in final):
                        true = 1
                    simulate(transition, input[i+1:], final, state, i)
                if each >= 4:
                    oneFalse = 1
                    true = 0
        i = i+1 #pops the top element of the stack and moves to the next element
main()