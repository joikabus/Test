from abc import ABC ,  abstractmethod

class Label:
    SPAM = 'SPAM'
    NEGATIVE_TEXT = 'NEGATIVE_TEXT'
    TOO_LONG = 'TOO_LONG'
    OK = 'OK'

class TextAnalyzer(ABC):
    @abstractmethod
    def processText(self):
        pass

class KeywordsAnalyzer(ABC):

    @abstractmethod
    def getKeyword(self):
        pass
     
    @abstractmethod
    def getLabel(self , text):
        pass
    

class NegativeTextAnalyzer(KeywordsAnalyzer , TextAnalyzer):  
    _keywords = ["=(" , ":|" , "8="]  
    def getLabel(self , text):
        for item in self._keywords:
            if item in text:
                return Label.NEGATIVE_TEXT
            else:
                return Label.OK
              
    def getKeyword(self):
        return self._keywords
    
    def processText(self , text):
        return self.getLabel(text)
    

class SpamAnalyzer(KeywordsAnalyzer , TextAnalyzer):
    _keywords = ["пас" , "бас" , "кас"]  
    def getLabel(self , text):
        for item in self._keywords:
            if item in text:
                return Label.SPAM
            else:
                return Label.OK
            
    def getKeyword(self):
        return self._keywords
    
    def processText(self , text):
        return self.getLabel(text)
        
class TooLongTextAnalyzer(TextAnalyzer):
    _maxLength = 4
    def processText(self , text):
        if len(text) > self._maxLength:
            return Label.TOO_LONG
        else:
            return Label.OK
        
   
def checkLabel():
    array = [NegativeTextAnalyzer()  , SpamAnalyzer()  , TooLongTextAnalyzer()]
    message = "=( пас"
    for item in array:
        getterItem = item.processText(message)
        print(getterItem)

checkLabel()
        

    





