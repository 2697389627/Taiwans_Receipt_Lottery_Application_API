from flask import Flask , Response
import json
from demjson import decode
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'UserName'
app.config['MYSQL_DATABASE_PASSWORD'] = 'UserPassword'
app.config['MYSQL_DATABASE_DB'] = 'DatabaseName'
app.config['MYSQL_DATABASE_HOST'] = 'DatabaseHost'

mysql = MySQL()
mysql.init_app(app)

@app.route('/time')
def provideTimeFile():
	cursor = mysql.get_db().cursor()
	cursor.execute( 'SELECT time from TableName' )
	data = cursor.fetchone()
	timeData = str( data[0] )
	return Response( timeData , mimetype = 'application/json' )

@app.route('/this_time')
def provideThisTimeFile():
	cursor = mysql.get_db().cursor()
	cursor.execute( 'SELECT this_time from TableName' )
	data = cursor.fetchone()
	timeData = str( data[0] )
	return Response( timeData , mimetype = 'application/json' )

@app.route('/last_time')
def provideLastTimeFile():
	cursor = mysql.get_db().cursor()
	cursor.execute( 'SELECT last_time from TableName' )
	data = cursor.fetchone()
	timeData = str( data[0] )
	return Response( timeData , mimetype = 'application/json' )

if __name__ == '__main__':
	app.run()
