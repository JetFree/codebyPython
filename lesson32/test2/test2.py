import exifread
from geopy.geocoders import Nominatim


def getTagsFromPhoto(file):
    f = open(file, 'rb')
    return exifread.process_file(f)


def getGPSlocation(lat, long):
    geolocator = Nominatim(user_agent="Codeby task EXIF")
    return geolocator.reverse((str(lat), str(long)), language="ru").address


def convertGPSData(latitude, directionLa, longitude, directionLo):
    r_latitude = latitude[0] + (latitude[1] / 60) + ((latitude[2].num / latitude[2].denominator) / 3600)
    r_longitude = longitude[0] + (longitude[1] / 60) + ((longitude[2].num / longitude[2].denominator) / 3600)
    if directionLa == "S" or directionLa == "W":
        r_latitude = r_latitude * -1
    if directionLo == "S" or directionLo == "W":
        r_longitude = r_longitude * -1
    return r_latitude, r_longitude


if __name__ == '__main__':
    photo_path = "./photo/swan.jpg"
    tags = getTagsFromPhoto(photo_path)
    f_latitude, f_longitude = convertGPSData(tags["GPS GPSLatitude"].values, tags["GPS GPSLatitudeRef"].values,
                                             tags["GPS GPSLongitude"].values, tags["GPS GPSLongitudeRef"].values)
    print(f"{f_latitude}\n{f_longitude}")
    print(getGPSlocation(f_latitude, f_longitude))
