import matplotlib.pyplot as plt
# Data visualization using matplotlib

class datavil:
    def dataVisualization(pos, neg, neu):
        temp = [pos, neg, neu]
        tempNames = ['Positive Sentiment', 'Negative Sentiment', 'Neutral Sentiment']
        plt.pie(temp, labels=tempNames, startangle=90, shadow=True, autopct='%.1f%%')
        plt.title('Sentiment Analysis')
        plt.show()