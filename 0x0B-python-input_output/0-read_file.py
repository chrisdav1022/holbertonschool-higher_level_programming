#!/urs/bin/python3
"""read file"""


def read_file(filename=""):
    """read and print text"""
    with open(filename, 'r') as fl:
        print(fl.read(), end="")
