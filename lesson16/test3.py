import argparse
import os


class Runner:

    def __init__(self):
        if args.system:
            print("System parameter")
            self.run_system()
        elif args.chmod:
            print("Chmod parameter")
        elif args.tree:
            print("Tree parameter")

    def run_system(self):
        print(os.getlogin())
        while (cmd := input("Shell command: ")) != "exit":
            os.system(cmd)
        print("The work was completed!")


    def run_chmod(self):
        pass

    def run_dir_tree(self):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System management program")
    parser.add_argument("-s", "--system", help="System command")
    parser.add_argument("-c", "--chmod", help="Checking access rights")
    parser.add_argument("-t", "--tree", help="Directory tree")
    args = parser.parse_args()
    Runner()
