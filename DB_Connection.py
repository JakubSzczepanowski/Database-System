import sqlite3
from tkinter import messagebox
import Exceptions as E

def open_connection():
    global conn,cursor
    conn = sqlite3.connect('database.db')
    print('Otwarto połączenie')
    cursor = conn.cursor()

def create_settings_table(obj,data):
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

        cursor.execute(f"""CREATE TABLE Products (
        id_product integer PRIMARY KEY,
        name text,
        netto_price real,
        vat_percentage integer,
        section text
        )""")

        cursor.execute("""CREATE TABLE Data (
        id_record integer PRIMARY KEY,
        quantity_price real,
        amount integer,
        date text,
        id_product integer
        )""")

        cursor.execute("""INSERT INTO settings(name_min,name_max,section_min,section_max,quantity_price_min,
        quantity_price_max,amount_min,amount_max,netto_price_min,netto_price_max)
        VALUES (?,?,?,?,?,?,?,?,?,?)""",data)
        conn.commit()
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
    else:
        messagebox.showinfo(parent=obj,title='Info',message='Ustawienia dotyczące pól zostały pomyślnie dodane')

def get_settings():
    cursor.execute("""SELECT name_min,name_max,section_min,section_max,quantity_price_min,
    quantity_price_max,amount_min,amount_max,netto_price_min,netto_price_max FROM settings""")
    return cursor.fetchall()[0]

def get_sections():
    cursor.execute("SELECT section FROM Products")
    sections = []
    for elem in cursor.fetchall():
        sections.append(elem[0].replace('_',' '))
    return sections

def get_products(section):
    cursor.execute(f"SELECT name FROM Products WHERE section='{section}'")
    products = []
    for elem in cursor.fetchall():
        products.append(elem[0])
    return products

def select_products():
    cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()

def select_supplies():
    cursor.execute("""SELECT Data.id_record,Data.date,Products.name,Data.quantity_price,Data.amount,Products.section FROM Data
    JOIN Products ON Data.id_product=Products.id_product WHERE Data.quantity_price IS NOT NULL
    """)
    return cursor.fetchall()

def select_sales():
    cursor.execute("""SELECT Data.id_record,Data.date,Products.name,Data.amount,Products.section FROM Data
    JOIN Products ON Data.id_product=Products.id_product WHERE Data.quantity_price IS NULL
    """)
    return cursor.fetchall()

def delete_product(id):
    cursor.execute("DELETE FROM Products WHERE id_product=?",(id,))
    conn.commit()

def delete_supply_or_sale(id):
    cursor.execute("DELETE FROM Data WHERE id_record=?",(id,))
    conn.commit()

def check_amount_correctness(obj):
    try:
        cursor.execute("SELECT amount,quantity_price FROM Data")
        result = 0
        for elem in cursor.fetchall():
            result += elem[0] if elem[1] is not None else -elem[0]
        if result >= 0:
            return True
        raise E.SaleGreaterThenCurrentAmount
    except E.SaleGreaterThenCurrentAmount as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
        return False

def insert_product(obj,prod):
    try:
        cursor.execute(f"SELECT name FROM Products WHERE section='{prod.Section}'")
        for elem in cursor.fetchall():
            if elem[0] == prod.Name:
                raise E.NameInThatSectionExistError
        cursor.execute(f"""INSERT INTO Products (name,netto_price,vat_percentage,section) 
        VALUES (:name,:netto_price,:vat_percentage,:section)""",\
            {'name':prod.Name,'netto_price':prod.Netto_price,'vat_percentage':prod.Vat_percentage,'section':prod.Section})
        conn.commit()
    except E.NameInThatSectionExistError as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
    else:
        messagebox.showinfo(parent=obj,title='Info',message='Produkt został pomyślnie dodany')

def edit_product(obj,prod,id):
    try:
        cursor.execute(f"""UPDATE Products SET name=?,netto_price=?,
        vat_percentage=?,section=? WHERE id_product=?
        """,(prod.Name,prod.Netto_price,prod.Vat_percentage,prod.Section,id))
        conn.commit()
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)

def edit_supply(obj,prod,id):
    try:
        cursor.execute(f"""UPDATE Data SET quantity_price=?,amount=? WHERE id_record=?
        """,(prod.Quantity_price,prod.Amount,id))
        conn.commit()
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)

def edit_sale(obj,prod,id):
    try:
        cursor.execute(f"""UPDATE Data SET amount=? WHERE id_record=?
        """,(prod.Amount,id))
        conn.commit()
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)

def insert_supply(obj,prod):
    try:
        cursor.execute(f"SELECT id_product FROM Products WHERE name='{prod.Name}'")
        id_product = cursor.fetchone()[0]
        cursor.execute("""INSERT INTO Data(quantity_price,amount,date,id_product) 
        VALUES (:quantity_price,:amount,:date,:id_product)""",\
            {'quantity_price':prod.Quantity_price,'amount':prod.Amount,'date':prod.Date,'id_product':id_product})
        conn.commit()
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
    else:
        messagebox.showinfo(parent=obj,title='Info',message='Rekord został pomyślnie dodany')

def insert_sale(obj,prod):
    try:
        cursor.execute(f"SELECT id_product FROM Products WHERE name='{prod.Name}'")
        id_product = cursor.fetchone()[0]
        cursor.execute("""INSERT INTO Data(quantity_price,amount,date,id_product) 
        VALUES (null,:amount,:date,:id_product)""",\
            {'amount':prod.Amount,'date':prod.Date,'id_product':id_product})
        conn.commit()
    except Exception as e:
        messagebox.showerror(parent=obj,title='Błąd',message=e)
    else:
        messagebox.showinfo(parent=obj,title='Info',message='Rekord został pomyślnie dodany')
    
def close_connection():
    conn.close()
    print('Zamknięto połączenie')
