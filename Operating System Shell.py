import os


def shell():
    while True:
        command = input("$ ")

        if command == "exit":
            break

        # Split the command into tokens
        tokens = command.split()

        if tokens:
            # Get the command and arguments
            cmd = tokens[0]
            args = tokens[1:]

            # Execute the command
            try:
                if cmd == "cd":
                    os.chdir(args[0])  # Change directory
                else:
                    os.system(command)  # Execute system command
            except Exception as e:
                print("Error:", e)


# Run the shell
shell()
