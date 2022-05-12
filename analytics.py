import DB_Connection
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dts
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def show_supply_plot(name):
    lista = DB_Connection.select_supplies_for_specific_product(name)
    if len(lista) == 0: raise IndexError
    plt.title('Wykres dostaw w funkcji czasu')
    show_plot(lista, is_supply=True)

def show_cumulative_amount_plot(name):
    lista = DB_Connection.select_amount_and_date_for_specific_product(name)
    if len(lista) == 0: raise IndexError
    plt.title('Wykres bieżących ilości na stanie w funkcji czasu')
    show_plot(lista, cumulative=True)

def show_sale_plot(name):
    lista = DB_Connection.select_sales_for_specific_product(name)
    plt.title('Wykres sprzedaży w funkcji czasu')
    show_plot(lista)

def show_plot(lista, cumulative=False, is_supply=False):
    lista = np.array(lista)
    X, Y = extract_time_domain_and_amount_range(lista)
    if is_supply:
        cumulate_dates(X, Y, None, True)
    if cumulative:
        Z = list(map(lambda item: False if item is None else True, lista[:,2]))
        cumulate_dates(X, Y, Z)
        cumulate = 0
        for i in range(len(Y)):
            cumulate += Y[i] if Z[i] or Y[i] < 0 else -Y[i]
            Y[i] = cumulate
    dates = dts.date2num(X)
    plt.xlabel('Czas')
    plt.ylabel('Ilość')
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

def cumulate_dates(X, Y, Z, is_supply=False):
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
                transform_specific_dates(X, Y, Z, same, is_supply)
                i -= len(same)
                same.clear()
            pointer = (i, X[i])
        if i == len(X)-1 and len(same) != 0:
            transform_specific_dates(X, Y, Z, same, is_supply)
            i -= len(same)
            same.clear()

def transform_specific_dates(X, Y, Z, same, is_supply):
    new_value = 0
    for i in same:
        if is_supply: new_value += Y[i]
        else: new_value += Y[i] if Z[i] else -Y[i]
    Y[same[0]] = new_value
    if not is_supply: Z[same[0]] = True
    del same[0]
    for _ in same:
        del X[same[0]]
        del Y[same[0]]
        if not is_supply: del Z[same[0]]

def predict_resume(name):
    lista = DB_Connection.select_amount_and_date_for_specific_product(name)
    
    lista = np.array(lista)
    X, Y = extract_timestamp_domain_and_amount_range(lista)
    Z = list(map(lambda item: False if item is None else True, lista[:,2]))
    cumulate_dates(X, Y, Z)
    cumulate = 0
    for i in range(len(Y)):
        cumulate += Y[i] if Z[i] or Y[i] < 0 else -Y[i]
        Y[i] = cumulate
    data_backup = (X,Y)
    cut = 0; index = len(X)-1; cut2 = 0
    while index != 0:
        if Z[index]:
            if cut == 0: cut = index
            elif cut2 == 0: 
                cut2 = index
                break
        index -= 1
    
    X, Y, Z = X[cut:], Y[cut:], Z[cut:]
    if len(X) in (0,1): raise IndexError
    days_range = (datetime.fromtimestamp(X[-1])-datetime.fromtimestamp(X[0])).days

    sale_for_day = (Y[0]-Y[-1])/days_range
    sale_ratio = 'Brakuje danych'
    if abs(cut2-cut) > 1:
        old_X, old_Y = data_backup
        old_dates = old_X[cut2:cut]
        old_amounts = old_Y[cut2:cut]
        old_days_range = (datetime.fromtimestamp(old_dates[-1])-datetime.fromtimestamp(old_dates[0])).days
        old_sale_for_day = (old_amounts[0]-old_amounts[-1])/old_days_range
        sale_ratio = sale_for_day/old_sale_for_day*100
    
    X, Y = np.array(X).reshape(-1,1), np.array(Y)
    sca = StandardScaler().fit(X)
    X_scale = sca.transform(X)
    lin_reg = LinearRegression()
    lin_reg.fit(X_scale, Y)
    if lin_reg.coef_[0] == 0: return (name, 'Nie potrzebujesz dostawy', sale_ratio, sale_for_day)
    when_empty = sca.inverse_transform(-lin_reg.intercept_/lin_reg.coef_)
    
    now = datetime.now()
    supply_date = datetime.fromtimestamp(*when_empty)
    if supply_date < now and lin_reg.coef_[0] > 0:
        return (name, 'Nie potrzebujesz dostawy', sale_ratio, sale_for_day)
    elif supply_date < now and lin_reg.coef_[0] < 0:
        new_date = now + timedelta(days=int(Y[-1]/sale_for_day))
        return (name, 'Potrzebujesz dostawy' if new_date == now else new_date.date(), sale_ratio, sale_for_day)
    return (name, supply_date.date(), sale_ratio, sale_for_day)
