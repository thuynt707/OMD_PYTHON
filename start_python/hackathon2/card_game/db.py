'''Kết nối CSDL'''
from pymysql import connect, cursors,Error
from card import Card
from player import Player
from game import Game

config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "game_log",
    "cursorclass": cursors.DictCursor
}


def log():
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
    sql = '''
    INSERT INTO games (play_at, winner)
    VALUES (%s, %s)
    '''


def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    pass


def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
