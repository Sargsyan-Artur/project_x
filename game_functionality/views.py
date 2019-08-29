from django.shortcuts import render
from .utils import Game


def index(request):
    game_id = request.session.get('game_id', False)
    game = Game()
    x_or_o = request.session.get('x_or_o', False)
    if request.method == 'POST':
        count = 0
        if game_id:
            print(x_or_o)
            #if game.check_draw(game_id):
            if x_or_o == 'x':
                game.load_file(game_id, int(request.POST['btn']), x_or_o)
                game.check_game(game_id)
                x_or_o = request.session['x_or_o'] = 'o'
                print('xorx = x')
            else:
                print(x_or_o)
                game.load_file(game_id, int(request.POST['btn']), x_or_o)
                game.check_game(game_id)
                x_or_o = request.session['x_or_o'] = 'x'
                print('x_oro = 000000')
            # else:
            #     print('vews draw')
    else:

        request.session['game_id'] = game.id
        request.session['x_or_o'] = 'x'
        game.create_file(game.id)
    return render(request, 'index.html')
# def index(request):
#     x_or_o = 'x'
#
#     game_id = request.session.get('game_id', False)
#     game = Game()
#
#
#     if request.method == 'POST':
#         if game_id:
#             if x_or_o == 'x':
#
#                 print('pox-0')
#                 pos_x_o = game.load_file(game_id)
#                 #pos_x_o[int(request.POST['btn'])-1] = 'x'
#                 #print(request.POST['btn'])
#                 x_or_o = 'o'
#                 print(pos_x_o)
#             else:
#
#                 pos_x_o = game.load_file(game_id)
#                 pos_x_o[int(request.POST['btn'])-1] = 'o'
#                 print(request.POST['btn'])
#                 x_or_o = 'x'
#                 print(pos_x_o)
#         else:
#             print('creqat new file')
#             game.create_file(game_id)
#             request.session['game_id'] = game.id
#
#
#             print(request. session['game_id'])
#     return render(request, 'index.html')








#http: // qaru.site / questions / 1068600 / ajax - post - in -django - framework
#https://stackoverflow.com/questions/13465711/how-do-i-post-with-jquery-ajax-in-django