########## Link of the code is http://www.davidsbatista.net/blog/2018/02/23/model_optimization/ #############

import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.feature_selection import RFE
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.extmath import density
from sklearn import metrics
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neural_network import MLPClassifier

class EstimatorSelectionHelper:
    def __init__(self, models, params):
        if not set(models.keys()).issubset(set(params.keys())):
            missing_params = list(set(models.keys()) - set(params.keys()))
            raise ValueError("Some estimators are missing parameters: %s" % missing_params)
        self.models = models
        self.params = params
        self.keys = models.keys()
        self.grid_searches = {}
    
    def fit(self, X, y, cv=5, n_jobs=1, verbose=1, scoring=None, refit=False):
        for key in self.keys:
            print("Running GridSearchCV for %s." % key)
            model = self.models[key]
            params = self.params[key]
            gs = GridSearchCV(model, params, cv=cv, n_jobs=n_jobs,
                              verbose=verbose, scoring=scoring, refit=refit,
                              return_train_score=True)
            gs.fit(X,y)
            self.grid_searches[key] = gs


    def score_summary(self, sort_by='mean_score'):
        def row(key, scores, params):
            d = {
                 'estimator': key,
                 'min_score': min(scores),
                 'max_score': max(scores),
                 'mean_score': np.mean(scores),
                 'std_score': np.std(scores),
            }
            return pd.Series({**params,**d})

        rows = []
        for k in self.grid_searches:
            print(k)
            params = self.grid_searches[k].cv_results_['params']
            scores = []
            for i in range(self.grid_searches[k].cv):
                key = "split{}_test_score".format(i)
                r = self.grid_searches[k].cv_results_[key]        
                scores.append(r.reshape(len(params),1))

            all_scores = np.hstack(scores)
            for p, s in zip(params,all_scores):
                rows.append((row(k, s, p)))

        df = pd.concat(rows, axis=1).T.sort_values([sort_by], ascending=False)

        columns = ['estimator', 'min_score', 'mean_score', 'max_score', 'std_score']
        columns = columns + [c for c in df.columns if c not in columns]

        return df[columns]

from sklearn.ensemble import (ExtraTreesClassifier, RandomForestClassifier, 
                              AdaBoostClassifier, GradientBoostingClassifier)
from sklearn.svm import SVC

models1 = { 
    'SVC': SVC(),
    'RandomForestClassifier': RandomForestClassifier(),
    'knn': KNeighborsClassifier(),
    'ExtraTreesClassifier': ExtraTreesClassifier(),
    'mlp': MLPClassifier()
}

params1 = {
    'ExtraTreesClassifier': { 'n_estimators': [10, 20, 40, 50, 100, 500], 'max_features': ['auto', 'sqrt', 'log2'], 'max_depth' : [4,5,6,7,8], 'criterion' :['gini', 'entropy'] },
    'RandomForestClassifier': { 'n_estimators': [50, 100, 200, 500], 'max_features': ['auto', 'sqrt', 'log2'], 'max_depth' : [4,5,6,7,8], 'criterion' :['gini', 'entropy']},
    'SVC': [
        {'kernel': ['linear'], 'C': [1,2,3,4,5,6,7,8,9,10]},
        {'kernel': ['rbf'], 'C': [1,2,3,4,5,10], 'gamma': [1,0.5,0.01,0.001, 0.0001]}
    ],
    'Ridge Classifier' : {'alpha' : [1,0.1,0.01,0.001,0.0001,0]},
    'mlp' : {'solver': ['lbfgs'], 'max_iter': [1000,1500,2000 ], 'alpha': 10.0 ** -np.arange(1, 10, 3), 'hidden_layer_sizes':np.arange(10, 16, 3), 'random_state':[0,1,3,9]},
    'knn' : {'n_neighbors':[5,6,7,8,9,10],'weights':['uniform', 'distance'],'algorithm':['auto', 'ball_tree','kd_tree','brute']}
}
