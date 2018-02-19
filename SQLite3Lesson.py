import sqlite3

if __name__ == "__main__":
	
	db = sqlite3.connect("Student.db")
	db.execute("drop table if exists grades")
	db.execute("create table grades(id int, name text, score int)")
	db.execute("insert into grades(id,name,score) values(101,'John',99)")
	db.execute("insert into grades(id,name,score) values(102,'Gary',90)")
	db.execute("insert into grades(id,name,score) values(103,'James',80)")
	db.execute("insert into grades(id,name,score) values(104,'Cathy',85)")
	db.execute("insert into grades(id,name,score) values(105,'Kris',95)")
	db.commit()
	result = db.execute("select * from grades order by score")
	for row in result:
		print(row)
	print("-" * 50)
	
	db.execute("update grades set score = 88 where name = 'Cathy'")
	db.commit()
	result = db.execute("select * from grades order by id")
	for row in result:
		print(row)
	
	db.close()