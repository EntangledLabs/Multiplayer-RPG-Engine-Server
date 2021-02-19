import sqlite3

class database():

	def __init__(self, file):
		self.file = file

	def open(self):
		self.con = sqlite3.connect(self.file)
		self.cursor = self.con.cursor()
		
	def insert(self, table, table_cols, values):
		# Take columns from table_cols and make string
		collist = str
		index = 0
		for col in table_cols:
			collist = collist + col
			if (index != len(table_cols)-1):
				collist = collist + ", "
			else:
				index = index + 1

		# Read number of values and make appropriate substitution string
		vallist = str
		index = 0
		for val in values:
			vallist = vallist + '?'
			if (index != len(values)-1):
				vallist = vallist + ", "
			else:
				index = index + 1

		statement = "INSERT INTO {}({}) VALUES ({})".format(table, collist, vallist)

		self.cursor.execute(statement, values)
		self.con.commit()