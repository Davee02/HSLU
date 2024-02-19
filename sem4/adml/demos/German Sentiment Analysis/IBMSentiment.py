from __future__ import print_function
import json
import requests
import pandas as pd
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#%%
class IBMSentiment():
    def __init__(self): 

        apikey = 'O0sdAtsVCZReN-8lcaBoYg2jSowaP7HqRRG-Kk24dChR'
        authenticator = IAMAuthenticator(apikey)

        self.service = NaturalLanguageUnderstandingV1(version="2021-08-01", authenticator=authenticator) 
        
        url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/f9f822ef-f6a7-4edd-8908-f3ab7fd03cf8" 
        self.service.set_service_url(url)
        
    def get_sentiment(self, service,sentence):
        """Run IBM API and get sentiment for given sentence"""
        try:
            response = service.analyze(
                text=sentence, 
                features=Features(sentiment=SentimentOptions())).get_result()
        except Exception as e:
            print(e.message)
            return "neutral" # If unable to categorize, set sentiment to "Neutral"
        return response['sentiment']['document']['label']


    def run_sentiment(self, data):
        """ Run IBM Sentiment analysis"""
        review_ids =  data['review_id']
        sentences = data['sentence']
        true_sentiments = data['sentiment']
        
        review_id_list = []
        true_sentimen_list = []
        predicted_sentiment_list = []
        count = 0
        for review_id, sentence, true_sentiment in zip(review_ids, sentences, true_sentiments):
            sentiment = self.get_sentiment(self.service, sentence)
            if sentiment:
                review_id_list.append(review_id)
                true_sentimen_list.append(true_sentiment)
                predicted_sentiment_list.append(sentiment)
                count+=1
                if(count%100==0):
                    print("IBM Watson analyzing review #", count)
                
        return self._save_results(review_id_list, true_sentimen_list, predicted_sentiment_list)

    def _save_results(self, review_id_list, true_sentimen_list, predicted_sentiment_list):
        """Save sentiments and IDs to CSV"""
        output = pd.DataFrame(data={"review_id":review_id_list, "true_sentiment": true_sentimen_list, "predicted_sentiment":predicted_sentiment_list})
        output.to_csv("predictions/ibmwatson_sentiment.csv", index=False, quoting=3, escapechar='\\')
        return output
