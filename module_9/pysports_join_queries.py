"""
    Drew King
    CSD310 Mod 9.2
    Join Queries
    2//21 
"""


import mysql.connector

from mysql.connector import errorcode

config ={
    "user": "pysports_user", 
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
try:
    #connect to the pysports database
    db = mysql.connector.connect(**config)

  #query pysports database  
    cursor = db.cursor()

# create inner table
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id");
    players = cursor
    
   #create print "Display" title
    print("-- DISPLAYING PLAYER RECORDS --")
    
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}" .format(player[1]))
        print("Last Name: {}" .format(player[2]))
        print("Team Name: {}" .format(player[3]))
        print("")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
     print("The specified database does not exist")

    else:
        print(err)

finally:
        db.close()