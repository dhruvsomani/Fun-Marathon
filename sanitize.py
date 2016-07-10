import sqlite3
def sanitize(file, database):
    file = open(file)

    players = file.read()
    players = players.split('\n')
    for row in range(len(players)):
        players[row] = players[row].split('\t')
        players[row][0] = int(players[row][0])

    connection = sqlite3.connect(database)
    connection.executemany('INSERT INTO PLAYERS (ID, NAME, GENDER, CATEGORY) VALUES(?, ?, ?, ?)', players)
    connection.commit()


sanitize('E:\\data.txt', 'D:\\fun_marathon.sqlite3')