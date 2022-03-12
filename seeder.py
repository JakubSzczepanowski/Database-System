import sqlite3
import pandas as pd
import numpy as np
import random as r

produkty = [('Kajak', 1200, 23, 'Sporty wodne', ''), ('Czepek', 20, 17, 'Sporty wodne', ''), ('Okularki', 90, 23, 'Sporty wodne', ''), ('Kąpielówki', 30, 23, 'Sporty wodne', ''), ('Narty', 4800, 17, 'Sporty zimowe', 'Zimowy'), ('Kurtka narciarska', 3000, 23, 'Sporty zimowe', 'Zimowy'), ('Buty skiturowe', 2500, 17, 'Sporty zimowe', 'Zimowy'), ('Łyżwy', 230, 23, 'Sporty zimowe', 'Zimowy'), ('Gogle snowboardowe', 70, 23, 'Sporty zimowe', 'Zimowy'), ('Okulary przeciwsłoneczne', 3000, 23, 'Bieganie', 'Letni'), ('Buty biegowe', 300, 23, 'Bieganie', ''), ('Plecak do biegania', 150, 23, 'Bieganie', 'Letni'), ('Piłka do koszykówki', 90, 23, 'Sporty drużynowe', ''), ('Piłka do siatkówki', 100, 23, 'Sporty drużynowe', ''), ('Nakolanniki', 15, 23, 'Sporty drużynowe', ''), ('Piłka footballowa', 130, 23, 'Sporty drużynowe', '')]

daty = pd.date_range('2021-01-01', periods=365, freq='D')


def simulate(random_dates, price, id, sale_to):
    sprzedaz = True
    dostawy_sprzedaze = [(price*0.8, r.randint(30,50), random_dates[0].date().strftime('%Y-%m-%d'), id)]
    print(dostawy_sprzedaze)
    cumulative = dostawy_sprzedaze[0][1]
    print(cumulative)
    for i in range(1, len(random_dates)-1):
        if cumulative <= 5: 
            sprzedaz = False
        if sprzedaz:
            amount = r.randint(1,sale_to)
            while amount > cumulative: amount = r.randint(1,sale_to)
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

cursor.executemany(f"INSERT INTO Products (name,netto_price,vat_percentage,section,season) VALUES (?,?,?,?,?)",produkty)
conn.commit()

for index, i in enumerate(produkty):
    if index < 2/3*len(produkty):
        random_dates = pd.to_datetime(
        np.concatenate([
                np.random.choice(daty[1:-1], size=20, replace=False),
                daty[[0, -1]]
            ])
        ).sort_values()
        sale_to = 10
    else:
        random_dates = pd.date_range('2021-01-01', periods=12, freq='25D')
        sale_to = 4
    cursor.executemany(f"INSERT INTO Data(quantity_price,amount,date,id_product) VALUES (?,?,?,?)",simulate(random_dates, i[1], index+1, sale_to))

conn.commit()

conn.close()
