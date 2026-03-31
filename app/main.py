import sys
import os

def main():
    builtins = ["type","echo","exit"]
    path_env = os.environ.get("PATH")
    search_dirs = path_env.split(":")
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break
        elif command.startswith("echo "):
            print(command[5:])
            continue
        elif command.startswith("type "):
            if command[5:] in builtins:
                print(f"{command[5:]} is a shell builtin")
                continue
            else:
                for dir in search_dirs:
                    if dir.split("/")[-1] == command[5:]:
                        print(f"{command[5:]} is dir")
            print(f"{command[5:]}: not found")

        else:
            print(f"{command}: command not found ")


    


if __name__ == "__main__":
    main()
