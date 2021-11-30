import sys
import os
import db
import error
from deck import Deck
from player import Player

class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.is_playing = False
        self.is_dealt = False
        self.is_flipped = False
        self._playerList = []
        self._deck = Deck()
        self.winner = None
        self.choices = {
            '1': self.list_players,
            '2': self.add_player,
            '3': self.remove_player,
            '4': self.dealing_card,
            '5': self.flip_cards,
            '6': self.last_game,
            '7': self.history,
            '8': self.quit
        }

    @property
    def deck(self):
        return self._deck

    @property
    def players(self):
        return self._players

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        self.cls()
        self._playerList = []
        inputPlayer = input('Nhap so luong nguoi choi:')
        inputPlayer = int(inputPlayer)
        for i in range(1,inputPlayer+1):
            player_name = input(f'Nhap ten nguoi choi {i}:')
            self._playerList.append(Player(i,player_name))

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        print("1.Danh sách người chơi"+ "(" + str(len(self._playerList)) +")")
        print("2.Thêm người chơi (có thể thêm)")
        print("3.Loại người chơi (Số người chơi tối thiểu rồi)")
        print("4.Chia bài")
        print("5.Lật bài")
        print("6.Xem lại game vừa chơi")
        print("7.Xem lịch sử chơi hôm nay")
        print("8.Công an tới, tốc biến!!!")

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print('ID\tPlayer Name')
        for player in self._playerList:
            print(f'{player._id}\t{player._name}')

    def add_player(self):
        '''Thêm một người chơi mới'''
        idx = len(self._playerList) +1
        name = input(f'Nhap ten nguoi choi thu {idx}:')
        self.players.append(Player(idx,name))

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        print("Nhập ID người chơi muốn xóa: ")
        index_player = int(input())
        del self.players[index_player-1]

    def dealing_card(self):
        '''Chia bài cho người chơi'''
        self._deck = Deck()
        self._deck.build()
        self._deck.shuffle_card()
        for p in self._playerList:
            p.remove_card()
        
        numberPlayer = len(self._playerList)
        cardNumber = 3
        for i in range(numberPlayer*cardNumber):
            playerIndex = i%numberPlayer
            card = self._deck.deal_card()
            self._playerList[playerIndex].add_card(card)
        print('Da chia xong!')
        self._is_deal = True

    def flip_cards(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        winner = None
        for player in self._playerList:
            player.flip_card()
            if winner == None:
                winner = player
            else:
                if winner.point == player.point:
                    if player.biggest_card > winner.biggest_card:
                        winner = player
                elif player.point > winner.point:
                    winner = player
        print(f'Nguoi chien thang:{winner._name}')
        self._winner = winner._name
        self._is_fliped = True

    def last_game(self):
        game, logs = db.get_last_game()
        if game is not None:
            print ("Thời gian: ", game['play_at'], ' Người chiến thắng: ', game['winner'])
            for log in logs:
                print (f"Người chơi {log['player']}: {log['cards']}", end="")                
                print (f", Tổng điểm {log['point']}, lá bài lớn nhất {log['biggest_card']}") 

    def history(self):
        historys = db.history()
        list_str = ""
        count_all = 0
        if historys is not None:
            for history in historys:
               count_all += history['count']
               list_str += f"{history['winner']} thắng {history['count']} ván\n"   
        print (f"Hôm nay đã chơi: {count_all} ván")     
        print (list_str)

    def run(self):
        self.setup()
        self.cls()

        while True:
            self.guide()

            try:
                c = input("> ")
                choice = self.choices.get(c)
                self.cls()

                if choice:
                    choice()
                    print()
                else:
                    raise error.FunctionDoesNotExists()
            except ValueError as e:
                raise error.FunctionDoesNotExists()
            except error.Error as e:
                print(e.message)

    def quit(self):
        print("Have fun :)")
        sys.exit()