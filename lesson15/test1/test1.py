import argparse


class EmailFilter:

    def __init__(self):
        self.base_file = "base.txt"
        content = self.get_file_content()
        content = self.filter_emails(content)
        self.create_result_file(content)

    def get_file_content(self):
        with open(self.base_file, "r") as file:
            return file.readlines()

    def filter_emails(self, lines):
        result_list = list()
        for line in lines:
            if line.split(":")[0].endswith(args.domain):
                result_list.append(line)
        return result_list

    def create_result_file(self, lines):
        with open(f"email_{args.domain}.txt", "w") as result_file:
            result_file.writelines(lines)
        print("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="filter email by domain and create new file with filtered emails")
    parser.add_argument("domain", type=str, help="domain to filter by")
    args = parser.parse_args()
    EmailFilter()
