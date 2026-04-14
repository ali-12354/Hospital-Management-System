"""
Top-level database helper for a MySQL (XAMPP) connection.

This file provides a convenience `create_connection()` function that returns
a mysql.connector connection object to a local XAMPP MySQL server.

Note: This project already contains an SQLite helper at
`src/utils/database.py`. Keep that in mind — use one or the other.
"""
import mysql.connector
from mysql.connector import Error


def create_connection(host: str = 'localhost', user: str = 'root', password: str = '', database: str = 'hospital_System'):
	"""
	Creates and returns a connection to the XAMPP MySQL database.

	Parameters:
		host: MySQL host (default 'localhost')
		user: MySQL username (default 'root')
		password: MySQL password (default empty for XAMPP)
		database: Database name to connect to (default 'hospital_db')

	Returns:
		A mysql.connector connection object if successful, otherwise None.
	"""
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host,
			user=user,
			password=password,
			database=database
		)
		if connection.is_connected():
			print("MySQL Database connection successful")
		else:
			print("MySQL connection failed to establish")
	except Error as e:
		print(f"The error '{e}' occurred")
		connection = None
	

	return connection

