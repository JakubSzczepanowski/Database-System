import sqlite3
from tkinter import messagebox
import Exceptions as E

def open_connection():
    global conn,cursor
    conn = sqlite3.connect('database.db')
    print('Otwarto połączenie')
    cursor = conn.cursor()

def create_settings_table(data):
    try:
        cursor.execute("""CREATE TABLE settings (
            id_setting integer PRIMARY KEY,
            name_min integer,
            name_max integer,
            section_min integer,
            section_max integer,
            quantity_price_min integer,
            quantity_price_max integer,
            amount_min integer,
            amount_max integer,
            netto_price_min integer,
            netto_price_max integer
        )""")

        #conn.commit()

        cursor.execute("""INSERT INTO settings(name_min,name_max,section_min,section_max,quantity_price_min,
        quantity_price_max,amount_min,amount_max,netto_price_min,netto_price_max)
        VALUES (?,?,?,?,?,?,?,?,?,?)""",data)
        conn.commit()
    except Exception as e:
        messagebox.showerror(title='Błąd',message=e)
    else:
        messagebox.showinfo(title='Info',message='Ustawienia dotyczące pól zostały pomyślnie dodane')

def get_settings():
    cursor.execute("""SELECT name_min,name_max,section_min,section_max,quantity_price_min,
    quantity_price_max,amount_min,amount_max,netto_price_min,netto_price_max FROM settings""")
    return cursor.fetchall()[0]

def get_sections():
    cursor.execute("select name from sqlite_master where type = 'table'")
    sections = []
    for elem in cursor.fetchall():
        if elem[0] not in {'settings','produkty'}:
            sections.append(elem[0].replace('_',' '))
    return sections

def get_products(section):
    cursor.execute(f"SELECT name FROM {section}")
    products = []
    for elem in cursor.fetchall():
        products.append(elem[0])
    return products

def get_last_amount_and_quantity_price(obj,prod):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produkty'")
    if cursor.fetchone() is None:
        return None
    cursor.execute(f"""SELECT amount,quantity_price FROM produkty JOIN {prod.Section} 
    ON produkty.id_section={prod.Section}.id_section WHERE {prod.Section}.name='{prod.Name}'
    AND produkty.id_product=(SELECT MAX(id_product) FROM produkty)""")
    return cursor.fetchone()

def insert_product(obj,prod):
    try:
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {prod.Section} (
        id_section integer PRIMARY KEY,
        name text,
        netto_price real,
        vat_percentage integer
        )""")
        conn.commit()
        cursor.execute(f"SELECT name FROM {prod.Section}")
        for elem in cursor.fetchall():
            if elem[0] == prod.Name:
                raise E.NameInThatSectionExistError
        cursor.execute(f"""INSERT INTO {prod.Section}(name,netto_price,vat_percentage) 
        VALUES (:name,:netto_price,:vat_percentage)""",\
            {'name':prod.Name,'netto_price':prod.Netto_price,'vat_percentage':prod.Vat_percentage})
        conn.commit()
    except E.NameInThatSectionExistError as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
    else:
        messagebox.showinfo(parent=obj,title='Info',message='Produkt został pomyślnie dodany')

def insert_update(obj,prod):
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS produkty (
        id_product integer PRIMARY KEY,
        quantity_price real,
        amount integer,
        date text,
        section text,
        id_section integer
        )""")
        conn.commit()
        cursor.execute(f"SELECT id_section FROM {prod.Section} WHERE name='{prod.Name}'")
        id_section = cursor.fetchall()[0][0]
        cursor.execute("""INSERT INTO produkty(quantity_price,amount,date,section,id_section) 
        VALUES (:quantity_price,:amount,:date,:section,:id_section)""",\
            {'quantity_price':prod.Quantity_price,'amount':prod.Amount,'date':prod.Date,'section':prod.Section,'id_section':id_section})
        conn.commit()
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
    else:
        messagebox.showinfo(parent=obj,title='Info',message='Rekord został pomyślnie dodany')
    
def close_connection():
    conn.close()
    print('Zamknięto połączenie')
