import sqlite3

connection = sqlite3.connect("userTable.db", check_same_thread=False)
crsr = connection.cursor()

def createTable(tableName):
	sql_command = f"""CREATE TABLE {tableName}(
		id SERIAL,
		username VARCHAR(30),
		password VARCHAR(30),
		email VARCHAR(40)
	);"""
	try:
		crsr.execute(sql_command)
	except:
		pass

def insertRow(tableName, serialNum, userName, password, email):
	sql_command = f"""INSERT INTO {tableName} VALUES ({serialNum}, '{userName}', '{password}', '{email}')"""
	crsr.execute(sql_command)
	connection.commit()

def deleteRow(tableName, serialNum):
	sql_command = f"""DELETE FROM {tableName} WHERE id={serialNum} """
	crsr.execute((sql_command))
	connection.commit()

def printTable(tableName):
	crsr.execute(f"SELECT * FROM {tableName}")
	ans = crsr.fetchall()
	for row in ans:
		print(row)

def checkIdentity(tableName, userName, password):
	crsr.execute(f"SELECT * FROM {tableName}")
	ans = crsr.fetchall()
	for row in ans:
		if row[1] == userName and row[2] == password:
			return True
	return False

	
createTable('user')
printTable('user')