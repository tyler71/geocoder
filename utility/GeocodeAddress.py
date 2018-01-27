import random

# https://pypi.python.org/pypi/geopy
from geopy.geocoders import GoogleV3, Nominatim, OpenCage
from geopy.exc import GeocoderTimedOut, GeocoderQuotaExceeded


class GeocodeAddress:
    """
    Takes address and returns class with lat long coordinates
    """

    def __init__(self, address):
        self.address = address

        self.decoded_address = None
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.raw = None
        self.api_keys = None

        self.geocoders = [
                          self.googlev3_decode,
                          self.nominatim_decode,
                          self.opencage_decode,
                         ]
        random.shuffle(self.geocoders)

    def int(self, api_keys):
        self.api_keys = api_keys

        for geocoder in self.geocoders:
            try:
                geocoder()
                return self
            except (LookupError, GeocoderTimedOut, GeocoderQuotaExceeded):
                pass
        else:
            raise LookupError

    def geosetter(self, geolocator):
        decoded_service = geolocator.geocode(self.address)

        if decoded_service:
            self.decoded_address = decoded_service.address
            self.latitude = decoded_service.latitude
            self.longitude = decoded_service.longitude
            self.altitude = decoded_service.altitude
            self.raw = decoded_service.raw
        else:
            raise LookupError

    def googlev3_decode(self):
        api_key = self.api_keys.get('GoogleV3', None)
        if api_key:
            geolocator_service = GoogleV3(api_key)
        else:
            geolocator_service = GoogleV3()
        self.geosetter(geolocator_service)

    def nominatim_decode(self):
        geolocator_service = Nominatim()
        self.geosetter(geolocator_service)

    def opencage_decode(self):
        api_key = self.api_keys.get('OpenCage', None)
        if api_key:
            geolocator_service = OpenCage(api_key=api_key)
            self.geosetter(geolocator_service)
        else:
            raise LookupError
