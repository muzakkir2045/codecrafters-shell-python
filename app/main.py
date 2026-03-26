import sys


def main():
    builtins = ["type","echo","exit"]

    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break
        elif command.startswith("echo "):
            print(command[5:])
            continue
        elif command.startswith("type "):
            if command[5:] not in builtins:
                print(f"{command[5:]}: not found")
                continue
            print(f"{command[5:]} is a shell builtin")
        else:
            print(f"{command}: command not found ")


    pass


if __name__ == "__main__":
    main()
