#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)-1))
    else:
        if len(sys.argv) == 2:
            print("{}argument:".format(len(sys.argv)-1))
        else:
            print("{}arguments:".format(len(sys.argv)-1))

        for av in range(1, len(sys.argv)):
            print("{} : {}".format(av, (sys.argv[av])))
