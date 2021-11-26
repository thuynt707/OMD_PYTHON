'''Kết nối CSDL'''
import mysql.connector as mysql
import pymysql

db = pymysql.connect(
    host = "remotemysql.com",
    user = "UyMDXcxEoz",
    passwd = "lFJmWnNbEC",
    database = "UyMDXcxEoz"
)

cur = db.cursor(pymysql.cursors.DictCursor)

def log(winner, players):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
    sql = '''INSERT INTO games (winner) VALUES (%s)'''
    cur.execute(sql, winner)

    game_id = cur.lastrowid

    sql = f'''
    INSERT INTO logs (game_id, player, cards, point, biggest_card)
    VALUES ({game_id}, %(player)s, %(cards)s, %(point)s, %(biggest_card)s)
    '''
    cur.executemany(sql, players)

    db.commit()

def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    sql = '''
    SELECT *
    FROM games AS g
    ORDER BY g.play_at DESC
    '''

    cur.execute(sql)
    game = cur.fetchone()

    if not game:
        raise Exception('Không có lịch sử game\nChơi vài game vui vẻ đi 😉\n')

    sql = f'''
    SELECT *
    FROM logs
    WHERE game_id = {game['game_id']}
    '''
    cur.execute(sql)
    players = cur.fetchall()

    return game, players


def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
    sql = '''
    SELECT
        winner as player,
        COUNT(*) AS game_won
    FROM games AS g
    WHERE DATE(g.play_at) = CURDATE()
    GROUP BY player
    ORDER BY game_won DESC
    '''

    cur.execute(sql)
    records = cur.fetchall()

    if not records:
        raise Exception('Không có lịch sử game\nChơi vài game vui vẻ đi 😉\n')

    total_game = sum([r['game_won'] for r in records])
    return total_game, records