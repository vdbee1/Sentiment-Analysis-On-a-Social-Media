from textblob import TextBlob
# Implementing TextBlob for sentiment analysis

class sentimfunc:
    # using textblob api to return polarity of the sentiment
    def sentimentP(text):
        try:
            return TextBlob(text).sentiment.polarity
        except:
            return "You are bad at Coding "
    #using textblob api to return subjectivity clause for a given message
    def sentimentS(text):
        try:
            return TextBlob(text).sentiment.subjectivity
        except:
            return "You are bad at Coding "
