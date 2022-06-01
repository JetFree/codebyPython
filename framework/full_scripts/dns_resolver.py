import dns.resolver


def get_MX_record():
    print("5. DNS MX-Record\n")
    address = input("Enter host: ")
    if address:
        my_resolver = dns.resolver.Resolver(configure=False)
        my_resolver.nameservers = ['8.8.8.8', '1.1.1.1']
        try:
            answers = my_resolver.resolve(address, "MX", search=True)

            for rdata in answers:
                print("MX Record: ", rdata.exchange)
        except Exception as e:
            print(e)