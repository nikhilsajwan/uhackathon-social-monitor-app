# Modified for Social-Monomania Project Usage under public usage
from textblob import TextBlob
def analysis(twitterReturn):
    Tweets = twitterReturn.get('statuses')
    neg = 0.0
    pos = 0.0
    neg_count = 0
    neutral_count = 0
    pos_count = 0
    ss=[]
    for entry in Tweets:
        #Testing:
        #print entry.get('text').encode('utf8')
        blob = TextBlob(entry.get('text'))
        #Negative Count
        ss.append(blob.sentiment.polarity)
        if blob.sentiment.polarity < 0:
            neg += blob.sentiment.polarity
            neg_count += 1
        #Neutral Count
        elif blob.sentiment.polarity == 0:
            neutral_count += 1
        #Positive Count
        else:
            pos += blob.sentiment.polarity
            pos_count += 1  
    return [['Sentiment', 'no. of tweets'],['Positive',pos_count]
            ,['Neutral',neutral_count],['Negative',neg_count],ss]