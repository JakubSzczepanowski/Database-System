import Exceptions as E
from tkinter import messagebox

class Product:
    def __init__(self,name_min=1,name_max=20,section_min=1,section_max=20,\
        quantity_price_min=1,quantity_price_max=10,amount_min=1,amount_max=20,\
            netto_price_min=1,netto_price_max=10):
            self.name_min = name_min
            self.name_max = name_max
            self.section_min = section_min
            self.section_max = section_max
            self.quantity_price_min = quantity_price_min
            self.quantity_price_max = quantity_price_max
            self.amount_min = amount_min
            self.amount_max = amount_max
            self.netto_price_min = netto_price_min
            self.netto_price_max = netto_price_max
            self.name = None
            self.section = None
            self.quantity_price = None
            self.amount = None
            self.netto_price = None
            self.vat_percentage = None
            self.date = None
    
    @property
    def Name(self):
        return self.name
    
    @Name.setter
    def Name(self,n):
        n,obj = n
        if self.check_str_correctness(obj,n,self.name_min,self.name_max):
            self.name = n

    @property
    def Section(self):
        return self.section

    @Section.setter
    def Section(self,n):
        n,obj = n
        if self.check_str_correctness(obj,n,self.section_min,self.section_max):
            self.section = n

    @property
    def Quantity_price(self):
        return self.quantity_price

    @Quantity_price.setter
    def Quantity_price(self,n):
        n,obj = n
        n = self.check_float_correctness(obj,n,self.quantity_price_min,self.quantity_price_max)
        if n is not None:
            self.quantity_price = n

    @property
    def Amount(self):
        return self.amount

    @Amount.setter
    def Amount(self,n):
        n,obj = n
        n = self.check_int_correctness(obj,n,self.amount_min,self.amount_max)
        if n is not None:
            self.amount = n

    @property
    def Netto_price(self):
        return self.netto_price

    @Netto_price.setter
    def Netto_price(self,n):
        n,obj = n
        n = self.check_float_correctness(obj,n,self.netto_price_min,self.netto_price_max)
        if n is not None:
            self.netto_price = n

    @property
    def Vat_percentage(self):
        return self.vat_percentage

    @Vat_percentage.setter
    def Vat_percentage(self,n):
        n,obj = n
        try:
            n = int(n)
        except ValueError:
            messagebox.showerror(parent=obj,title='Błąd',message='Wpisano tekst zamiast liczby')
        else:
            if n in {0,17,23}:
                self.vat_percentage = n
            else:
                self.vat_percentage = 23
    @property
    def Date(self):
        return self.date

    @Date.setter
    def Date(self,n):
        self.date = n

    def check_int_correctness(self,obj,n:str,x:int,y:int) -> int:
        try:
            if n == '':
                raise E.EmptyFieldError
            elif len(n) < x or len(n) > y:
                raise E.ValueOutOfRangeError
            n = int(n)
            if n < 0:
                raise E.NegativeValueError
        except ValueError:
            messagebox.showerror(parent=obj,title='Błąd',message='W polu przeznaczonym na liczbę wstawiono znaki')
            return None
        except (E.ValueOutOfRangeError,E.NegativeValueError,E.EmptyFieldError) as e:
            messagebox.showerror(parent=obj,title='Błąd',message=e)
            return None
        else:
            return n

    def check_float_correctness(self,obj,n:str,x:int,y:int) -> float:
        try:
            if n == '':
                raise E.EmptyFieldError
            elif len(n.split('.')[0]) < x or len(n.split('.')[0]) > y:
                raise E.ValueOutOfRangeError
            n = round(float(n),2)
            if n < 0:
                raise E.NegativeValueError
        except ValueError as e:
            messagebox.showerror(parent=obj,title='Błąd',message='W polu przeznaczonym na liczbę wstawiono znaki')
            return None
        except (E.ValueOutOfRangeError,E.NegativeValueError,E.EmptyFieldError) as e:
            messagebox.showerror(parent=obj,title='Błąd',message=e)
            return None
        else:
            return n

    def check_str_correctness(self,obj,n:str,x:int,y:int) -> bool:
        try:
            if n == '':
                raise E.EmptyFieldError
            elif len(n) < x or len(n) > y:
                raise E.ValueOutOfRangeError
            if not n.replace(' ','a').isalnum():
                raise E.TextIsNotAlphaNumeric
        except (E.ValueOutOfRangeError,E.TextIsNotAlphaNumeric,E.EmptyFieldError) as e:
            messagebox.showerror(parent=obj,title='Błąd',message=e)
            return False
        else:
            return True


    def final_prod_check(self,prod):
        for p in prod:
            if p is None:
                return False
        return True
