from random import random
from interface import FeatureExtractor

class MockFeatureExtractor(FeatureExtractor):

    def getFeaturesByImageId(self, imageId):
        return [random() for x in range(3)]

