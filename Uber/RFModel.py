# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:18:37 2017

@author: zhang_000
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
from FeatureEngineering import FeatureEngineering
from operator import itemgetter
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc

rawDataFile = './ds_challenge_v2_1_data (1) (1).csv' 
FE = FeatureEngineering(rawDataFile)
rawData = FE.loadRawData()
features = FE.generateFeatures()
labels = FE.generateLabels()

#test function
def performTest(X_test, Y_test, classifier):
    predictions = classifier.predict(X_test)
    FA = 0
    Accu = 0
    MD = 0
    Y_test = list(Y_test.as_matrix())
    for i in range(len(predictions)):
        if Y_test[i] == predictions[i]:
            Accu += 1
        elif Y_test[i] and not predictions[i]:
            MD += 1
        else:
            FA += 1

    print ('Accuracy: %f' % (float(Accu)/len(Y_test)))
    print ('False Alarm Rate: %f' % (float(FA)/Y_test.count(False)))
    print ('Miss of Detection: %f' % (float(MD)/Y_test.count(True)))   

    return ([Accu, FA, MD])   

def generateROC(preds, Y):
    #generate ROC curve 
    fpr, tpr, thresholds =roc_curve(Y, preds)
    roc_auc = auc(fpr, tpr)
    print("Area under the ROC curve : %f" % roc_auc)
    
    i = np.arange(len(tpr)) # index for df
    roc = pd.DataFrame({'fpr' : pd.Series(fpr, index=i),'tpr' : pd.Series(tpr, index = i), 'fpr' : pd.Series(fpr, index = i), 'tf' : pd.Series(tpr - (1-fpr), index = i), 'thresholds' : pd.Series(thresholds, index = i)})
    roc.ix[(roc.tf-0).abs().argsort()[:1]]

    # Plot tpr vs fpr
    lw = 2
    fig, ax = plt.subplots()
    plt.plot(roc['fpr'],roc['tpr'], color = 'red')
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    ax.set_xticklabels([])
    
#use random forest 
X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=0.33, random_state=42)
cvScores = []
# some simple grid search for hyper-parameters
for n_estimators in range(10, 101, 10):
    clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=None, min_samples_split=2, random_state=0)
    scores = cross_val_score(clf, X_train, Y_train)
    cvScores.append([n_estimators, scores.mean()])
    print ('n_estimators: %d with scores %f' % (n_estimators, scores.mean()))
                             
#use the best model with highest cv scores
n_estimators = sorted(cvScores, key = itemgetter(1), reverse = True)[0][0]
clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=None, min_samples_split=2, random_state=0)
clf = clf.fit(X_train, Y_train)
importances = clf.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

plt.figure()
plt.title("Feature importances")
plt.bar(range(X_train.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X_train.shape[1]), indices)
plt.xlim([-1, X_train.shape[1]])
plt.show()

# test on testing data
[Accu, FA, MD] =  performTest(X_train, Y_train, clf)
preds = clf.predict_proba(X_test)[:,1]
generateROC(preds, Y_test)

# use logistic regression
LR = LogisticRegression(penalty='l1')
print ('CV Score: %f' % (cross_val_score(LR, X_train, Y_train).mean()))
Y_score = LR.fit(X_train, Y_train)
[Accu, FA, MD] =  performTest(X_train, Y_train, LR)
preds = LR.predict_proba(X_test)[:,1]
generateROC(preds, Y_test)
#weight adjustment on LR
LR_balanced = LogisticRegression(penalty='l1', class_weight="balanced")
print ('CV Score: %f' % (cross_val_score(LR_balanced, X_train, Y_train).mean()))
LR_balanced.fit(X_train, Y_train)
[Accu, FA, MD] =  performTest(X_train, Y_train, LR_balanced)
preds = LR_balanced.predict_proba(X_test)[:,1]
generateROC(preds, Y_test)


    

