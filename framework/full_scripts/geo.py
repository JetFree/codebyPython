import pygeoip
import os


def get_site_location():
    print("2. Site location\n")
    if ip := input("Enter ip: "):
        if os.path.exists("./full_scripts/GeoIPCity.dat"):
            gi = pygeoip.GeoIP("./full_scripts/GeoIPCity.dat")
            try:
                city = gi.region_by_addr(ip)
                for key in city:
                    if city[key] is None or city[key] == 0:
                        continue
                    else:
                        print(key, city[key], sep=": ")
            except OSError as e:
                print(e)
        else:
            print("File GeoIPCity.data was not found")