# Source Codes for German Sentiment Analysis with Pretrained Models

The `directory tree` of this project is as follows.

```
./german_sentiment_pre_trained_models/
│
├── credentials/
|   └── ambient-hulling-323011-28ed4a8f68a6.json
|
├── dataset/
│   └── ge_test_data.xlsx
│
├── predictions/
|
├── AWSSentiment.py
├── DataManipulation.py
├── german_sentiment_analysis.ipynb
├── GoogleSentiment.py
├── google_t5_sentiment.py
├── IBMSentiment.py
├── microsoft_sentiment.py
├── ModelValidation.py
└── README.md
```

## About each python file

*  `AWSSentiment.py` : Includes required credential and codes to post request to Amazon Sentiment Analysis's API.
*   `DataManipulation.py` : Loads the dataset and modifies it if required.
*   `german_sentiment_analysis.ipynb` : This is the main file to run the project.
*   `GoogleSentiment.py` : Includes codes to post request to Google Sentiment Analysis's API
*   `google_t5_sentiment.py` : Uses Google T5 pretrained model for sentiment analysis'.
*   `IBMSentiment.py` : Includes required credential and codes to post request to IBMWatson Sentiment Analysis's API.
*   `microsoft_sentiment.py` : Includes required credential and codes to post request to Microsoft Sentiment Analysis's API.
*   `ModelValidation.py` : Includes some functions to evaluate the model's performance and visualize the confusion matrix.


## Run the project

To run the project you only need to run the notebook: `german_sentiment_analysis.ipynb`

## Reference
Some of the base codes come from this repo:
https://github.com/ianovski/customer-review-sentiment
