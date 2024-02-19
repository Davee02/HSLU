import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials/ambient-hulling-323011-28ed4a8f68a6.json"

import time
import pandas as pd

# from googleapiclient import discovery
# import google.cloud
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


#%%
class GoogleSentiment:

    """Instantiates a Google client. Replace with proper init statement"""
    def __init__(self):
      self.client = language.LanguageServiceClient()
  
    def parse_text(self,text):
      """Convert sentence to document"""
      document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
      return document

    def get_sentiment(self, client, document):
        """Run Google API and get sentiment for given sentence"""
        negative_threshold = -0.33
        neutral_threshold = 0.33
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        sentiment_classification = "negative" if sentiment.score<=negative_threshold \
                      else "neutral" if sentiment.score<=neutral_threshold \
                      else "positive"
        return sentiment_classification

    def run_sentiment(self, data):
        """Run Google Sentiment analysis"""
        review_ids =  data['review_id']
        sentences = data['sentence']
        true_sentiments = data['sentiment']
        
        review_id_list = []
        true_sentimen_list = []
        predicted_sentiment_list = []
        count = 0
        for review_id, sentence, true_sentiment in zip(review_ids, sentences, true_sentiments):
          sentiment = self.get_sentiment(self.client, self.parse_text(sentence))
          if sentiment:
                review_id_list.append(review_id)
                true_sentimen_list.append(true_sentiment)
                predicted_sentiment_list.append(sentiment)
                count+=1
                if(count%100==0):
                    print("Test set index = ", count, "......")
                if(count%598==0):
                    print("Pausing Google API requests for 1 minute.....") # API requests limited to 600/minute
                    time.sleep(65)
        return self._save_results(review_id_list, true_sentimen_list, predicted_sentiment_list)
    
    def _save_results(self, review_id_list, true_sentimen_list, predicted_sentiment_list):
        """Save sentiments and IDs to CSV"""
        output = pd.DataFrame(data={"review_id":review_id_list, "true_sentiment": true_sentimen_list, "predicted_sentiment":predicted_sentiment_list})
        output.to_csv("predictions/google_sentiment.csv", index=False, quoting=3, escapechar='\\')
        return output
