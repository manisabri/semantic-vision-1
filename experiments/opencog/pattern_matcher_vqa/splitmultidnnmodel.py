import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import glob
import re

from interface import MultiDnn


class SplitMultidnnModel(MultiDnn):

    def __init__(self, models_directory):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.networks = self.load_models(os.path.join(models_directory, 'networks'),
                                         model_prefix='best_loss_model_',
                                         device=device)

    def create_networks(all_words, device):
        nets = dict()
        for k in all_words:
            model = nn.Sequential(
            nn.Linear(2048, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
            ).to(device)
            nets[k] = model        
        return nets
    
    def get_parameters(nets):
        rez = []
        for k in nets:
            rez += nets[k].parameters()
        return rez
    
    def set_all_train(nets, is_train):
        for k in nets:
            nets[k].train(is_train)
    
    
    def load_models(path_to_models, prefix, device):    
        list_of_files = glob.glob(path_to_models + "/" + prefix + "_*.pth")
        list_of_words = []
        for f in list_of_files:
            rez = int(re.findall("_(\d+)\.pth", f)[0])
            list_of_words.append(rez)
        
        nets =  create_networks(list_of_words, device)
        
        for f,w in zip(list_of_files, list_of_words):
            nets[w].load_state_dict(torch.load(f))
        
        return nets

