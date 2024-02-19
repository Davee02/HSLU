# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:57:11 2021

@author: Reza
"""

import pandas as pd
from textblob_de import TextBlobDE


class TextBlobDESentiment(): 

    def __init__(self):
        pass

    def get_sentiment(self, sentence):
        """Run TextBlobDE and get sentiment for given sentence"""
        polarity = TextBlobDE(sentence).sentiment.polarity
        return(polarity)

    def run_sentiment(self, data):
        """ Run TextBlobDE Sentiment analysis"""
        review_ids =  data['review_id']
        sentences = data['sentence']
        true_sentiments = data['sentiment']
        
        review_id_list = []
        true_sentimen_list = []
        predicted_sentiment_list = []
        count = 0
        for review_id, sentence, true_sentiment in zip(review_ids, sentences, true_sentiments):
            sentiment_ = self.get_sentiment(sentence)
            sentiment = 'negative' if sentiment_ == -1 else 'positive'
            if sentiment:
                review_id_list.append(review_id)
                true_sentimen_list.append(true_sentiment)
                predicted_sentiment_list.append(sentiment)
                count+=1
                if(count%100==0):
                    print("TextBlobDE analyzing review #", count)

        return self._save_results(review_id_list, true_sentimen_list, predicted_sentiment_list)
    
    def _save_results(self, review_id_list, true_sentimen_list, predicted_sentiment_list):
        """Save sentiments and IDs to CSV"""
        output = pd.DataFrame(data={"review_id":review_id_list, "true_sentiment": true_sentimen_list, "predicted_sentiment":predicted_sentiment_list})
        output.to_csv("predictions/textblob_de_sentiment.csv", index=False, quoting=3, escapechar='\\')
        return output
