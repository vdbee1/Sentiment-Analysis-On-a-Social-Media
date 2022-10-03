# Used to classsify the postive,neutral and the negetive messages
class classck:
    def ClassCheck(df):
        negative = 0;
        positive = 0;
        neutral = 0;
        for index in range(len(df)):
            if index < len(df.index) - 1:  # the index starts from 0 so that is the reason for the -1
                if df.loc[index, 'sentiment'] < 0:
                    df.loc[index, 'Category'] = "Negetive"
                    negative += 1
                elif df.loc[index, 'sentiment'] > 0:
                    df.loc[index, 'Category'] = "Positive"
                    positive += 1
                elif df.loc[index,'sentiment'] == 0:
                    df.loc[index, "Category"] = 'Neutral'
                    neutral+=1
                else:
                    pass
        return positive, negative, neutral