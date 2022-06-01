import sys
import whois


def get_info():
    print("3. Whois\n")
    add = input("Enter domain: ")
    if add:
        try:
            domain = whois.query(add)
        except Exception as e:
            print(e)
            sys.exit(0)
        res = domain.__dict__
        for i in res:
            print(i, res[i], sep=": ")
