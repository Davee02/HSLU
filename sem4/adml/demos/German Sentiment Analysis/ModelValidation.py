from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score, balanced_accuracy_score
import matplotlib.pyplot as plt
import numpy as np


class ModelValidation:

  def plot_confusion_matrix(self,y_true, y_pred, classes,
                           normalize=False,
                           title=None,
                           cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    # classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    plt.show()
    return ax

  def plot_result_comparison(self, y_true, y_pred, classes, title):
    barWidth = 0.25
    y_true_count = y_true.value_counts()
    y_pred_count = y_pred.value_counts()
    r1 = np.arange(len(classes))
    r2 = [x + barWidth for x in r1]
    # Make the plot
    plt.bar(r1,y_true_count,width=barWidth,edgecolor='white',label='True')
    plt.bar(r2,y_pred_count,width=barWidth,edgecolor='white',label='Predicted')
    y_true_count = y_true.value_counts()
    
    plt.xlabel('Sentiment Labels')
    plt.ylabel('Label Count')
    plt.title(title)
    plt.xticks([r + barWidth for r in range(len(classes))], classes)
    # Create legend & Show graphic
    plt.legend()
    # plt.savefig('figures/result_comparison.png')
    plt.show()
    
  def evaluate(self, true_sentiment, predicted_sentiment, title=None):
    predicted_sentiment = predicted_sentiment.replace({'neutral': 'positive'})
    predicted_sentiment = predicted_sentiment.replace({'mixed': 'positive'})
    classes = ["negative", "positive", "neutral"]
    title_ = f'{title} Sentiment Confusion Matrix'
    self.plot_confusion_matrix(true_sentiment, predicted_sentiment, 
                               classes=classes, title=title_)
    self.plot_confusion_matrix(true_sentiment, predicted_sentiment, 
                               classes=classes, normalize=True, title=title_)
    
    # # Printing classification report and accuracy score of the model
    print(f"{title} Classification report:\n ", classification_report(true_sentiment, predicted_sentiment))  
    
    true_sentiment = true_sentiment.replace({'neutral': 2})
    true_sentiment = true_sentiment.replace({'positive': 1})
    true_sentiment = true_sentiment.replace({'negative': 0})
    predicted_sentiment = predicted_sentiment.replace({'neutral': 2})
    predicted_sentiment = predicted_sentiment.replace({'positive': 1})
    predicted_sentiment = predicted_sentiment.replace({'negative': 0})
    
    print(f"{title} Accuracy: ", np.round(accuracy_score(true_sentiment, predicted_sentiment), 2) )
    print(f"{title} Balanced Accuracy Score: ", np.round(balanced_accuracy_score(true_sentiment, predicted_sentiment), 2) )
    print(f"{title} F1-Score: ", np.round(f1_score(true_sentiment, predicted_sentiment, average='macro'), 2) )
