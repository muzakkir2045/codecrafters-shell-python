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
                for dir in search_dirs:
                    full_path = f"dir/{command[5:]}"
                    if os.path.exists(full_path) and os.access(full_path):
                        print(f"{command[5:]} is {full_path}")


                    # if dir.split("/")[-1] == command[5:]:
                    #     print(f"{command[5:]} is dir")
                    # print(dir)
        

        else:
            print(f"{command}: command not found ")


    


if __name__ == "__main__":
    main()
