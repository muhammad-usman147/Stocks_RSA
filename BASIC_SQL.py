import pypyodbc 
from tblBrokerTransConsol import tblBrokerTransConsole
from tblBrokerTransactions import tblBrokerTrans
from tblFxRates import tblFxRates
conenction = pypyodbc.connect('Driver={SQL Server};Server=.;Database=MetalTiger')
print("success")
#insert query
'''
cursor = conenction.cursor()
insert = "INSERT INTO ShareMaster(Code,Name,StockType) values('k','kk','kkk')"
cursor.execute(insert)
cursor.commit()
cursor.execute("SELECT * FROM ShareMaster")
s = ''
for row in cursor:    
    print(row)   
'''
cur = tblFxRates()
cur.BuildCurrency()
'''
sheet_name = 'Certificated CAD'
if sheet_name == 'Certificated CAD':
    brokerconsole = tblBrokerTrans()
    brokerconsole.InsertDataBuild(sheet_name=sheet_name)
else:
    brokerconsole = tblBrokerTransConsole()
    brokerconsole.InsertDataBuld(sheet_name=sheet_name)
'''
conenction.close()   