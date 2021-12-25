import DB_Connection
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dts
from datetime import datetime

def show_supply_plot(name):
    lista = DB_Connection.select_supplies_for_specific_product(name)
    if len(lista) == 0: raise IndexError
    show_plot(lista)

def show_cumulative_amount_plot(name):
    lista = DB_Connection.select_amount_and_date_for_specific_product(name)
    print(lista)
    #lista.append(('2021-09-25', 500, True))
    # lista.append(('2021-10-20', 100, False))
    # lista.append(('2021-11-24', 200, False))
    if len(lista) == 0: raise IndexError
    
    show_plot(lista, True)


def show_sale_plot(name):
    lista = DB_Connection.select_sales_for_specific_product(name)
    show_plot(lista)

def show_plot(lista, cumulative=False):
    lista = np.array(lista)
    X, Y = extract_time_domain_and_amount_range(lista)
    Z = list(map(lambda item: False if item is None else True, lista[:,2]))
    cumulate_dates(X, Y, Z)
    if cumulative:
        cumulate = 0
        for i in range(len(Y)):
            cumulate += Y[i] if Z[i] or Y[i] < 0 else -Y[i]
            Y[i] = cumulate
    print(X, Y)
    dates = dts.date2num(X)
    plt.plot_date(dates, Y, linestyle='solid')
    plt.show()

def extract_time_domain_and_amount_range(data):
    dates = list(map(lambda date: datetime.strptime(date, '%Y-%m-%d'), data[:,0]))
    amounts = list(map(int, data[:,1]))
    return (dates, amounts)

def extract_timestamp_domain_and_amount_range(data):
    dates = list(map(lambda date: datetime.strptime(date, '%Y-%m-%d').timestamp(), data[:,0]))
    amounts = list(map(int, data[:,1]))
    return (dates, amounts)

def cumulate_dates(X,Y,Z):
    pointer = (0, X[0])
    same = []; i = 0
    while i != len(X)-1:
        i += 1
        if X[i] == pointer[1]:
            if len(same) == 0:
                same.append(pointer[0])
            same.append(i)
        else:
            if len(same) != 0:
                transform_specific_dates(X, Y, Z, same)
                i -= len(same)
                same.clear()
            pointer = (i, X[i])
        if i == len(X)-1 and len(same) != 0:
            transform_specific_dates(X, Y, Z, same)
            i -= len(same)
            same.clear()

def transform_specific_dates(X, Y, Z, same):
    new_value = 0
    for i in same:
        print(Y[i],Z[i])
        new_value += Y[i] if Z[i] else -Y[i]
        print(new_value)
    Y[same[0]] = new_value
    del same[0]
    for i in same:
        del X[i]
        del Y[i]
        del Z[i]

def predict_supply(name):
    lista = DB_Connection.select_amount_and_date_for_specific_product(name)
    if len(lista) == 0: raise IndexError

    lista = np.array(lista)
    X, Y = extract_timestamp_domain_and_amount_range(lista)
    Z = list(map(lambda item: False if item is None else True, lista[:,2]))
    cumulate_dates(X, Y, Z)
    cumulate = 0
    for i in range(len(Y)):
        cumulate += Y[i] if Z[i] or Y[i] < 0 else -Y[i]
        Y[i] = cumulate

    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression
    
    X, Y = np.array(X).reshape(-1,1), np.array(Y)
    sca = StandardScaler().fit(X)
    print(X,Y)
    X_scale = sca.transform(X)
    lin_reg = LinearRegression()
    lin_reg.fit(X_scale, Y)
    print('coef', lin_reg.coef_)
    print('intercept', lin_reg.intercept_)
    x = np.arange(X_scale[0], X_scale[-1])
    y = x*lin_reg.coef_+lin_reg.intercept_
    print(X_scale,Y)
    when_empty = sca.inverse_transform(-lin_reg.intercept_/lin_reg.coef_)
    print(when_empty)
    print(datetime.fromtimestamp(*when_empty))
    # plt.plot(X_scale,Y)
    # plt.plot(x,y)
    # plt.show()


DB_Connection.open_connection()
predict_supply('Spodnie')
DB_Connection.close_connection()
# from sklearn.linear_model import LinearRegression
# lin_reg = LinearRegression()
# X = np.array([[1],[2],[3],[4],[5]])
# y = np.dot(X, np. array([2])) + 3.
# print(y)
# lin_reg.fit(X, y)
# print('coef', lin_reg.coef_)
# print('intercept', lin_reg.intercept_)

# lista = DB_Connection.select_amount_and_date_for_specific_product('Spodnie')
# show_plot(lista, True)
# print(lista)
# lista = np.array(lista)
# X, Y = extract_time_domain_and_amount_range(lista)
# Z = list(map(lambda item: False if item is None else True, lista[:,2]))
# print(Z)
# cumulate_dates2(X, Y, Z)
# print(X)
# print(Y)
