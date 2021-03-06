import psycopg2


def connPostgreSQL():
	try:
		conn = psycopg2.connect(database="dvdtwo", user = "postgres", password = "p@ssword", host = "127.0.0.1", port = "5432")
		print("Opened connection successfully")
		#conn.close()
		#print("Connection Closed")
	except:
		print("Connection failed")
	return conn

if __name__ == "__main__":
	
	con = connPostgreSQL()
	cur = con.cursor()
	
	cur.execute("SELECT actor_id, first_name, last_name from actor")
	rows = cur.fetchall()
	for row in rows:
		print("ID = ".format(row[0]))
		print("FirstName = {}".format(row[1]))
		print("LastName = {}. \n".format( row[2]))

	print( "Operation done successfully")
	con.close()