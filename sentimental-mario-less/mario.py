
def main():
    while True:
        height = int(input("Height:"))
        if 1<= height <= 8:
            break;
    for i in range(1,height+1):
        print(" " * (height-i) + "#" * i)


if __name__ == "__main__":
    main()
