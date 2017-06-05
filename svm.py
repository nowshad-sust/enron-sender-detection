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

print('data processing . . .');

# vectorize the training data
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)


from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

print('training started');

# feed training data into svm
from sklearn.linear_model import SGDClassifier
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