import pypyodbc 
print("success")

conenction = pypyodbc.connect('Driver={SQL Server};Server=.;Database=MetalTiger')
#insert query

cursor = conenction.cursor()
insert = "INSERT INTO ShareMaster(Code,Name,StockType) values('k','kk','kkk')"
cursor.execute(insert)
cursor.commit()
cursor.execute("SELECT * FROM ShareMaster")
s = ''
for row in cursor:    
    print(row)   
    
conenction.close()   