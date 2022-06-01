from dns import reversename, resolver


def reverse_dns():
    print("6. Reverse DNS\n")
    ip = input("Enter ip: ")
    if ip:
        try:
            rev_name = reversename.from_address(ip)
            reversed_dns = str(resolver.resolve(rev_name, "PTR", search=True)[0])
            print(reversed_dns)
        except Exception as e:
            print(e)
