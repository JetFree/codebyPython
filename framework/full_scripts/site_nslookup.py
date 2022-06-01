from nslookup import Nslookup


def run_nslookup():
    print("4. Nslookup\n")
    domain = input("Enter host: ")
    if domain:
        dns_query = Nslookup(dns_servers=["1.1.1.1"])
        ips_record = dns_query.dns_lookup(domain)
        for i in ips_record.response_full:
            print(i)

        soa_record = dns_query.soa_lookup(domain)
        for i in soa_record.response_full:
            print("\n".join(i.split(". ")))
