#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{}argument:".format(len(sys.argv)-1))
    else:
        if len(sys.argv) == 2:
            print("{}arguments:".format(len(sys.argv)-1))
        else:
            print("{}argument:".format(len(sys.argv)-1))

        for arv in range(1, len(sys.argv)):
            print("{} : {}".format(arv, (sys.argv[arv])))
