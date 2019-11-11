#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from estimator import *
from sklearn.metrics import accuracy_score
from sklearn.metrics import make_scorer
from sklearn.metrics import matthews_corrcoef
from sklearn.model_selection import cross_validate
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import matthews_corrcoef as MCC
from sklearn.metrics import cohen_kappa_score


def check_fitted(clf): 
    return hasattr(clf, "classes_")


def sensitivity(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    sensitivity = tp / (tp+fn)
    return sensitivity

def specificity(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    specificity = tn / (tn+fp)
    return specificity

scoring = {'rocauc': make_scorer(roc_auc_score),
           'accuracy': make_scorer(accuracy_score),
           'sensitivity': make_scorer(sensitivity), 
           'specificity': make_scorer(specificity),
           'mcc': make_scorer(MCC),
           'kappa': make_scorer(cohen_kappa_score)}

def print_results(cv_results, classifier):
    print(classifier)
    print('Sensitivity: ', "%.2f" % cv_results['test_sensitivity'].mean())
    print('Specificity: ', "%.2f" % cv_results['test_specificity'].mean())
    print('Accuracy: ', "%.2f" % cv_results['test_accuracy'].mean())  
    print('MCC: ', "%.2f" % cv_results['test_mcc'].mean())
    print('ROC: ', "%.2f" % cv_results['test_rocauc'].mean())  
    print('Cohen\'s Kappa: ', "%.2f" % cv_results['test_kappa'].mean())


def generate_results(clf, features, labels, fold_size=5):
    cv_results = cross_validate(clf.fit(features, labels), features, labels, scoring=scoring, cv=fold_size)
    print_results(cv_results, clf)

def print_results_test(y_true, y_pred, y_scores, classifier):
    print(classifier)
    print('Sensitivity: ', "%.2f" % sensitivity(y_true, y_pred))
    print('Specificity: ', "%.2f" % specificity(y_true, y_pred))
    print('Accuracy: ', "%.2f" % accuracy_score(y_true, y_pred))  
    print('MCC: ', "%.2f" % MCC(y_true, y_pred))
    print('ROC: ', "%.2f" % roc_auc_score(y_true, y_scores))
    print('Cohen\'s Kappa: ', "%.2f" % cohen_kappa_score(y_true, y_pred))


def evaluate_models_cv(clf1, clf2, clf3, clf4, clf5, X_train, Y_train):
    generate_results(clf1, X_train, Y_train)
    generate_results(clf2, X_train, Y_train)
    generate_results(clf3, X_train, Y_train)
    generate_results(clf4, X_train, Y_train)
    generate_results(clf5, X_train, Y_train)

def evaluate_models_test(clf1, X_valid, Y_valid):

    Y_valid_scores = clf1.predict_proba(X_valid)[:, 1]
    Y_valid_pred = clf1.predict(X_valid)
    print_results_test(Y_valid, Y_valid_pred, Y_valid_scores, clf1)


def hyper_parameter_tuning(X_train, Y_train, csvname):
    models1 = models1 = { 
        'SVC': SVC()
    }
    params1 = {
        'SVC': [
            {'kernel': ['linear'], 'C': [1,2,3,4,5,6,7,8,9,10]},
            {'kernel': ['rbf'], 'C': [1,2,3,4,5,10], 'gamma': [1,0.5,0.01,0.001, 0.0001]}
        ]
    }
    helper1 = EstimatorSelectionHelper(models1, params1)
    helper1.fit(X_train, Y_train, cv=5, scoring='roc_auc', n_jobs=-1)
    helper1.score_summary(sort_by='mean_score').to_csv(csvname, sep=',')


#random_or_not = 'rand_'
def preprocessing(xt='c', rand=''):
    neg_train_c5 = pd.read_csv('../features/bp/' + xt + 't/neg_train_' + rand +  xt + '5', header=None, names = list(range(5*20+1)))
    neg_train_c10 = pd.read_csv('../features/bp/' + xt + 't/neg_train_' + rand +  xt + '10', header=None, names = list(range(10*20+1)))
    neg_train_c15 = pd.read_csv('../features/bp/' + xt + 't/neg_train_' + rand +  xt + '15', header=None, names = list(range(15*20+1)))

    neg_valid_c5 = pd.read_csv('../features/bp/' + xt + 't/neg_valid_' + rand +  xt + '5', header=None, names = list(range(5*20+1)))
    neg_valid_c10 = pd.read_csv('../features/bp/' + xt + 't/neg_valid_' + rand +  xt + '10', header=None, names = list(range(10*20+1)))
    neg_valid_c15 = pd.read_csv('../features/bp/' + xt + 't/neg_valid_' + rand +  xt + '15', header=None, names = list(range(15*20+1)))

    pos_train_c5 = pd.read_csv('../features/bp/' + xt + 't/pos_train_' + xt + '5', header=None, names = list(range(5*20+1)))
    pos_train_c10 = pd.read_csv('../features/bp/' + xt + 't/pos_train_' + xt + '10', header=None, names = list(range(10*20+1)))
    pos_train_c15 = pd.read_csv('../features/bp/' + xt + 't/pos_train_' + xt + '15', header=None, names = list(range(15*20+1)))

    pos_valid_c5 = pd.read_csv('../features/bp/' + xt + 't/pos_valid_' + xt + '5', header=None, names = list(range(5*20+1)))
    pos_valid_c10 = pd.read_csv('../features/bp/' + xt + 't/pos_valid_' + xt + '10', header=None, names = list(range(10*20+1)))
    pos_valid_c15 = pd.read_csv('../features/bp/' + xt + 't/pos_valid_' + xt + '15', header=None, names = list(range(15*20+1)))
    
    
    neg_train_c5.drop(neg_train_c5.columns[len(neg_train_c5.columns)-1], axis=1, inplace=True)
    neg_train_c10.drop(neg_train_c10.columns[len(neg_train_c10.columns)-1], axis=1, inplace=True)
    neg_train_c15.drop(neg_train_c15.columns[len(neg_train_c15.columns)-1], axis=1, inplace=True)


    neg_valid_c5.drop(neg_valid_c5.columns[len(neg_valid_c5.columns)-1], axis=1, inplace=True)
    neg_valid_c10.drop(neg_valid_c10.columns[len(neg_valid_c10.columns)-1], axis=1, inplace=True)
    neg_valid_c15.drop(neg_valid_c15.columns[len(neg_valid_c15.columns)-1], axis=1, inplace=True)

    pos_train_c5.drop(pos_train_c5.columns[len(pos_train_c5.columns)-1], axis=1, inplace=True)
    pos_train_c10.drop(pos_train_c10.columns[len(pos_train_c10.columns)-1], axis=1, inplace=True)
    pos_train_c15.drop(pos_train_c15.columns[len(pos_train_c15.columns)-1], axis=1, inplace=True)

    pos_valid_c5.drop(pos_valid_c5.columns[len(pos_valid_c5.columns)-1], axis=1, inplace=True)
    pos_valid_c10.drop(pos_valid_c10.columns[len(pos_valid_c10.columns)-1], axis=1, inplace=True)
    pos_valid_c15.drop(pos_valid_c15.columns[len(pos_valid_c15.columns)-1], axis=1, inplace=True)
    
    neg_train_c5.dropna(inplace=True)
    neg_train_c10.dropna(inplace=True)
    neg_train_c15.dropna(inplace=True)

    neg_valid_c5.dropna(inplace=True)
    neg_valid_c10.dropna(inplace=True)
    neg_valid_c15.dropna(inplace=True)

    pos_train_c5.dropna(inplace=True)
    pos_train_c10.dropna(inplace=True)
    pos_train_c15.dropna(inplace=True)

    pos_valid_c5.dropna(inplace=True)
    pos_valid_c10.dropna(inplace=True)
    pos_valid_c15.dropna(inplace=True)
    
    
    neg_train_c5.reset_index(drop=True, inplace=True)
    neg_train_c10.reset_index(drop=True, inplace=True)
    neg_train_c15.reset_index(drop=True, inplace=True)


    neg_valid_c5.reset_index(drop=True, inplace=True)
    neg_valid_c10.reset_index(drop=True, inplace=True)
    neg_valid_c15.reset_index(drop=True, inplace=True)

    pos_train_c5.reset_index(drop=True, inplace=True)
    pos_train_c10.reset_index(drop=True, inplace=True)
    pos_train_c15.reset_index(drop=True, inplace=True)

    pos_valid_c5.reset_index(drop=True, inplace=True)
    pos_valid_c10.reset_index(drop=True, inplace=True)
    pos_valid_c15.reset_index(drop=True, inplace=True)
    
    
    neg_train_c5['flag'] = 0
    neg_train_c10['flag'] = 0
    neg_train_c15['flag'] = 0


    neg_valid_c5['flag'] = 0
    neg_valid_c10['flag'] = 0
    neg_valid_c15['flag'] = 0

    pos_train_c5['flag'] = 1
    pos_train_c10['flag'] = 1
    pos_train_c15['flag'] = 1

    pos_valid_c5['flag'] = 1
    pos_valid_c10['flag'] = 1
    pos_valid_c15['flag'] = 1
    
    
    train_c5 = pd.concat([pos_train_c5, neg_train_c5])
    train_c5 = train_c5.sample(frac=1).reset_index(drop=True)
    X_c5 = train_c5.drop(train_c5.columns[len(train_c5.columns)-1], axis=1)
    Y_c5 = train_c5['flag']

    train_c10 = pd.concat([pos_train_c10, neg_train_c10])
    train_c10 = train_c10.sample(frac=1).reset_index(drop=True)
    X_c10 = train_c10.drop(train_c10.columns[len(train_c10.columns)-1], axis=1)
    Y_c10 = train_c10['flag']

    train_c15 = pd.concat([pos_train_c15, neg_train_c15])
    train_c15 = train_c15.sample(frac=1).reset_index(drop=True)
    X_c15 = train_c15.drop(train_c15.columns[len(train_c15.columns)-1], axis=1)
    Y_c15 = train_c15['flag']
    

    valid_c5 = pd.concat([pos_valid_c5, neg_valid_c5])
    valid_c5 = valid_c5.sample(frac=1).reset_index(drop=True)
    Xval_c5 = valid_c5.drop(valid_c5.columns[len(valid_c5.columns)-1], axis=1)
    Yval_c5 = valid_c5['flag']

    valid_c10 = pd.concat([pos_valid_c10, neg_valid_c10])
    valid_c10 = valid_c10.sample(frac=1).reset_index(drop=True)
    Xval_c10 = valid_c10.drop(valid_c10.columns[len(valid_c10.columns)-1], axis=1)
    Yval_c10 = valid_c10['flag']

    valid_c15 = pd.concat([pos_valid_c15, neg_valid_c15])
    valid_c15 = valid_c15.sample(frac=1).reset_index(drop=True)
    Xval_c15 = valid_c15.drop(valid_c15.columns[len(valid_c15.columns)-1], axis=1)
    Yval_c15 = valid_c15['flag']
    
    return X_c5, Y_c5, X_c10, Y_c10, X_c15, Y_c15, Xval_c5, Yval_c5, Xval_c10, Yval_c10, Xval_c15, Yval_c15


X_c5, Y_c5, X_c10, Y_c10, X_c15, Y_c15, Xval_c5, Yval_c5, Xval_c10, Yval_c10, Xval_c15, Yval_c15 = preprocessing()


X_n5, Y_n5, X_n10, Y_n10, X_n15, Y_n15, Xval_n5, Yval_n5, Xval_n10, Yval_n10, Xval_n15, Yval_n15 = preprocessing(xt='n')





hyper_parameter_tuning(X_c5, Y_c5, "c5.csv")
hyper_parameter_tuning(X_c10, Y_c10, "c10.csv")
hyper_parameter_tuning(X_c15, Y_c15, "c15.csv")


hyper_parameter_tuning(X_n5, Y_n5, "n5.csv")
hyper_parameter_tuning(X_n10, Y_n10, "n10.csv")
hyper_parameter_tuning(X_n15, Y_n15, "n15.csv")





clf1 = SVC(C=1, gamma=0.5, kernel='rbf', probability=True)
clf2 = SVC(C=10, gamma=0.01, kernel='rbf', probability=True)
clf3 = SVC(C=10, gamma=0.01, kernel='rbf', probability=True)
clf4 = SVC(C=1, gamma=0.5, kernel='rbf', probability=True)
clf5 = SVC(C=1, gamma=0.5, kernel='rbf', probability=True)
clf6 = SVC(C=1, gamma=0.01, kernel='rbf', probability=True)


generate_results(clf1, X_n5, Y_n5)
generate_results(clf2, X_n10, Y_n10)
generate_results(clf3, X_n15, Y_n15)
generate_results(clf4, X_c5, Y_c5)
generate_results(clf5, X_c10, Y_c10)
generate_results(clf6, X_c15, Y_c15)


clf1.fit(X_n5, Y_n5)
clf2.fit(X_n10, Y_n10)
clf3.fit(X_n15, Y_n15)
clf4.fit(X_c5, Y_c5)
clf5.fit(X_c10, Y_c10)
clf6.fit(X_c15, Y_c15)


evaluate_models_test(clf1, Xval_n5, Yval_n5)
evaluate_models_test(clf2, Xval_n10, Yval_n10)
evaluate_models_test(clf3, Xval_n15, Yval_n15)
evaluate_models_test(clf4, Xval_c5, Yval_c5)
evaluate_models_test(clf5, Xval_c10, Yval_c10)
evaluate_models_test(clf6, Xval_c15, Yval_c15)





#random_or_not = 'rand_'
def preprocessing2(xt='c', rand=''):
    neg_train_c5 = pd.read_csv('../features/bp/' + xt + 't/neg_train_' + rand +  xt + '5', header=None, names = list(range(5*20+1)))
    neg_train_c10 = pd.read_csv('../features/bp/' + xt + 't/neg_train_' + rand +  xt + '10', header=None, names = list(range(10*20+1)))
    neg_train_c15 = pd.read_csv('../features/bp/' + xt + 't/neg_train_' + rand +  xt + '15', header=None, names = list(range(15*20+1)))

    neg_valid_c5 = pd.read_csv('../features/bp/' + xt + 't/neg_valid_' + rand +  xt + '5', header=None, names = list(range(5*20+1)))
    neg_valid_c10 = pd.read_csv('../features/bp/' + xt + 't/neg_valid_' + rand +  xt + '10', header=None, names = list(range(10*20+1)))
    neg_valid_c15 = pd.read_csv('../features/bp/' + xt + 't/neg_valid_' + rand +  xt + '15', header=None, names = list(range(15*20+1)))

    pos_train_c5 = pd.read_csv('../features/bp/' + xt + 't/pos_train_' + xt + '5', header=None, names = list(range(5*20+1)))
    pos_train_c10 = pd.read_csv('../features/bp/' + xt + 't/pos_train_' + xt + '10', header=None, names = list(range(10*20+1)))
    pos_train_c15 = pd.read_csv('../features/bp/' + xt + 't/pos_train_' + xt + '15', header=None, names = list(range(15*20+1)))

    pos_valid_c5 = pd.read_csv('../features/bp/' + xt + 't/pos_valid_' + xt + '5', header=None, names = list(range(5*20+1)))
    pos_valid_c10 = pd.read_csv('../features/bp/' + xt + 't/pos_valid_' + xt + '10', header=None, names = list(range(10*20+1)))
    pos_valid_c15 = pd.read_csv('../features/bp/' + xt + 't/pos_valid_' + xt + '15', header=None, names = list(range(15*20+1)))
    
    
    neg_train_c5.drop(neg_train_c5.columns[len(neg_train_c5.columns)-1], axis=1, inplace=True)
    neg_train_c10.drop(neg_train_c10.columns[len(neg_train_c10.columns)-1], axis=1, inplace=True)
    neg_train_c15.drop(neg_train_c15.columns[len(neg_train_c15.columns)-1], axis=1, inplace=True)


    neg_valid_c5.drop(neg_valid_c5.columns[len(neg_valid_c5.columns)-1], axis=1, inplace=True)
    neg_valid_c10.drop(neg_valid_c10.columns[len(neg_valid_c10.columns)-1], axis=1, inplace=True)
    neg_valid_c15.drop(neg_valid_c15.columns[len(neg_valid_c15.columns)-1], axis=1, inplace=True)

    pos_train_c5.drop(pos_train_c5.columns[len(pos_train_c5.columns)-1], axis=1, inplace=True)
    pos_train_c10.drop(pos_train_c10.columns[len(pos_train_c10.columns)-1], axis=1, inplace=True)
    pos_train_c15.drop(pos_train_c15.columns[len(pos_train_c15.columns)-1], axis=1, inplace=True)

    pos_valid_c5.drop(pos_valid_c5.columns[len(pos_valid_c5.columns)-1], axis=1, inplace=True)
    pos_valid_c10.drop(pos_valid_c10.columns[len(pos_valid_c10.columns)-1], axis=1, inplace=True)
    pos_valid_c15.drop(pos_valid_c15.columns[len(pos_valid_c15.columns)-1], axis=1, inplace=True)
    
    
    return neg_train_c5, neg_train_c10, neg_train_c15, neg_valid_c5, neg_valid_c10, neg_valid_c15, pos_train_c5, pos_train_c10, pos_train_c15, pos_valid_c5, pos_valid_c10, pos_valid_c15


def preprocessing3(neg_train_c5, neg_train_c10, neg_train_c15, neg_valid_c5, neg_valid_c10, neg_valid_c15, pos_train_c5, pos_train_c10, pos_train_c15, pos_valid_c5, pos_valid_c10, pos_valid_c15):
       
    neg_train_c5.dropna(inplace=True)
    neg_train_c10.dropna(inplace=True)
    neg_train_c15.dropna(inplace=True)

    neg_valid_c5.dropna(inplace=True)
    neg_valid_c10.dropna(inplace=True)
    neg_valid_c15.dropna(inplace=True)

    pos_train_c5.dropna(inplace=True)
    pos_train_c10.dropna(inplace=True)
    pos_train_c15.dropna(inplace=True)

    pos_valid_c5.dropna(inplace=True)
    pos_valid_c10.dropna(inplace=True)
    pos_valid_c15.dropna(inplace=True)
    
    
    neg_train_c5.reset_index(drop=True, inplace=True)
    neg_train_c10.reset_index(drop=True, inplace=True)
    neg_train_c15.reset_index(drop=True, inplace=True)


    neg_valid_c5.reset_index(drop=True, inplace=True)
    neg_valid_c10.reset_index(drop=True, inplace=True)
    neg_valid_c15.reset_index(drop=True, inplace=True)

    pos_train_c5.reset_index(drop=True, inplace=True)
    pos_train_c10.reset_index(drop=True, inplace=True)
    pos_train_c15.reset_index(drop=True, inplace=True)

    pos_valid_c5.reset_index(drop=True, inplace=True)
    pos_valid_c10.reset_index(drop=True, inplace=True)
    pos_valid_c15.reset_index(drop=True, inplace=True)
    
    
    neg_train_c5['flag'] = 0
    neg_train_c10['flag'] = 0
    neg_train_c15['flag'] = 0


    neg_valid_c5['flag'] = 0
    neg_valid_c10['flag'] = 0
    neg_valid_c15['flag'] = 0

    pos_train_c5['flag'] = 1
    pos_train_c10['flag'] = 1
    pos_train_c15['flag'] = 1

    pos_valid_c5['flag'] = 1
    pos_valid_c10['flag'] = 1
    pos_valid_c15['flag'] = 1
    
    
    train_c5 = pd.concat([pos_train_c5, neg_train_c5])
    train_c5 = train_c5.sample(frac=1).reset_index(drop=True)
    X_c5 = train_c5.drop(train_c5.columns[len(train_c5.columns)-1], axis=1)
    Y_c5 = train_c5['flag']

    train_c10 = pd.concat([pos_train_c10, neg_train_c10])
    train_c10 = train_c10.sample(frac=1).reset_index(drop=True)
    X_c10 = train_c10.drop(train_c10.columns[len(train_c10.columns)-1], axis=1)
    Y_c10 = train_c10['flag']

    train_c15 = pd.concat([pos_train_c15, neg_train_c15])
    train_c15 = train_c15.sample(frac=1).reset_index(drop=True)
    X_c15 = train_c15.drop(train_c15.columns[len(train_c15.columns)-1], axis=1)
    Y_c15 = train_c15['flag']
    

    valid_c5 = pd.concat([pos_valid_c5, neg_valid_c5])
    valid_c5 = valid_c5.sample(frac=1).reset_index(drop=True)
    Xval_c5 = valid_c5.drop(valid_c5.columns[len(valid_c5.columns)-1], axis=1)
    Yval_c5 = valid_c5['flag']

    valid_c10 = pd.concat([pos_valid_c10, neg_valid_c10])
    valid_c10 = valid_c10.sample(frac=1).reset_index(drop=True)
    Xval_c10 = valid_c10.drop(valid_c10.columns[len(valid_c10.columns)-1], axis=1)
    Yval_c10 = valid_c10['flag']

    valid_c15 = pd.concat([pos_valid_c15, neg_valid_c15])
    valid_c15 = valid_c15.sample(frac=1).reset_index(drop=True)
    Xval_c15 = valid_c15.drop(valid_c15.columns[len(valid_c15.columns)-1], axis=1)
    Yval_c15 = valid_c15['flag']
    
    return X_c5, Y_c5, X_c10, Y_c10, X_c15, Y_c15, Xval_c5, Yval_c5, Xval_c10, Yval_c10, Xval_c15, Yval_c15


neg_train_c5, neg_train_c10, neg_train_c15, neg_valid_c5, neg_valid_c10, neg_valid_c15, pos_train_c5, pos_train_c10, pos_train_c15, pos_valid_c5, pos_valid_c10, pos_valid_c15 = preprocessing2()


neg_train_n5, neg_train_n10, neg_train_n15, neg_valid_n5, neg_valid_n10, neg_valid_n15, pos_train_n5, pos_train_n10, pos_train_n15, pos_valid_n5, pos_valid_n10, pos_valid_n15 = preprocessing2(xt='n')


neg_train_c5 = pd.concat([neg_train_n5, neg_train_c5], axis=1)
neg_train_c10 = pd.concat([neg_train_n10, neg_train_c10], axis=1)
neg_train_c15 = pd.concat([neg_train_n15, neg_train_c15], axis=1)
neg_valid_c5 = pd.concat([neg_valid_n5, neg_valid_c5], axis=1)
neg_valid_c10 = pd.concat([neg_valid_n10, neg_valid_c10], axis=1)
neg_valid_c15 = pd.concat([neg_valid_n15, neg_valid_c15], axis=1)
pos_train_c5 = pd.concat([pos_train_n5, pos_train_c5], axis=1)
pos_train_c10 = pd.concat([pos_train_n10, pos_train_c10], axis=1)
pos_train_c15 = pd.concat([pos_train_n15, pos_train_c15], axis=1)
pos_valid_c5 = pd.concat([pos_valid_n5, pos_valid_c5], axis=1)
pos_valid_c10 = pd.concat([pos_valid_n10, pos_valid_c10], axis=1)
pos_valid_c15 = pd.concat([pos_valid_n15, pos_valid_c15], axis=1)


X_c5, Y_c5, X_c10, Y_c10, X_c15, Y_c15, Xval_c5, Yval_c5, Xval_c10, Yval_c10, Xval_c15, Yval_c15 = preprocessing3(neg_train_c5, neg_train_c10, neg_train_c15, neg_valid_c5, neg_valid_c10, neg_valid_c15, pos_train_c5, pos_train_c10, pos_train_c15, pos_valid_c5, pos_valid_c10, pos_valid_c15)


hyper_parameter_tuning(X_c5, Y_c5, "nc5.csv")
hyper_parameter_tuning(X_c10, Y_c10, "nc10.csv")
hyper_parameter_tuning(X_c15, Y_c15, "nc15.csv")


clf1 = SVC(C=10, gamma=0.01, kernel='rbf', probability=True)
clf2 = SVC(C=2, gamma=0.01, kernel='rbf', probability=True)
clf3 = SVC(C=2, gamma=0.01, kernel='rbf', probability=True)


generate_results(clf1, X_c5, Y_c5)
generate_results(clf2, X_c10, Y_c10)
generate_results(clf3, X_c15, Y_c15)


clf1.fit(X_c5, Y_c5)
clf2.fit(X_c10, Y_c10)
clf3.fit(X_c15, Y_c15)


evaluate_models_test(clf1, Xval_c5, Yval_c5)
evaluate_models_test(clf2, Xval_c10, Yval_c10)
evaluate_models_test(clf3, Xval_c15, Yval_c15)




