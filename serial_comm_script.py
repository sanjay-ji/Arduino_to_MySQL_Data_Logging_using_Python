import serial # Serial library
import MySQLdb # MySQL 
import time 

db = MySQLdb.connect(host= "127.0.0.1", # usually "localhost"
port = 3306, # default port of MySQL.
user ="root", # username
passwd="Matrix789", # password of MySQL
db="test_db") # name of the database used here
cur = db.cursor() # Opening and closing connection with database.

# connecting with computers serial port
ser = serial.Serial('/dev/ttyACM0',baudrate = 9600) # port in which Arduino board is connected = /dev/ttyACM0
time.sleep(3) # time for connection process to complete and become stable

# function to read values from the serial port
def readValues():
    receivedData = ser.readline().split(str.encode('\r\n'))
    return receivedData[0]

while 1:

    ser.write(str.encode('a')) # sending 'a' to Arduino board
    value1 = readValues() # when arduino recieves 'a' it sends the corresponding value to the computer
    
    ser.write(str.encode('b')) # using str.encode() to convert unicode strings to bytes
    value2 = readValues()

    ser.write(str.encode('c'))
    value3 = readValues()

    ser.write(str.encode('d'))
    value4 = readValues()

    time.sleep(10) # time between two consecutive data transmissions, chnage it as per your requirements

    # To check the received values in the pyrhon shell and not needed for data logging purpose
    print('value_1 =',value1)   
    print("value_2 =",value2)
    print("value_3 =",value3)
    print("value_4 =",value4)

    # Loading data into MySQL databse "test_db" and table name "table2"
    sql = "INSERT INTO table2(value1,value2,value3,value4) VALUES (%s,%s,%s,%s)" 
    data = (value1,value2,value3,value4)
    cur.execute(sql,data)
    db.commit()
