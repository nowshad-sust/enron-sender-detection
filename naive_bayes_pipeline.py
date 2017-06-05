import sklearn.datasets
import logging

# load all data from files
twenty_all = sklearn.datasets.load_files("./remail", 
categories=None, load_content=True, shuffle=True, encoding="latin1", random_state=42, decode_error='strict')

print('dataset loaded');

print('data processing . . .');
# split the train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(twenty_all.data, twenty_all.target, test_size=0.2)


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

print('training started');

# feed the train dataset into naive_bayes model
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
])
text_clf = text_clf.fit(X_train, y_train)

print('training finished');

print('testing trained model');

# validation of the trained model
import numpy as np
docs_test = X_test
predicted = text_clf.predict(docs_test)

print('Test Result:');
print(np.mean(predicted == y_test))
