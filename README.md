# enron-sender-detection
A simple machine learning approach to detect the sender based on the mail body of the famous Enron Datasset

# prerequisites
* python
* anaconda
* scikit learn
* other dependencies

# How to run
1. clone this repository - `git clone https://github.com/nowshad-sust/enron-sender-detection.git`
2. download enron dataset from here - https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tgz
3. now extract this dataset(maildir) to the project(clonned) folder
4. open a terminal or cmd in the project directory
5. run the `copy_sent_mails.py` script by the command - `python copy_sent_mails.py`
  This should make a directory named remail in the project folder and copy all the sent mails from the original dataset directory.
6. Now, run the `naive_bayes_pipeline.py` by the command - `python naive_bayes_pipeline.py`
  This should give you a number which refers to the validation sucess rate.
  
# Latest Statistics (accuracy)
  * Naive Bayes classifier ~ 0.46
  * SVM ~ 0.79
  * SVM with grid search ~ 0.85

