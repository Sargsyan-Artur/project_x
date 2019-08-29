import pickle
import uuid


class Game(object):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.matrices = [1, 2, 3,
                         4, 5, 6,
                         7, 8, 9
                         ]


    def create_file(self, f_name):

        with open('games/{}'.format(f_name), 'wb') as f:
            pickle.dump(self.id, f)
            pickle.dump(self.matrices, f)


    def load_file(self, f_name, pos, x_or_o):
        fh = open('games/{}'.format(f_name), "rb")
        self.id = pickle.load(fh)
        self.matrices = pickle.load(fh)

        self.matrices[pos-1] = x_or_o

        fh.close()
        f = open('games/{}'.format(f_name), "wb")
        pickle.dump(self.id, f)
        pickle.dump(self.matrices, f)
        print(self.matrices)
        f.close()
        return self.matrices



    def check_game(self, f_name):
        fh = open('games/{}'.format(f_name), 'rb')
        game_id = pickle.load(fh)
        matr = pickle.load(fh)
        print(matr)
        chek_list = [
             matr[0:3],
             matr[3:6],
             matr[6:9],
             matr[::3],
             matr[1:9:3],
             matr[2:9:3],
             matr[0:9:4],
             matr[2:8:2],
        ]

        checked_x = ['x', 'x', 'x']
        checked_y = ['y', 'y', 'y']
        if checked_x in chek_list:
            print('x win')
            return 1
        elif checked_y in chek_list:
            print('y win')
            return 0

    def check_draw(self, f_name):
        fh = open('games/{}'.format(f_name), 'rb')
        game_id = pickle.load(fh)
        matr = pickle.load(fh)
        if int in matr:
            print('akkkkkkkkkaaaaaaaaa')
        # for i in matr:
        #     if type(i) == str:
        #         continue
        #         print('game continus')
        #         return True
        #     else:
        #         print('game drawwwwwwwwwwww')
        #         return False


