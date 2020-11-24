import numpy as np
import pandas as pd 
import pypyodbc 
from currency_converter import CurrencyConverter
class tblFxRates():
    def __init__(self):
        connection = pypyodbc.connect('Driver={SQL Server};Server=.;Database=MetalTiger')
        self.cursor = connection.cursor()
        self.currency = CurrencyConverter()
    
    def BuildCurrency(self,from_ = 'GBP',to = 'AUD',value = 1):
        """
        docstring
        """
        c = self.currency.convert(value,from_,to)
        print(c)

        self.cursor.execute("INSERT INTO tblFXRates(Date,GBP,AUD) values('2020-11-24 05:51:11','42','{}')".format(c))

        self.cursor.commit()


