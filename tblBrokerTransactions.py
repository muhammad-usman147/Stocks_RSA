import numpy as np
import pandas as pd 
import pypyodbc 
class tblBrokerTrans():
    def __init__(self):
        connection = pypyodbc.connect('Driver={SQL Server};Server=.;Database=MetalTiger')
        self.cursor = connection.cursor()

    
    def InsertDataBuild(self,sheet_name,filename = 'MTR Investments 07-11-2020 v1.xlsm'):
        """
        docstring
        """
        df = pd.read_excel('MTR Investments 07-11-2020 v1.xlsm',sheet_name=sheet_name)
        #emoving all the first 18 rows
        df = df[18:].iloc[:,1:10]
        cols = cols = ['date','reference','description','code','tx_type','non-share_transacts','shares',"price[local_currency]",'Ex_rate']
        #broker = sheet_name
        df.columns = cols
        for i in range(df.shape[0]):
            '''
            insert = "INSERT INTO tblBrokerTransConsol(Date,Reference,Description,Code,Txtype,Nonsharetransacts,Shares,Pricelocalcurrency,Exchangerate,year,month,Broker) values({},{},{},{},{},{},{},{},{},{},{},{})".format(str(df.iloc[i,0]),
            str(df.iloc[i,1]),str(df.iloc[i,2]),str(df.iloc[i,3]),str(df.iloc[i,4]),4
            ,df.iloc[i,6],df.iloc[i,7],str(df.iloc[i,7]),df.iloc[i,0].year,df.iloc[i,0].month,sheet_name)'''
            insert ="INSERT INTO tblBrokerTransactions(Date,Reference,Description,Code,Txtype,Nonsharetransacts,Shares,Pricelocalcurrency,Exchangerate,year,month,Broker) values('2016-01-01 00:00:00','nan','nan','AAU','b/fwd',4,4927777,0.8144443224602088,0.8144443224602088,2016,1,'certiusman')"
            self.cursor.execute(insert)
            self.cursor.commit()
            break
        
        
