from sys import argv
def subtract(args):
    res = 0
    for arg in args:
        res += int(arg)
    return res 


if __name__ == "__main__":
    argv.pop(0)
    print(subtract(argv))
