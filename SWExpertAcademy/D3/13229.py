#import sys
#sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    week = input()
    # print(week)

    if week == "SUN":
        ret = 7
    elif week == "MON":
        ret = 6
    elif week == "TUE":
        ret = 5
    elif week == "WED":
        ret = 4
    elif week == "THU":
        ret = 3
    elif week == "FRI":
        ret = 2
    elif week == "SAT":
        ret = 1

    print("#"+str(test_case)+" "+str(ret))
    # ///////////////////////////////////////////////////////////////////////////////////
