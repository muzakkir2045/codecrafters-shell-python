import sys
import os

def main():
    builtins = ["type","echo","exit"]
    while True:
        path_env = os.environ.get("PATH")
        search_dirs = path_env.split(":")
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
                found = False
                for dir in search_dirs:
                    # full_path = os.path.join(dir, command[5:])
                    full_path = f"{dir}/{command[5:]}"
                    if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                        found = True
                        print(f"{command[5:]} is {full_path}")
                        break
                if not found:
                    print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found ")


if __name__ == "__main__":
    main()
