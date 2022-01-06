import argparse
import itertools
import datetime
import random


class CombinationGenerator:

    def __init__(self, length):
        self.length = int(length)
        comb_list = self.generate_combinations()
        self.print_result(comb_list)
        self.write_to_file(comb_list)

    def generate_combinations(self):
        int_list = random.sample("0123456789", self.length)
        comb_list = list(itertools.product(int_list, repeat=4))
        random.shuffle(comb_list)
        return comb_list

    def print_result(self, comb_list):
        print(f"Start process...\nКоличество комбинаций: {len(comb_list)}")
        [print("".join(comb)) for comb in comb_list]

    def write_to_file(self, comb_list):
        time_start = datetime.datetime.now()
        with open(f"num_dict{self.length}.txt", "w") as file:
            file.writelines([("".join(comb) + "\n") for comb in comb_list])
        result = datetime.datetime.now().timestamp() - time_start.timestamp()
        print(f"Completed in: {result:.2f} sec.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int, help="length of combinations")
    args = parser.parse_args()
    CombinationGenerator(args.length)
