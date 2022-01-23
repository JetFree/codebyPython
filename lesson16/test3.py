import argparse
import os
import stat


class Runner:

    def __init__(self):
        if args.system:
            print("System parameter")
            self.run_system()
        elif args.chmod:
            print("Chmod parameter")
            self.run_chmod()
        elif args.tree:
            print("Tree parameter")
            self.run_dir_tree()

    def run_system(self):
        while cmd := input("Shell command: "):
            if cmd == "exit":
                print("The work was completed!")
                break
            elif os.system(cmd) != 0:
                print("Wrong command, exit!")
                break

    def run_chmod(self):
        while path := input("Enter the path: "):
            if path == "exit":
                print("The work was completed!")
                break
            elif os.path.exists(path):
                print(str(oct(stat.S_IMODE(os.lstat(path).st_mode)))[-3:])
            else:
                print("The file or directory does not exist!")

    def run_dir_tree(self):
        while path := input("Enter the path: "):
            if path == "exit":
                print("The work was completed!")
                break
            elif os.path.exists(path):
                result = os.system(f"tree {path}")
            else:
                print("The file or directory does not exist!")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System management program")
    parser.add_argument("-s", "--system", help="System command")
    parser.add_argument("-c", "--chmod", help="Checking access rights")
    parser.add_argument("-t", "--tree", help="Directory tree")
    args = parser.parse_args()
    Runner()
