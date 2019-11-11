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


def gen_training_matrix(pos_train, neg_train):
    pos_train = pos_train.drop(['Unnamed: 20'], axis=1)
    neg_train = neg_train.drop(['Unnamed: 20'], axis=1)
    pos_train['flag'] = 1
    neg_train['flag'] = 0
    train = pd.concat([pos_train, neg_train])
    train = train.sample(frac=1).reset_index(drop=True)
    X = train[train.columns[:20]]
    Y = train['flag']
    return X, Y


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

def evaluate_models_test(clf1, clf2, clf3, clf4, clf5, X_valid, Y_valid):

    Y_valid_scores = clf1.predict_proba(X_valid)[:, 1]
    Y_valid_pred = clf1.predict(X_valid)
    print_results_test(Y_valid, Y_valid_pred, Y_valid_scores, clf1)

    Y_valid_scores = clf2.predict_proba(X_valid)[:, 1]
    Y_valid_pred = clf2.predict(X_valid)
    print_results_test(Y_valid, Y_valid_pred, Y_valid_scores, clf2)

    Y_valid_scores = clf3.predict_proba(X_valid)[:, 1]
    Y_valid_pred = clf3.predict(X_valid)
    print_results_test(Y_valid, Y_valid_pred, Y_valid_scores, clf3)

    Y_valid_scores = clf4.predict_proba(X_valid)[:, 1]
    Y_valid_pred = clf4.predict(X_valid)
    print_results_test(Y_valid, Y_valid_pred, Y_valid_scores, clf4)

    Y_valid_scores = clf5.predict_proba(X_valid)[:, 1]
    Y_valid_pred = clf5.predict(X_valid)
    print_results_test(Y_valid, Y_valid_pred, Y_valid_scores, clf5)


def hyper_parameter_tuning(X_train, Y_train, csvname):
    helper1 = EstimatorSelectionHelper(models1, params1)
    helper1.fit(X_train, Y_train, cv=5, scoring='roc_auc', n_jobs=-1)
    helper1.score_summary(sort_by='mean_score').to_csv(csvname, sep=',')


_pos_train = pd.read_csv('../features/aac/pos_train')
_neg_train = pd.read_csv('../features/aac/neg_train')


X_train, Y_train = gen_training_matrix(_pos_train, _neg_train)





#Takes a lot of time. Comment out to perform it again. 
#You will have to manually read the csv files and change the hyperparameters of the classifiers (clf1, ..., clf6) manually.
#For now the clfx's have the best parameters. So there is no need to perform this again
hyper_parameter_tuning(X_train, Y_train, "parameters.csv")





clf1 = SVC(C=5, gamma=0.001, kernel='rbf', probability=True)
clf2 = RandomForestClassifier(criterion='entropy', max_depth=8, max_features='sqrt', n_estimators=500)
clf3 = KNeighborsClassifier(algorithm='kd_tree', n_neighbors=10, weights='uniform')
clf4 = ExtraTreesClassifier(criterion='gini', max_depth=8, max_features='log2', n_estimators=500)
clf5 = MLPClassifier(alpha=1.00E-7, hidden_layer_sizes=13, max_iter=1000, random_state=1, solver='lbfgs')


# # EVALUATE MODELS - CV




evaluate_models_cv(clf1, clf2, clf3, clf4, clf5, X_train, Y_train)


# # Validation results

_pos_valid = pd.read_csv('../features/aac/pos_valid')
_neg_valid = pd.read_csv('../features/aac/neg_valid')


X_valid, Y_valid = gen_training_matrix(_pos_valid, _neg_valid)


clf1.fit(X_train, Y_train)
clf2.fit(X_train, Y_train)
clf3.fit(X_train, Y_train)
clf4.fit(X_train, Y_train)
clf5.fit(X_train, Y_train)


evaluate_models_test(clf1, clf2, clf3, clf4, clf5, X_valid, Y_valid)





X_train = None
Y_train = None
X_valid = None
Y_valid = None


_pos_train_rand = pd.read_csv('../features/aac/pos_train')
_neg_train_rand = pd.read_csv('../features/aac/neg_train_rand')


X_train_rand, Y_train_rand = gen_training_matrix(_pos_train_rand, _neg_train_rand)


hyper_parameter_tuning(X_train_rand, Y_train_rand, "parameters_rand.csv")


clf1 = SVC(C=4, gamma=0.01, kernel='rbf', probability=True)
clf2 = RandomForestClassifier(criterion='gini', max_depth=8, max_features='auto', n_estimators=100)
clf3 = KNeighborsClassifier(algorithm='ball_tree', n_neighbors=10, weights='distance')
clf4 = ExtraTreesClassifier(criterion='gini', max_depth=8, max_features='log2', n_estimators=500)
clf5 = MLPClassifier(alpha=0.1, hidden_layer_sizes=13, max_iter=1500, random_state=1, solver='lbfgs')


evaluate_models_cv(clf1, clf2, clf3, clf4, clf5, X_train_rand, Y_train_rand)





_pos_valid_rand = pd.read_csv('../features/aac/pos_valid')
_neg_valid_rand = pd.read_csv('../features/aac/neg_valid_rand')


X_valid_rand, Y_valid_rand = gen_training_matrix(_pos_valid_rand, _neg_valid_rand)


clf1.fit(X_train_rand, Y_train_rand)
clf2.fit(X_train_rand, Y_train_rand)
clf3.fit(X_train_rand, Y_train_rand)
clf4.fit(X_train_rand, Y_train_rand)
clf5.fit(X_train_rand, Y_train_rand)


evaluate_models_test(clf1, clf2, clf3, clf4, clf5, X_valid_rand, Y_valid_rand)




