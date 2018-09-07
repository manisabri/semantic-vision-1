import sys
import logging
import torch
import torch.nn.functional as F

from util import *
from interface import MultiDnn 

sys.path.insert(0, currentDir(__file__) + '/../DNNs/vqa_multi_dnn')
from netsvocabulary import NetsVocab


class NetsVocabularyNeuralNetworkRunner(MultiDnn):
    
    def __init__(self, modelsFileName):
        self.logger = logging.getLogger('NetsVocabularyNeuralNetworkRunner')
        self.netsVocabulary = self.loadNets(modelsFileName)

    def loadNets(self, modelsFileName):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        checkpoint = torch.load(modelsFileName, map_location=device.type)
        netsVocabulary = NetsVocab.fromStateDict(device, checkpoint['state_dict'])
        netsVocabulary.train(False)
        return netsVocabulary


