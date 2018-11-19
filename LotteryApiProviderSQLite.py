from flask import Flask , Response
import json
import sqlite3
from demjson import decode

app = Flask(__name__)

# please edit the right url where ApplicationDatabase.db is placed
DATABASE = '~/ApplicationDatabase.db'

@app.route('/time')
def provideTimeFile():
	conn = sqlite3.connect( DATABASE )
	cursor = conn.cursor()
	cursor.execute( 'SELECT time from LotteryTable' )
	result = cursor.fetchone()
	JsonString = decode( str( result[0] ) )
	cursor.close()
	conn.close()
	return Response ( json.dumps( JsonString ) , mimetype = 'application/json' ) 

@app.route('/this_time')
def provideThisTime():
	conn = sqlite3.connect( DATABASE )
	cursor = conn.cursor()
	cursor.execute( 'SELECT this_time from LotteryTable' )
	result = cursor.fetchone()
	JsonString = decode( str( result[0] ) )
	cursor.close()
	conn.close()
	return Response ( json.dumps( JsonString ) , mimetype = 'application/json' ) 
	
@app.route('/last_time')
def provideLastTime():
	conn = sqlite3.connect( DATABASE )
	cursor = conn.cursor()
	cursor.execute( 'SELECT last_time from LotteryTable' )
	result = cursor.fetchone()
	JsonString = decode( str( result[0] ) )
	cursor.close()
	conn.close()
	return Response ( json.dumps( JsonString ) , mimetype = 'application/json' ) 

if __name__ == '__main__':
	app.run()

