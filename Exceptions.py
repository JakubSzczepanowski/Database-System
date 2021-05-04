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

