from pip._vendor.distlib.compat import raw_input
#By Eric Av
#Github repo name: CPSC351
#Python version 3.8

true = 0
def main():
    global true
    length = 0;
    while(length==0):
        transition = [[[3], [1]], [[2], [2]], [[3], [1]], [[3], [3]]]
        booleanToStart = 1
        #dfa transition of L2 = {w | every odd position of w is a 1}
        print("Test values:")
        print("1010... should be true")
        print("10010... should be false")
        print("01... should be false")
        print("00... should be false")
        print("110... should be false\n")
        input = raw_input("Type in a string of 1's and 0's to see if it is an acceptable string: ")
        print("Test values:")
        print("1010... should be true")
        print("10010... should be false")
        print("01... should be false")
        print("00... should be false")
        print("110... should be false\n")
        input = list(input)
        for index in range(len(input)):
            if input[index] == '0':
                input[index] = '0'
            if input[index] == '1':
                input[index] = '1'
            if input[index] != '0' and input[index] != '1': #error checking out of bounds
                booleanToStart = 0

        final = "121"
        start = 0
        i = 0
        if booleanToStart == 1:
            simulate(transition, input, final, start, i)
        if true == 0 or booleanToStart == 0:
            print("Result with " + input.__str__() + ": rejected")
        if true == 1:
            print("Result with " + input.__str__() + ": accepted")
        true = 0

def simulate(transition, input, final, state, i):
    global true
    for j in range (len(input)):
        if[input[j] == '0' or input[j] == '1']:
            for each in transition[state][int(input[j])]:
                if each < 4:
                    state = each
                    if j == len(input)-1 and (str(state) in final):
                        true = 1
                    simulate(transition, input[i+1:], final, state, i)

        i = i+1
main()