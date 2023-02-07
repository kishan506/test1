import mysql.connector as m
import mysql.connector.errors as ae

class UserDao:
	def __init__(self):
		try:
			self.con = m.connect(host="localhost",user="root",password="",database="ecommerce");
			print("Connection is successfully")
			
		except ae.DatabaseError as de:
			print(de)
		
	def insertUser(self,user):
		try:
			cur = self.con.cursor()
			sql = "insert into user (uname,uemail,upassword,uAdddress) values (%s,%s,%s,%s);"
			value = (user.getName(),user.getEmail(),user.getPassword(),user.getAddress())
			cur.execute(sql,value)
			self.con.commit()
			return "registered..."
		except ae.ProgrammingError as e:
			print(e)
		except Exception as e:
			print("python error : ",e)
		
		

	def updatePassword(self,email,password):
		try:
			cur = self.con.cursor()
			sql = "update user set upassword = %s where uemail = %s;"
			value = (password,email)
			cur.execute(sql,value)
			self.con.commit()
			return "updated..."
		except ae.ProgrammingError as e:
			print(e)
		except Exception as e:
			print("python error : ",e)

	def login(self,email,password):
		try:
			cur = self.con.cursor()
			sql = "select uname,uid from user where uemail=%s and upassword=%s;"
			value = (email,password)
			cur.execute(sql,value)
			a = cur.fetchone()
			self.con.commit()
			return a
		except ae.ProgrammingError as e:
			print(e)
		except Exception as e:
			print("python error : ",e)