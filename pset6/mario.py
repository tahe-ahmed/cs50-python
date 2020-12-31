def main():
    try:
        while True:
            height = int(input("height : "))
            if height > 0:
                break
        printhashs(height)
    except ValueError:
        print("Height can only be a number ")


def printhashs(height):
    for i in range(1, height+1):
        print(" "*(height-i) + "#"*i + "  " + "#"*i + " "*(height-i))


main()
