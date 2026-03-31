import sys
import subprocess
import os

def main():
    builtins = ["type","echo","exit"]
    while True:
        path_env = os.environ.get("PATH")
        search_dirs = path_env.split(os.pathsep)
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
                    full_path = os.path.join(dir, command[5:])
                    if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                        
                        print(f"{command[5:]} is {full_path}")
                        break
                else:
                    print(f"{command[5:]}: not found")
    
        else:
            args  = command.split()
            for dir in search_dirs:
                full_path = os.path.join(dir, args[0])
                if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                    subprocess.run(args)

                    break
            else:
                print(f"{command[5:]}: not found")

            


if __name__ == "__main__":
    main()
