
# <p align = "center"> You've Got Mail </p>

![](Images/spam_header.webp)

## Overview

This collaborative project was created to assist the user in identifying which emails or texts messages they receive are spam or ham (normal). Spam emails and text messages were gathered from various datasets. Machine learning was utilized to produce these results; multiple models were pre-processed, trained, and tested to uncover the model wtih the most accuracy. 

## Analysis

Data was collected from multiple data sets to identify which messages were labeled as spam or ham. The data was then pre-processed, filtered, and trained using multiple machine learning models. Furthermore, word-count and frequency of specific words within a message were analyzed to determine if these factors had an effect on determining if the message was spam or ham, based on a UCI machine learning benchmark database named spambase where 57 features have already been extracted for each email message and all instances were labelled as “0” (normal) or “1” (spam).

A typical scenario for machine learning is to create a learning system by training it on a given training data set. Later on the system will be applied to different test data sets. Various machine learning models were used to uncover the most useful model. 

### Machine Learning Models

<h5>Logistic Regression Model (Email Spam Detection)</h5> 
<h6>Using supervised machine learning, this model attempts to distinguish between spam or ham based on class values. <h6>

![](Images/logisitc_regression_model_results.png)

<h5> Random Forest Classifier (Email Spam Detection)</h5>
<h6>This model determined predictive accuracy by averaging descision tree classifiers from the entire dataset <h6>

![](Images/rfm_model_results.png)
![](Images/random_forest_stefanie.png)

<h5>Sequential Model /#1 (Email Spam Detection)<h5>
<h6>This sequential model used two hidden layers, trained using 50 epochs, and had a total of 701 parameters. <h6>

![](Images/sequential_1.png)

<h5>Sequential Model #2 (Email Spam Detection)</h5>
<h6>This sequential model used two hidden layers, trained using 50 epochs, and had a total of 1,601 parameters. <h6>

![](Images/sequential_2.png)

<h5>Sequential Model #3 (Email Spam Detection)</h5>
<h6>This sequential model used scikit_learn's countVectorizer transform a list of messages to trainable features. It used 3 hidden layers, trained using 50 epochs, and had a total of 280,401 parameters. <h6>

![](Images/nn_model_hannah.png)

<h5>Naive Bayes</h5>
<h6>This model used the Bayes Theorem and tokenization to classify email/text as spam or not. <h6>

![](Images/naive_bayes_model_stefanie.png)
![](Images/naive_bayes_model_rilee.png)



## Datasets

Email Spam Detection: https://www.kaggle.com/code/mfaisalqureshi/email-spam-detection-98-accuracy/data

Email Spam Classification: https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv

SMS Spam Collection Dataset: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Tools Used

-Jupyter Notebook 
-Google Colab
-PySpark
-Bootstrap
-Flask



## Video Demo Link
https://drive.google.com/file/d/1lo1i5d1dmkiiIV972Ad7Mh3Y5PgqjOOH/view?usp=share_link



![](Images/undefined%20-%20Imgur.gif)

