from PIL import Image
import piexif


def get_exif_meta_data(filepath):
  
    return piexif.load(filepath)

def remove_metadata(filepath):
    image = Image.open(filepath)
    image_data = list(image.getdata())
    image_without_exif = Image.new(image.mode,image.size)
    image_without_exif.putdata(image_data)
    
    return image_without_exif

def get_gps(filepath):
    exif_data = get_exif_meta_data(filepath)
    gps_info = exif_data.get("GPS")

    if not isinstance(gps_info, dict):
        return None, None

    if 2 not in gps_info or 4 not in gps_info:
        return None, None

    lat = dms_to_decimal(gps_info[2], gps_info[1].decode())
    lon = dms_to_decimal(gps_info[4], gps_info[3].decode())
    return lat, lon

def dms_to_decimal(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1]
    seconds = dms[2][0] / dms[2][1]
    decimal = degrees + minutes / 60 + seconds / 3600
    if ref in ['S', 'W']:
        decimal *= -1
    return decimal