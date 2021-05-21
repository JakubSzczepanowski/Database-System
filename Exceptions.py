class NegativeValueError(Exception):
    def __init__(self):
        super(NegativeValueError,self).__init__('Podano ujemną liczbę')

class ValueOutOfRangeError(Exception):
    def __init__(self):
        super(ValueOutOfRangeError,self).__init__('Ta liczba jest z poza ustalonego przedziału')

class MinGreaterThanMaxError(Exception):
    def __init__(self):
        super(MinGreaterThanMaxError,self).__init__('Wartość stanowiąca minimalny przedział jest większa lub równa od granicy maksymalnej')

class NameInThatSectionExistError(Exception):
    def __init__(self):
        super(NameInThatSectionExistError,self).__init__('Produkt o danej nazwie już istnieje w danym dziale')

class TextIsNotAlphaNumeric(Exception):
    def __init__(self):
        super(TextIsNotAlphaNumeric,self).__init__('Ten tekst nie jest w formie alfanumerycznej')

class SaleGreaterThenCurrentAmount(Exception):
    def __init__(self):
        super(SaleGreaterThenCurrentAmount,self).__init__('Nie masz takiej ilości towaru w magazynie')

class EmptyFieldError(Exception):
    def __init__(self):
        super(EmptyFieldError,self).__init__('Wpisano puste pole')

