import boto3
import pandas as pd
import time

access_key_id = 'AKIAWIF546PGGO5ZAMTF'
secret_access_key = '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'

class AWSSentiment(): 

    def __init__(self):
        self.client = boto3.client('comprehend',
		region_name="us-east-2",
		aws_access_key_id = access_key_id,
		aws_secret_access_key = secret_access_key)

    def get_sentiment(self,client,document):
        """Run AWS API and get sentiment for given sentence"""
        response = client.detect_sentiment(
			Text=document,
			LanguageCode='de'
		)
        sentiment = response["Sentiment"]
        sentiment = sentiment.lower()
        if(sentiment=="mixed"):
            sentiment="neutral"
        return(sentiment)

    def run_sentiment(self, data):
        """ Run AWS Sentiment analysis"""
        review_ids =  data['review_id']
        sentences = data['sentence']
        true_sentiments = data['sentiment']
        
        review_id_list = []
        true_sentimen_list = []
        predicted_sentiment_list = []
        count = 0
        for review_id, sentence, true_sentiment in zip(review_ids, sentences, true_sentiments):
            sentiment = self.get_sentiment(self.client, sentence)
            if sentiment:
                review_id_list.append(review_id)
                true_sentimen_list.append(true_sentiment)
                predicted_sentiment_list.append(sentiment)
                count+=1
                if(count%100==0):
                    print("AWS analyzing review #", count)
                    time.sleep(1)
        return self._save_results(review_id_list, true_sentimen_list, predicted_sentiment_list)
    
    def _save_results(self, review_id_list, true_sentimen_list, predicted_sentiment_list):
        """Save sentiments and IDs to CSV"""
        output = pd.DataFrame(data={"review_id":review_id_list, "true_sentiment": true_sentimen_list, "predicted_sentiment":predicted_sentiment_list})
        output.to_csv("predictions/amazon_sentiment.csv", index=False, quoting=3, escapechar='\\')
        return output
