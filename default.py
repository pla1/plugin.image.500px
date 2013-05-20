
import utils
import utils.xbmc

import xbmcgui
import xbmcplugin

from fivehundredpx.client import FiveHundredPXAPI

_CONSUMER_KEY = 'LvUFQHMQgSlaWe3aRQot6Ct5ZC2pdTMyTLS0GMfF'
_RPP = int(xbmcplugin.getSetting(utils.xbmc.addon_handle, 'quantity'))
API = FiveHundredPXAPI()


class Image(object):
    def __init__(self, photo_json):
        self.name= photo_json['name']
        self.thumb_url = photo_json['images'][0]['url']
        self.url = photo_json['images'][1]['url']

    def __repr__(self):
        return str(self.__dict__)


def feature():
    def get_images(feature):
        resp = API.photos(feature=feature, rpp=_RPP, consumer_key=_CONSUMER_KEY, image_size=[2, 4])
        return map(Image, resp['photos'])

    feature = utils.xbmc.get_addon_params()['feature']
    for image in get_images(feature):
        utils.xbmc.add_image(image)
    utils.xbmc.end_of_directory()


def root():
    features = (
        "editors",
        "popular",
        "upcoming",
        "fresh_today",
        "fresh_yesterday"
    )

    for feature in features:
        url = utils.xbmc.encode_child_url('feature', feature=feature)
        utils.xbmc.add_dir(feature, url)
    utils.xbmc.end_of_directory()


try:
    modes = {
        'feature': feature
    }

    params = utils.xbmc.get_addon_params()
    mode_name = params['mode']
    modes[mode_name]()
except KeyError:
    root()





