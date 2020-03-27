#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install pymysql Para poder connectarnos
import pymysql 

class Technozone(object):
 
    def __init__(self):
        # Variable que determina si estamos conectados a MySQL...
        self.connected=0
        self.error=""
 
    def mysqlConnect(self,host,user,pw,database,port=3306):
        """
        Realiza la conexion con la base de datos
        Tiene que recibir:
            - host
            - user
            - pw => password
            - database => database name
        Puede recibir:
            - port
        Devuelve True o False
        """
        try:
            self.db = pymysql.connect(user=user, passwd=pw, host=host, db=database, port=port, charset="utf8", init_command="set names utf8")
            self.cursor = self.db.cursor()
            self.connected=1
            return True
        except Exception as e:
            self.error="Error: %s" % (e)
        return False
 
    def prepare(self,query,params=None,execute=True):
        """
        Funcion que ejecuta una instruccion mysql
        Tiene que recibir:
            - query
        Puede recibir:
            - params => tupla con las variables
            - execute => devuelve los registros
        Devuelve False en caso de error
        """
        if self.connected:
            self.error=""
            try:
                self.cursor.execute(query,params)
                self.db.commit()
                return True
            except Exception as e:
                self.error="Error: %s" % (e)
        return False
 
    def lastId(self):
        """
        Funcion que devuelve el ultimo id añadido
        """
        return self.cursor.lastrowid
 
    def affectedRows(self):
        return self.cursor.rowcount
 
    def mysqlClose(self):
        """
        Funcion para cerrar la conexion con la base de datos
        """
        self.connected=0
        try:
            self.cursor.close()
        except:pass
        try:
            self.cnx.close()
        except:pass
 
    def fetchOneAssoc(self,cursor) :
        # procesa una unica linea usando el metodo fetchone().
        data = cursor.fetchone()
        if data == None :
            return None
    
    #Para abrir un fichero
    def open_file(self, path, mode):
        with open(path, mode) as myfile:
            return myfile.read()