import sys


def main():
    
    command = input("$ ")
    if command == "xyz":
        sys.stdout.write(f"{command}: command not found ")
    pass


if __name__ == "__main__":
    main()
