from abc import ABC

class NeuralNetworkRunner(ABC):
    
    def runNeuralNetwork(self, features, word):
        pass

class AnswerHandler(ABC):
    
    def onNewQuestion(self, record):
        pass
    
    def onAnswer(self, record, answer):
        pass
    

class ChainAnswerHandler(AnswerHandler):
    
    def __init__(self, answerHandlerList):
        self.answerHandlerList = answerHandlerList
        
    def onNewQuestion(self, record):
        self.notifyAll(lambda handler: handler.onNewQuestion(record))

    def onAnswer(self, record, answer):
        self.notifyAll(lambda handler: handler.onAnswer(record, answer))
        
    def notifyAll(self, methodToCall):
        map(methodToCall, answerHandlerList)

class FeatureExtractor(ABC):
    
    def getFeaturesByImageId(self, imageId):
        pass


class MultiDnn(NeuralNetworkRunner):

    def runNeuralNetwork(self, features, word):
        model = self.netsVocabulary.getModelByWord(word)
        if model is None:
            self.logger.debug('no model found, return FALSE')
            return torch.zeros(1)
        # TODO: F.sigmoid should part of NN
        return F.sigmoid(model(torch.Tensor(features)))

