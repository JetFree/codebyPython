import pygeoip


def get_site_location():
    print("2. Site location\n")
    ip = input("Enter ip: ")
    if ip:
        gi = pygeoip.GeoIP("GeoIPCity.dat")
        try:
            city = gi.region_by_addr(ip)
            for key in city:
                if city[key] is None or city[key] == 0:
                    continue
                else:
                    print(key, city[key], sep=": ")
        except OSError as e:
            print(e)