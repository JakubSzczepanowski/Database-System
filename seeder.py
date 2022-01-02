import sqlite3
import pandas as pd
import numpy as np
import random as r

produkty = [('Kajak', 1200, 23, 'Sporty wodne'), ('Czepek', 20, 17, 'Sporty wodne'), ('Okularki', 90, 23, 'Sporty wodne'), ('Kąpielówki', 30, 23, 'Sporty wodne'), ('Narty', 4800, 17, 'Sporty zimowe'), ('Kurtka narciarska', 3000, 23, 'Sporty zimowe'), ('Buty skiturowe', 2500, 17, 'Sporty zimowe'), ('Łyżwy', 230, 23, 'Sporty zimowe'), ('Gogle snowboardowe', 70, 23, 'Sporty zimowe'), ('Okulary przeciwsłoneczne', 3000, 23, 'Bieganie'), ('Buty biegowe', 300, 23, 'Bieganie'), ('Plecak do biegania', 150, 23, 'Bieganie'), ('Piłka do koszykówki', 90, 23, 'Sporty drużynowe'), ('Piłka do siatkówki', 100, 23, 'Sporty drużynowe'), ('Nakolanniki', 15, 23, 'Sporty drużynowe'), ('Piłka footballowa', 130, 23, 'Sporty drużynowe')]

daty = pd.date_range('2021-01-01', periods=365, freq='D')


def supply_sales(random_dates, price, id):
    sprzedaz = True
    dostawy_sprzedaze = [(price*0.8, r.randint(30,50), random_dates[0].date().strftime('%Y-%m-%d'), id)]
    print(dostawy_sprzedaze)
    cumulative = dostawy_sprzedaze[0][1]
    print(cumulative)
    for i in range(1, len(random_dates)-1):
        if cumulative <= 5: 
            sprzedaz = False
        if sprzedaz:
            amount = r.randint(1,10)
            while amount > cumulative: amount = r.randint(1,10)
        else: amount = r.randint(30,50)
        dostawy_sprzedaze.append((None if sprzedaz else price*0.8, amount, random_dates[i].date().strftime('%Y-%m-%d'), id))
        cumulative += -amount if sprzedaz else amount
        print(dostawy_sprzedaze[i], cumulative)
        if sprzedaz == False: sprzedaz = True
    return dostawy_sprzedaze


# for index, i in enumerate(produkty):
#     random_dates = pd.to_datetime(
#     np.concatenate([
#             np.random.choice(daty[1:-1], size=20, replace=False),
#             daty[[0, -1]]
#         ])
#     ).sort_values()
#     supply_sales(random_dates, i[1], index+1)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.executemany(f"INSERT INTO Products (name,netto_price,vat_percentage,section) VALUES (?,?,?,?)",produkty)
conn.commit()

for index, i in enumerate(produkty):
    random_dates = pd.to_datetime(
    np.concatenate([
            np.random.choice(daty[1:-1], size=20, replace=False),
            daty[[0, -1]]
        ])
    ).sort_values()
    cursor.executemany(f"INSERT INTO Data(quantity_price,amount,date,id_product) VALUES (?,?,?,?)",supply_sales(random_dates, i[1], index+1))

conn.commit()

conn.close()