from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import glob
import os


"""
def get_exif(image_file_path):
    exif_table = {}
    image = Image.open(image_file_path)
    print(image)
    info = image.getexif()
    print(info)
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value
    gps_info = {}

    print(exif_table)
    for key in exif_table['GPSInfo'].keys():
        decode = GPSTAGS.get(key,key)
        gps_info[decode] = exif_table['GPSInfo'][key]
    return gps_info
"""


def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_decimal_from_dms(dms, ref):
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
    return (lat,lon)





if __name__ == "__main__":
    for root, dirs, files in os.walk("/../../Volumes/VOLUME/"):
        for file in files:
            if file.endswith(".jpg"):
                exif = get_exif(os.path.join(root, file))
                try:
                    geotags = get_geotagging(exif)
                    print(get_coordinates(geotags))
                except ValueError:
                    pass