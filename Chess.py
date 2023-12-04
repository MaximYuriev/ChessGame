from config import *
from chess_items import *
clock = pg.time.Clock()
screen = pg.display.set_mode(WINDOW_SIZE)
screen.blit(background,(0,0))
menu = Menu(screen)
pg.time.set_timer(pg.USEREVENT, 1000)
run = True
while run:
    if play:
        chessboard.print_moves()
        chessboard.get_turn()
        if chessboard.check_pat() == True:
            flag = 1
            if visible == 1:
                chessboard.declare_win(0)
                timer = 0
        if chessboard.get_shah(white) == True:
            shah_flag_w = 1
            if flag == 0:
                chessboard.print_shah(white)
            if chessboard.get_mat(white) == True:
                flag = 1
                chessboard.print_mat(white)
                if visible == 1:
                    chessboard.declare_win(black)
                    timer = 0
        else:
            if shah_flag_w == 1:
                shah_flag_w = 0
                chessboard.print_shah(0)
        if chessboard.get_shah(black) == True:
            shah_flag_b = 1
            if flag == 0:
                chessboard.print_shah(black)
            if chessboard.get_mat(black) == True:
                flag = 1
                chessboard.print_mat(black)
                if visible ==  1:
                    chessboard.declare_win(white)
                    timer = 0
        else:
            if shah_flag_b == 1:
                shah_flag_b = 0
                chessboard.print_shah(0)
    for event in pg.event.get():
        if event.type == pg.USEREVENT and play == True:
            if chessboard.turn == 0:
                if timer == 1:
                    chessboard.white_times -= 1
                    chessboard.print_time()
                if chessboard.white_times <=0:
                    timer = 0
                    flag = 1
                    if visible == 1:
                        chessboard.declare_win(black)
            elif chessboard.turn == 1:
                if timer == 1:
                    chessboard.black_times -= 1
                    chessboard.print_time()
                if chessboard.black_times <=0:
                    timer = 0
                    flag = 1
                    if visible == 1:
                        chessboard.declare_win(white)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if clickable_menu == 1:
                menu_chose = menu.btn_down(event.button, event.pos)
            if menu_chose == 0:
                clickable_menu = 0
                menu_chose = None
                screen.blit(background,(0,0))
                flag = 0
                chessboard = Chessboard(screen,timer)
                play = True
            if menu_chose == 1:
                clickable_menu = 0 
                menu.draw_menu_chose_color()
                chose_color = menu.chose_color_btn_down(event.button, event.pos)
                if chose_color == 0:
                    menu_chose = None
                    clickable_menu = 1
                    screen.blit(background,(0,0))
                    menu.draw_menu()
                if chose_color == 'w':
                    menu_chose = None
                    screen.blit(background,(0,0))
                    chessboard = Chessboard(screen,timer,1,chose_color)
                    flag = 0
                    play = True
                if chose_color == 'b':
                    menu_chose = None
                    screen.blit(background,(0,0))
                    chessboard = Chessboard(screen,timer,1,chose_color)
                    flag = 0
                    play = True
            if menu_chose == 2:
                clickable_menu = 0 
                if visible_setting_menu == 1:
                    chose_setting = menu.setting_btn_down(event.button, event.pos)
                    if chose_setting == 0:
                        menu_chose = None
                        clickable_menu = 1
                        screen.blit(background,(0,0))
                        visible_setting_menu = 0
                        menu.draw_menu()
                    if chose_setting == 2:
                        timer = 0
                        temp_time = timer
                    if chose_setting == 3:
                        timer = 1
                        temp_time = timer
                else:
                    menu.draw_setting()
                    visible_setting_menu = 1
            if menu_chose == 3:
                clickable_menu = 0
                if visible_rules == 1:
                    close_rules = menu.rules_btn_down(event.button, event.pos)
                    if close_rules == 0:
                        menu_chose = None
                        clickable_menu = 1
                        screen.blit(background,(0,0))
                        menu.draw_menu()
                        visible_rules = 0
                else:
                    visible_rules = 1
                    menu.draw_rules()
            if menu_chose == 4:
                clickable_menu = 0
                menu.draw_exit()
                chose_exit = menu.exit_btn_down(event.button, event.pos)
                if chose_exit == 0:
                    menu_chose = None
                    clickable_menu = 1
                    screen.blit(background,(0,0))
                    menu.draw_menu()
                if chose_exit == 1:
                    pg.quit()
                    run = False
        if event.type == pg.MOUSEBUTTONDOWN and flag == 0:
            chessboard.btn_down(event.button, event.pos)
        if event.type == pg.MOUSEBUTTONUP and flag == 0:
            chessboard.btn_up(event.button, event.pos)
        if event.type == pg.KEYDOWN and play == True:
            if event.key == pg.K_ESCAPE:
                visible_exit = 1
                flag = -1
                timer = 0
                chessboard.draw_exit()
        if event.type == pg.MOUSEBUTTONDOWN and visible_exit == 1:
            chose_exit_from_menu = chessboard.exit_btn_down(event.button,event.pos)
            if chose_exit_from_menu == 0:
                visible_exit = 0
                flag = 0
                if stop_time == 0:
                    timer = temp_time
                chessboard.grand_update()
            if chose_exit_from_menu == 1:
                visible_exit = 0
                play = False
                screen.blit(background,(0,0))
                menu.draw_menu()
                clickable_menu = 1
                flag = -1
                visible = 1
                shah_flag_w = 0
                shah_flag_b = 0
                chose_after_win = -1
                stop_time = 0
                timer = temp_time
        if event.type == pg.MOUSEBUTTONDOWN and flag == 1:
            stop_time = 1
            if visible == 1:
                chose_after_win = chessboard.declare_win_btn_dwn(event.button, event.pos)
            visible = 1    
            if chose_after_win == 0:
                play = False
                screen.blit(background,(0,0))
                menu.draw_menu()
                clickable_menu = 1
                flag = -1
                visible = 1
                shah_flag_w = 0
                shah_flag_b = 0
                stop_time = 0
                chose_after_win = -1
                timer = temp_time
            if chose_after_win == 1:
                chose_after_win = -1
                visible = 0
    clock.tick(FPS)
quit()