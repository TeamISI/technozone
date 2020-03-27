from database_connection import *

obj = Technozone()
result = obj.mysqlConnect('localhost','arcadio','practicasISI/1920','technozone')

if result:

    # ejeplo 1 - CREATE
    path = './database/create_tables.sql'
    mode = 'r'
    query = obj.open_file(path, mode)
    obj.prepare(query, None)
    if result:
        print("Creada")
    else:
        print(obj.error)

    # ejeplo 2 - INSERT
    print (obj.prepare("INSERT INTO tabla VALUES (null, now(), 'http')", None, False))
    print (obj.lastId)

    # ejemplo 3 - UPDATE
    query = "UPDATE tabla SET Texto=%s WHERE id=%s"
    params = ("XX",20)
    obj.prepare(query,params,False)
    if result:
        print (result)
    else:
        print (obj.error)
    print (obj.affectedRows())

    # ejemplo 4 - SELECT
    result=obj.prepare("SELECT id,Texto FROM tabla WHERE id=%s", (20,))
    if result:
        print (result)
    else:
        print (obj.error)
    
    # ejemplo 5 - DROP
    path = './database/drop_tables.sql'
    mode = 'r'
    query = obj.open_file(path, mode)
    result = obj.prepare(query, None)
    if result:
        print ("Borrada")
    else:
        print (obj.error)

    obj.mysqlClose()
else:
    print (obj.error)
