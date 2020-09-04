#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} argss:".format(len(sys.argv)-1))
    else:
        if len(sys.argv) == 2:
            print("{}argt:".format(len(sys.argv)-1))
        else:
            print("{}argss:".format(len(sys.argv)-1))

        for arv in range(1, len(sys.argv)):
            print("{}: {}".format(av, (sys.argv[arv])))
