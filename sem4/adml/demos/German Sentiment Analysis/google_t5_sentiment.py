# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:21:34 2021

@author: Reza
"""


import pandas as pd

from transformers import AutoTokenizer, AutoModelWithLMHead


class GoogleT5Sentiment:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-imdb-sentiment")
        self.model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-imdb-sentiment")
    
    def _get_sentiment(self, sentence):
      input_ids = self.tokenizer.encode(sentence + '</s>', return_tensors='pt')
      output = self.model.generate(input_ids=input_ids, max_length=2)
      dec = [self.tokenizer.decode(ids) for ids in output]
      label = dec[0]

      return label.split(' ')[1]
  
    def run_sentiment(self, data):
        """ Run Google T5 Sentiment analysis"""
        review_ids =  data['review_id']
        sentences = data['sentence']
        true_sentiments = data['sentiment']
        
        review_id_list = []
        true_sentimen_list = []
        predicted_sentiment_list = []
        count = 0
        for review_id, sentence, true_sentiment in zip(review_ids, sentences, true_sentiments):
          sentiment = self._get_sentiment(sentence)
          if sentiment:
                review_id_list.append(review_id)
                true_sentimen_list.append(true_sentiment)
                predicted_sentiment_list.append(sentiment)
                count+=1
                if(count%100==0):
                    print("Google T5 analyzing review #", count)
            
        return self._save_results(review_id_list, true_sentimen_list, predicted_sentiment_list)

  
    def _save_results(self, review_id_list, true_sentimen_list, predicted_sentiment_list):
        """Save sentiments and IDs to CSV"""
        output = pd.DataFrame(data={"review_id":review_id_list, "true_sentiment": true_sentimen_list, "predicted_sentiment":predicted_sentiment_list})
        output.to_csv("predictions/googlet5_sentiment.csv", index=False, quoting=3, escapechar='\\')
        return output
