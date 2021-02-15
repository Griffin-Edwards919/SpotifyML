##importing libraries
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import mean_squared_error, r2_score
from itertools import combinations

if __name__ == '__main__':

    ##importing data
    df = pd.read_csv('data.csv')

    ##stripping data of non-numeric values
    df = df.drop(['artists', 'id', 'key', 'mode', 'release_date', 'name'], axis=1)

    ##determining what the best combination of variables is to remove: ['acousticness', 'danceability', 'explicit', 'speechiness', 'tempo', 'valence']
    #variableList = df.columns.tolist()
    #variableList.remove('popularity')
    #tempList = []
    #maxList = []
    #maxr = 0
    #model = tree.DecisionTreeRegressor()
    #for a in range(len(variableList)):
        #tempList = combinations(variableList, a)
        #for b in tempList:
            #tempr = 0
            #b = list(b)
            #b.append('popularity')
            #for a in range(5):
                #X_train, X_test, Y_train, Y_test = train_test_split(df.drop(b, axis=1), df['popularity'], test_size=0.2)
                #model = model.fit(X_test, Y_test)
                #Y_pred = model.predict(X_test)
                #tempr += r2_score(Y_test, Y_pred)
            #if tempr > maxr:
                #maxr = tempr
                #maxList = b
    #print(maxr, maxList)

    ##removing variables, separating data at 80-20 ratio, and creating X and Y sets for the independent and dependant variables
    X_train, X_test, Y_train, Y_test = train_test_split(df.drop(['acousticness', 'danceability', 'explicit', 'speechiness', 'tempo', 'valence', 'popularity'], axis=1), df['popularity'], test_size=0.2)

    ##determining what most effective depth is for decision tree (11)
    #x = 1
    #maxr = 0
    #maxx = 0
    #r = 0
    #while x < 35:
        #model = tree.DecisionTreeRegressor(max_depth=x)
        #model = model.fit(X_train, Y_train)
        #Y_pred = model.predict(X_test)
        #r = r2_score(Y_test, Y_pred)
        #if r > maxr:
            #maxr = r
            #maxx = x
        #print(x)
        #x+=1
    #print(maxr, maxx)

    ##creating decision tree model
    model = tree.DecisionTreeRegressor(max_depth=11)
    model = model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    ##printing model success and tree visualization
    print("____Decision Tree Model____")
    print('Mean squared error:', mean_squared_error(Y_test, Y_pred))
    print('R^2:', r2_score(Y_test, Y_pred))
    plt.scatter(Y_test, Y_pred, marker='+', alpha=.5)
    plt.show()
    plt.figure(figsize=(50,50))
    tree.plot_tree(model, feature_names=X_train.columns.tolist(), fontsize=8, filled=True)
    plt.show()