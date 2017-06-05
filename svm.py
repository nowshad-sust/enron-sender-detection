import sklearn.datasets
import logging

print('Loading dataset ...');

# load all data from files
twenty_all = sklearn.datasets.load_files("./remail", 
categories=None, load_content=True, shuffle=True, encoding="latin1", random_state=42, decode_error='strict')

print('dataset loaded');

# split the train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(twenty_all.data, twenty_all.target, test_size=0.2)


# vectorize the training data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier

print('training started');

# feed training data into svm

from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, n_iter=5, random_state=42)),
])
_ = text_clf.fit(X_train, y_train)

print('Training complete');

print('Testing trained model');

# validation of the trained model
import numpy as np
docs_test = X_test
predicted = text_clf.predict(docs_test)

print('Test Result:');
print(np.mean(predicted == y_test))