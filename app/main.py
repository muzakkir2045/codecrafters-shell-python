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
        elif command.startswith("type ") and command[5:] in builtins:
            print(f"{command[5:]} is a shell builtin")
            continue
        else:
            print(f"{command}: command not found ")


    pass


if __name__ == "__main__":
    main()
