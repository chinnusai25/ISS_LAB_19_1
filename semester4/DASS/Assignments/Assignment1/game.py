import signal,os,time

from alarmexception import AlarmException
from getch import _getChUnix as getChar
from board import Board
from mario import Mario
from scenary import Scenary

board=Board(30,500)
board.createboard()

mandalorian=Mario(25,0,1)
mandalorian.start(board.matrix)

s=Scenary()

s.create_ground(board.matrix)
s.create_sky(board.matrix)
s.create_beams(board.matrix,12,19)
# s.create_beams(board.m,12,99)
board.printit(0)


def movemario():
    def alarmhandler(signum,frame):
        raise AlarmException
    def user_input(timeout=0.1):
        signal.signal(signal.SIGALRM,alarmhandler)
        signal.setitimer(signal.ITIMER_REAL,timeout)

        try:
            text=getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM,signal.SIG_IGN)
        return ''

    char=user_input()
    
    if(char=='d'):
        is_it_safe=mandalorian.safety_check_at_right_move(board.matrix)
        if(is_it_safe==1):
            mandalorian.need_to_be_updated(board.matrix)
            print("GAME OVER")
            quit()
        else:
            mandalorian.need_to_be_updated(board.matrix)
            mandalorian.y+=1
            mandalorian.is_updated(board.matrix)

    if(char=='a'):
        is_it_safe=mandalorian.safety_check_at_left_move(board.matrix)
        if(is_it_safe==1):
            mandalorian.need_to_be_updated(board.matrix)
            print("GAME OVER")
            quit()
        else:
            mandalorian.need_to_be_updated(board.matrix)
            mandalorian.y-=1
            mandalorian.is_updated(board.matrix)

    if(char=='w'):
        is_it_safe=mandalorian.safety_check_at_up_move(board.matrix)
        if(is_it_safe==1):
            mandalorian.need_to_be_updated(board.matrix)
            print("GAME OVER")
            quit()
        else:
            mandalorian.need_to_be_updated(board.matrix)
            mandalorian.x-=1
            mandalorian.is_updated(board.matrix)


    if(char=='q'):
        quit()
    # print(char)
    # return char

x=round(time.time())
y=x

while True:
    
    os.system('clear')
    print('\n\n\n')
    board.printit(0)
    movemario()

    is_it_safe=mandalorian.safety_check_at_down_move(board.matrix)
    # print(mandalorian.x,is_it_safe,board.matrix[mandalorian.x+1][mandalorian.y])
    if(is_it_safe==1):
        mandalorian.need_to_be_updated(board.matrix)
        print("GAME OVER")
        quit()


    # if(round(time.time())-x>=0.1):
    #     # board.printit(0)
    #     os.system('clear')
    #     # movemario()
    #     print('\n\n\n')
    #     board.printit(0)
    #     x=round(time.time())
        
    if(round(time.time())-y>=0.01):
        is_it_safe=mandalorian.safety_check_at_down_move(board.matrix)
        if(is_it_safe==1):
            mandalorian.need_to_be_updated(board.matrix)
            print("GAME OVER")
            quit()
        else:
            if((mandalorian.x+1)<=25):
                mandalorian.need_to_be_updated(board.matrix)
                mandalorian.x+=1
                mandalorian.is_updated(board.matrix)
        y=round(time.time())