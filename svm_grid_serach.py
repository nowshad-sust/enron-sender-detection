import sklearn.datasets
from pprint import pprint
from time import time
import logging

print('Loading dataset ...');

# load all data from files
twenty_all = sklearn.datasets.load_files("./remail", 
categories=None, load_content=True, shuffle=False, encoding="latin1", random_state=42, decode_error='strict')

print('dataset loaded');

# split the train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(twenty_all.data, twenty_all.target, test_size=0.1)

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
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier()),
])

# uncommenting more parameters will give better exploring power but will
# increase processing time in a combinatorial way
parameters = {
    'vect__max_df': (0.5, 0.75, 1.0),
    #'vect__max_features': (None, 5000, 10000, 50000),
    'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
    #'tfidf__use_idf': (True, False),
    #'tfidf__norm': ('l1', 'l2'),
    'clf__alpha': (0.00001, 0.000001),
    'clf__penalty': ('l2', 'elasticnet'),
    #'clf__n_iter': (10, 50, 80),
}

from sklearn.model_selection import GridSearchCV

if __name__ == "__main__":
    # multiprocessing requires the fork to happen in a __main__ protected
    # block

    # find the best parameters for both the feature extraction and the
    # classifier
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1)

    print("Performing grid search...")
    t0 = time()
    grid_clf = grid_search.fit(X_train, y_train)
    print("done in %0.3fs" % (time() - t0))

print('Training complete');

print('Testing trained model');

# validation of the trained model
import numpy as np
predicted = grid_clf.predict(X_test)

print('Test Result:');
print(np.mean(predicted == y_test))