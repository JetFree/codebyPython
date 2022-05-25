import exifread
from os import path, listdir
import datetime


def findPhotoWithData(mypath, month, year):
    for file in [path.join(mypath, f) for f in listdir(mypath) if path.isfile(path.join(mypath, f))]:
        if tags := verifyPhotoData(file, month, year):
            return tags


def verifyPhotoData(file, month, year):
    f = open(file, 'rb')
    tags = exifread.process_file(f)
    date_obj = datetime.datetime.strptime(str(tags["Image DateTime"]), "%Y:%m:%d %H:%M:%S")
    if date_obj.month == month and date_obj.year == year:
        return tags


def print_tags(tags):
    for tag in tags.keys():
        if tag not in ("JPEGThumbnail", "TIFFThumbnail", "Filename", "EXIF MakerNote"):
            print(f"{tag} {tags[tag]}")


if __name__ == '__main__':
    folder_path = "./photo"
    results = findPhotoWithData(folder_path, 9, 2019)
    print_tags(results)
