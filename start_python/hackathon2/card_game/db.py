'''Kết nối CSDL'''
import mysql.connector as mysql
import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "game_log"
)
cursor = db.cursor(pymysql.cursors.DictCursor)

# def log(winner, players):
#     '''
#     Ghi thông tin về game vào CSDL và 2 bảng games và logs

#     Bảng games gồm tên người chiến thắng

#     Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

#     Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
#     '''
#     sql = '''INSERT INTO games (winner) VALUES (%s)'''
#     cursor.execute(sql, winner)

#     game_id = cursor.lastrowid

#     sql = f'''
#     INSERT INTO logs (game_id, player, cards, point, biggest_card)
#     VALUES ({game_id}, %(player)s, %(cards)s, %(point)s, %(biggest_card)s)
#     '''
#     cursor.executemany(sql, players)

#     db.commit()

# def get_last_game():
#     '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
#     sql = '''
#     SELECT *
#     FROM games AS g
#     ORDER BY g.play_at DESC
#     '''

#     cursor.execute(sql)
#     game = cursor.fetchone()

#     if not game:
#         raise Exception('Không có lịch sử game\nChơi vài game vui vẻ đi 😉\n')

#     sql = f'''
#     SELECT *
#     FROM logs
#     WHERE game_id = {game['game_id']}
#     '''
#     cursor.execute(sql)
#     players = cursor.fetchall()

#     return game, players


# def history():
#     '''
#     Lấy thông tin về lịch sử chơi

#     Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
#     '''
#     sql = '''
#     SELECT
#         winner as player,
#         COUNT(*) AS game_won
#     FROM games AS g
#     WHERE DATE(g.play_at) = CURDATE()
#     GROUP BY player
#     ORDER BY game_won DESC
#     '''

#     cursor.execute(sql)
#     records = cursor.fetchall()

#     if not records:
#         raise Exception('Không có lịch sử game\nChơi vài game vui vẻ đi 😉\n')

#     total_game = sum([r['game_won'] for r in records])
#     return total_game, records

def log(winner, players):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs
    Bảng games gồm tên người chiến thắng
    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game
    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
    query = "INSERT INTO games(winner) VALUES (%(winner)s)"
    cursor.execute(query, { "winner": winner.name})
    db.commit()
    game_id = cursor.lastrowid
    print(game_id)

    query = "INSERT INTO logs (game_id, player, cards, 	point, biggest_card) VALUES (%(game_id)s, %(player)s, %(cards)s, %(point)s, %(biggest_card)s)"
    ## storing values in a variable
    values = []
    for player in players:
        values.append({"game_id" : game_id,
                       "player": player.name,
                       "cards": player.flip_card(),
                       "point": player.point,
                       "biggest_card" : str(player.biggest_card)
                       })
    
    cursor.executemany(query, values)
    db.commit()

def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    sql = '''SELECT * FROM games ORDER BY game_id DESC limit 1'''
    cursor.execute(sql)
    game = cursor.fetchone()
    logs = None
    
    if game is not None:
        sql = '''SELECT * FROM logs WHERE game_id = "%(game_id)s" ORDER BY log_id'''
        cursor.execute(sql, {"game_id": game["game_id"]})
        logs = cursor.fetchall()
    return game, logs


def history():
    '''
    Lấy thông tin về lịch sử chơi
    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
    sql = "SELECT winner, COUNT(winner) as count FROM games WHERE DATE(play_at) = CURDATE() GROUP BY winner ORDER BY `count` DESC"
    cursor.execute(sql)
    return cursor.fetchall()