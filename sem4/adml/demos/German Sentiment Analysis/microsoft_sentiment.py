# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:21:34 2021

@author: Reza
"""

key = "KEY_HERE"
endpoint = "https://gesent.cognitiveservices.azure.com/"

import time
import pandas as pd
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

class MicrosoftSentiment:
    def __init__(self):
        self.client = self._authenticate_client() 

    def _authenticate_client(self):
        ta_credential = AzureKeyCredential(key)
        text_analytics_client = TextAnalyticsClient(
                endpoint=endpoint, 
                credential=ta_credential)
        return text_analytics_client
    
    def sentiment_analysis(self, data):
        """Run MSFT Azure Sentiment analysis model"""
        review_ids =  data['review_id']
        sentences = data['sentence']
        true_sentiments = data['sentiment']
        
        review_id_list = []
        true_sentimen_list = []
        predicted_sentiment_list = []
        count = 0
        for review_id, sentence, true_sentiment in zip(review_ids, sentences, true_sentiments):
            response = self.client.analyze_sentiment(documents=[sentence])[0]
            if response:
                review_id_list.append(review_id)
                true_sentimen_list.append(true_sentiment)
                predicted_sentiment_list.append(response.sentiment)
                count+=1
                if(count%100==0):
                    print("Microsoft analyzing review #", count)
                    print("Pausing Microsoft API requests for 1 minute.....") # API requests limited to 600/minute
                    time.sleep(65)
        
        return self._save_results(review_id_list, true_sentimen_list, predicted_sentiment_list)
    
    def _save_results(self, review_id_list, true_sentimen_list, predicted_sentiment_list):
        """Save sentiments and IDs to CSV"""
        output = pd.DataFrame(data={"review_id":review_id_list, "true_sentiment": true_sentimen_list, "predicted_sentiment":predicted_sentiment_list})
        output.to_csv("predictions/microsoft_sentiment.csv", index=False, quoting=3, escapechar='\\')
        return output
    
    

