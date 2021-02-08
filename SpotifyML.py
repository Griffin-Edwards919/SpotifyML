import pandas as pd, numpy
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

def func(x, a, b, c):
    return a * numpy.exp(-b * x) + c

if __name__ == '__main__':

    #importing data
    df = pd.read_csv('data.csv')

    #stripping data of non-numeric values
    df = df.drop(['artists', 'id', 'key', 'mode', 'release_date', 'name'], axis=1)

    #measuring correlation of the variables to the target variable
    corr = df.corr()
    print(corr['popularity'])

    #stripping data of any very weakly correlated variables
    df = df.drop(['duration_ms', 'liveness', 'tempo', 'valence'], axis=1)

    #separating data at 80-20 ratio and creating X and Y sets for the 8 independant variables and 1 dependant
    X_train, X_test = train_test_split(df, test_size=0.2)
    Y_train = X_train['popularity']
    Y_test = X_test['popularity']
    X_train = X_train.drop(['popularity'], axis=1)
    X_test = X_test.drop(['popularity'], axis=1)

    #creating least squares model
    model = linear_model.LinearRegression()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    #printing model success
    print("\n\n____Least Squares Model____")
    print('Coefficients:', model.coef_)
    print('Intercept:', model.intercept_)
    print('Mean squared error:', mean_squared_error(Y_test, Y_pred))
    print('R^2:', r2_score(Y_test, Y_pred))
    plt.scatter(Y_test, Y_pred, marker='+', alpha=.5)
    plt.show()

    # creating ridge model
    model = linear_model.Ridge()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    # printing model success
    print("\n\n____Ridge Model____")
    print('Coefficients:', model.coef_)
    print('Intercept:', model.intercept_)
    print('Mean squared error:', mean_squared_error(Y_test, Y_pred))
    print('R^2:', r2_score(Y_test, Y_pred))
    plt.scatter(Y_test, Y_pred, marker='+', alpha=.5)
    plt.show()

    #creating lasso model
    model = linear_model.Lasso()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    # printing model success
    print("\n\n____Lasso Model____")
    print('Coefficients:', model.coef_)
    print('Intercept:', model.intercept_)
    print('Mean squared error:', mean_squared_error(Y_test, Y_pred))
    print('R^2:', r2_score(Y_test, Y_pred))
    plt.scatter(Y_test, Y_pred, marker='+', alpha=.5)
    plt.show()

    # creating elastic-net model
    model = linear_model.ElasticNet()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    # printing model success
    print("\n\n____Elastic-Net Model____")
    print('Coefficients:', model.coef_)
    print('Intercept:', model.intercept_)
    print('Mean squared error:', mean_squared_error(Y_test, Y_pred))
    print('R^2:', r2_score(Y_test, Y_pred))
    plt.scatter(Y_test, Y_pred, marker='+', alpha=.5)
    plt.show()
