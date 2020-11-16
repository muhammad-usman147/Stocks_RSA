import pypyodbc 
print("success")

conenction = pypyodbc.connect('Driver={SQL Server};Server=.;Database=MetalTiger')

cursor = conenction.cursor()

cursor.execute("SELECT * FROM ShareMaster")
s = ''
for row in cursor:    
    print(type(row))   
    break
conenction.close()   