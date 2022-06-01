from sys import exit
from full_scripts import ip_address
from full_scripts import geo
from full_scripts import whois_add
from full_scripts import site_nslookup
from full_scripts import dns_resolver
from full_scripts import reversed_dns
from full_scripts import robots
from full_scripts import sitemap
from full_scripts import reverse_ip


def print_start_help():
    print("\033[32m" + r'''
      ___  ____ ___ _   _ _____   ____   _____  __
     / _ \/ ___|_ _| \ | |_   _| | __ ) / _ \ \/ /
    | | | \___ \| ||  \| | | |   |  _ \| | | \  / 
    | |_| |___) | || |\  | | |   | |_) | |_| /  \ 
     \___/|____/___|_| \_| |_|   |____/ \___/_/\_\
    ''')
    print('''
        0. Exit the program
        1. Host IP
        2. Site location
        3. Whois
        4. Nslookup
        5. DNS MX-Record
        6. Reverse DNS
        7. robots.txt
        8. sitemap.xml
        9. Reverse IP lookup
    ''' + "\033[0m")


if __name__ == '__main__':
    print_start_help()
    dict_method = {1: ip_address.run, 2: geo.get_site_location, 3: whois_add.get_info, 4: site_nslookup.run_nslookup,
                   5: dns_resolver.get_MX_record, 6: reversed_dns.reverse_dns, 7: robots.show_robots_content,
                   8: sitemap.get_sitemap, 9: reverse_ip.run_ip_reversed_lookup}
    while True:
        try:
            num = int(input("\nEnter the option number: "))
        except KeyboardInterrupt:
            print("Program was stopped by user.")
            exit(0)
        if num == 0:
            print('The program is complete')
            exit(0)
        elif 0 < num < 10:
            print('-' * 70, sep="\n")
            dict_method[num]()
            print('-' * 70, sep="\n")
        else:
            print("Incorrect number was entered! Please use digit between 0 - 8")
