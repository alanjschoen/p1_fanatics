from geopy.geocoders import Nominatim 
geolocator = Nominatim()

def getZip(lon, lat):
    location = geolocator.reverse("%f, %f"%(lat, lon))
    print location.raw
    try:
        return int(location.raw["address"]["postcode"])
    except:
        print "Could not find zipcode"
        return -1

lon = -74.014028
lat = 40.787143
print getZip(lon, lat)


