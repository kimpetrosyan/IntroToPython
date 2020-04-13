import sys
#sys.path.append("/Users/shahane/desktop/ACA_Python/Lecture6")


from draw import draw_game
#import draw
#from draw import *
#import draw as drw
#from draw import draw_game as dg

def play_game():
    return 'FIFA'

def main():
    result = play_game()
    draw_game(result)
    


# this means that if this script is executed, then 
# main() will be executed

if __name__ == '__main__':
    main()
    