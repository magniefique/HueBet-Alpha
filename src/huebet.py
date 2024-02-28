import pygame
from sys import exit
import random

# initialize pygame and pygame.mixer
pygame.init()
pygame.mixer.init()

# set size of the window
windowx, windowy = 512,512
window = pygame.display.set_mode((512,512))

# set caption for the window
pygame.display.set_caption("Hue Bet")

# set icon for the window
icon = pygame.image.load('assets/imgs/color-game-icon.png')
pygame.display.set_icon(icon)

# load font for the playerbalance
balance_font = pygame.font.Font('assets/font/balance_font.ttf', 20)

# load font for bet amount  
bet_font = pygame.font.Font('assets/font/balance_font.ttf', 15)

# load font for the round_count 
round_count_font = pygame.font.Font('assets/font/base_font.otf', 32)

# declare FPS variable
FPS = pygame.time.Clock()

# load background and buttons for main menu
main_menu_playbuttonarray = [pygame.image.load('assets/imgs/background/main_menu1.jpg').convert_alpha(),
                             pygame.image.load('assets/imgs/background/main_menu1_hover.jpg').convert_alpha()]
main_menu_playbutton_ctr = 0
main_menu_exitbuttonarray = [pygame.image.load('assets/imgs/background/main_menu2.jpg').convert_alpha(),
                             pygame.image.load('assets/imgs/background/main_menu2_hover.jpg').convert_alpha(),]
main_menu_exitbutton_ctr = 0
main_menu_background1 = pygame.image.load('assets/imgs/background/main_menu3.jpg').convert_alpha()
main_menu_background2 = pygame.image.load('assets/imgs/background/main_menu4.jpg').convert_alpha()

# load image for background
maingame_background = pygame.image.load('assets/imgs/background/table.jpg').convert_alpha()

# load images for red button
red_button = [pygame.image.load('assets/imgs/button/redbutton.png').convert_alpha(),
              pygame.image.load('assets/imgs/button_activate/redbutton_activate.png').convert_alpha()]
red_ctr = 0
# load images for green button 
green_button = [pygame.image.load('assets/imgs/button/greenbutton.png').convert_alpha(),
                pygame.image.load('assets/imgs/button_activate/greenbutton_activate.png').convert_alpha()]
green_ctr = 0
# load images for blue button
blue_button = [pygame.image.load('assets/imgs/button/bluebutton.png').convert_alpha(),
               pygame.image.load('assets/imgs/button_activate/bluebutton_activate.png').convert_alpha()]
blue_ctr = 0
# load images for pink button 
pink_button = [pygame.image.load('assets/imgs/button/pinkbutton.png').convert_alpha(),
               pygame.image.load('assets/imgs/button_activate/pinkbutton_activate.png').convert_alpha()]
pink_ctr = 0
# load images for yellow button
yellow_button = [pygame.image.load('assets/imgs/button/yellowbutton.png').convert_alpha(), 
                 pygame.image.load('assets/imgs/button_activate/yellowbutton_activate.png').convert_alpha()]
yellow_ctr = 0
# load images for violet button
violet_button = [pygame.image.load('assets/imgs/button/violetbutton.png').convert_alpha(), 
                 pygame.image.load('assets/imgs/button_activate/violetbutton_activate.png').convert_alpha()]
violet_ctr = 0
# load images for end turn button
endturn_button = [pygame.image.load('assets/imgs/button/endturnbutton.png').convert_alpha(),
                  pygame.image.load('assets/imgs/button_activate/endturnbutton_activate.png')]
endturn_ctr = 0
# load images for main menu button while in game
mainmenu_ingame_button = pygame.image.load('assets/imgs/button/mainmenubutton_ingame.png')

# load color result images
default_result = pygame.image.load('assets/imgs/result_color/default_result.png').convert_alpha()
red_result = pygame.image.load('assets/imgs/result_color/red_result.png').convert_alpha()
green_result = pygame.image.load('assets/imgs/result_color/green_result.png').convert_alpha()
blue_result = pygame.image.load('assets/imgs/result_color/blue_result.png').convert_alpha()
pink_result = pygame.image.load('assets/imgs/result_color/pink_result.png').convert_alpha()
yellow_result = pygame.image.load('assets/imgs/result_color/yellow_result.png').convert_alpha()
violet_result = pygame.image.load('assets/imgs/result_color/violet_result.png').convert_alpha()
result_array = [default_result, red_result, green_result, blue_result, pink_result, yellow_result, violet_result]

# load images for player_win and player_lose
player_win_bg = pygame.image.load('assets/imgs/background/player_win.jpg').convert_alpha()
player_lose_bg = pygame.image.load('assets/imgs/background/player_lose.jpg').convert_alpha()
draw_bg = pygame.image.load('assets/imgs/background/draw.jpg').convert_alpha()
retry_button = pygame.image.load('assets/imgs/button/retrybutton.png').convert_alpha()
mainmenu_button = pygame.image.load('assets/imgs/button/mainmenubutton.png').convert_alpha()

# function for the main menu
def menu():
    # declare global variables needed in this function
    global main_menu_playbutton_ctr, main_menu_exitbutton_ctr
    
    # loads the background music for main menu
    pygame.mixer.music.load('assets/music/bgmusic.mp3')
    # plays the background music in a loop 
    pygame.mixer.music.play(-1)

    # main loop for the main menu
    while True:
        # sets the tick value to 60 
        FPS.tick(60)

        # sets cursor to arrow
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        # checks the events in pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # checks if a certain button is clicked           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse_pos[0] <= 0+256 and 0 <= mouse_pos[1] <= 0+256:
                    pygame.mixer.music.pause()
                    main_game()
                elif 256 <= mouse_pos[0] <= 256+256 and 256 <= mouse_pos[1] <= 256+256:
                    exit()

        # gets the mouse position
        mouse_pos = pygame.mouse.get_pos()

        # if else statements for hover effect on buttons
        if 0 <= mouse_pos[0] <= 0+256 and 0 <= mouse_pos[1] <= 0+256:
            main_menu_playbutton_ctr = 1
        else:
            main_menu_playbutton_ctr = 0

        if 256 <= mouse_pos[0] <= 256+256 and 256 <= mouse_pos[1] <= 256+256:
            main_menu_exitbutton_ctr = 1
        else:
            main_menu_exitbutton_ctr = 0

        # displays the buttons and background for the main menu
        window.blit(main_menu_playbuttonarray[main_menu_playbutton_ctr],(0,0))
        window.blit(main_menu_exitbuttonarray[main_menu_exitbutton_ctr],(256,256))
        window.blit(main_menu_background2,(256,0))
        window.blit(main_menu_background1,(0,256))
        
        # updates the screen 
        pygame.display.update()

# function for the main game
def main_game():
    # declare global variables needed in this function
    global red_ctr, green_ctr, blue_ctr, pink_ctr, yellow_ctr, violet_ctr, endturn_ctr

    # loads the background music for the main game
    pygame.mixer.music.load('assets/music/ingamemusic.mp3')
    # plays the background music in a loop 
    pygame.mixer.music.play(-1)
    
    # loads the sound effects for the main game
    button_sound = pygame.mixer.Sound('assets/music/buttonclick.mp3')
    endturnbutton_sound = pygame.mixer.Sound('assets/music/endturnclick.mp3')
    endshuffle_sound = pygame.mixer.Sound('assets/music/endshuffle.wav')
    buttonreset_sound = pygame.mixer.Sound('assets/music/buttonreset.mp3')

    # variable that stores the balance of the player and the enemy bot
    playerbalance = 1000
    enemybalance = 1000

    # array that stores the color of the balances
    balance_fontcolor = [(80,238,80), (255,0,0)]
    # counter for the array balance_fontcolor for both the player and enemy bot respectively
    balance_fontcolor_check = 0
    enemybalance_fontcolor_check = 0

    # variable for the bet needed for each round
    bet = 10

    # counts the rounds
    round_count = 1

    # variable that checks if the player has start the color shuffling
    play_game = False
    # variable for printing the winnings of the player or enemy bot or both 
    displayadd = False
    # variable responsible for locking the buttons in the main game
    button_lock = False
    # variable responsible for reseting the values for the next round
    reset = False
    # variable that identifies the winner 
    matchRes = None
    # variable that checks if there is already a winner
    ismatchDone = False
    
    # array that contains the results so that it could be displayed in the window
    result = [0,0,0]

    # array that stores the colors that the user chose
    user_bet = []
    # array that stores the colors that the enemy bot chose
    enemy_bet = []
    # array that contains the colors that the enemy bot can choose
    enemy_color_array = ['red','green','blue','pink','yellow','violet']

    # variables that serves as a counter for the animation
    partial_animation_ctr = 0.0
    result_animation_ctr = 0

    # main loop for the game
    while True:
        # FPS of the game
        FPS.tick(60)

        # checks for the events
        for event in pygame.event.get():
            # event for quitting the application
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # event for all the buttons in main game
            if event.type == pygame.MOUSEBUTTONDOWN:
                # checks if buttons are not locked, if true, the buttons can be clicked
                if button_lock == False:
                # click event for the red button
                    if (windowx/2-176 <= mouse_pos[0] <= windowx/2-176+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and red_ctr == 0 and (playerbalance >= bet):
                        red_ctr = 1
                        playerbalance -= bet
                        # adds red in array user_bet
                        user_bet.append("red")
                        # plays sound effect button_sound
                        button_sound.play()
                    elif (windowx/2-176 <= mouse_pos[0] <= windowx/2-176+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and red_ctr == 1:
                        red_ctr = 0
                        playerbalance += bet
                        # removes red in array user_bet
                        user_bet.remove("red")
                        # plays sound effect button_sound
                        button_sound.play()

                    # click event for the green button
                    elif (windowx/2-112 <= mouse_pos[0] <= windowx/2-112+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and green_ctr == 0 and (playerbalance >= bet):
                        # responsible for changing the sprite for the button
                        green_ctr = 1
                        playerbalance -= bet
                        # adds green in array user_bet
                        user_bet.append("green")
                        # plays sound effect button_sound
                        button_sound.play()      
                    elif (windowx/2-112 <= mouse_pos[0] <= windowx/2-112+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and green_ctr == 1:
                        # responsible for changing the sprite for the button
                        green_ctr = 0
                        playerbalance += bet
                        # removes green in array user_bet
                        user_bet.remove("green")
                        # plays sound effect button_sound
                        button_sound.play()   

                    # click event for the blue button
                    elif (windowx/2-48 <= mouse_pos[0] <= windowx/2-48+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and blue_ctr == 0 and (playerbalance >= bet):
                        # responsible for changing the sprite for the button
                        blue_ctr = 1
                        playerbalance -= bet
                        # adds blue in array user_bet
                        user_bet.append("blue")
                        # plays sound effect button_sound
                        button_sound.play()   
                    elif (windowx/2-48 <= mouse_pos[0] <= windowx/2-48+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and blue_ctr == 1:
                        # responsible for changing the sprite for the button
                        blue_ctr = 0
                        playerbalance += bet
                        # removes blue in array user_bet
                        user_bet.remove("blue")
                        # plays sound effect button_sound
                        button_sound.play()  

                    # click event for the pink button
                    elif (windowx/2+16 <= mouse_pos[0] <= windowx/2+16+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and pink_ctr == 0 and (playerbalance >= bet):
                        # responsible for changing the sprite for the button
                        pink_ctr = 1
                        playerbalance -= bet
                        # adds pink in array user_bet
                        user_bet.append("pink")
                        # plays sound effect button_sound
                        button_sound.play() 
                    elif (windowx/2+16 <= mouse_pos[0] <= windowx/2+16+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and pink_ctr == 1:
                        # responsible for changing the sprite for the button
                        pink_ctr = 0
                        playerbalance += bet
                        # removes pink in user_bet
                        user_bet.remove("pink")
                        # plays sound effect button_sound
                        button_sound.play()   

                    # click event for the yellow button
                    elif (windowx/2+80 <= mouse_pos[0] <= windowx/2+80+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and yellow_ctr == 0 and (playerbalance >= bet):
                        # responsible for changing the sprite for the button
                        yellow_ctr = 1
                        playerbalance -= bet
                        # adds yellow in array user_bet
                        user_bet.append("yellow")
                        # plays sound effect button_sound
                        button_sound.play()   
                    elif (windowx/2+80 <= mouse_pos[0] <= windowx/2+80+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and yellow_ctr == 1:
                        # responsible for changing the sprite for the button
                        yellow_ctr = 0
                        playerbalance += bet
                        # removes yellow in array user_bet
                        user_bet.remove("yellow")
                        # plays sound effect button_sound
                        button_sound.play()  

                    # click event for the violet button
                    elif (windowx/2+144 <= mouse_pos[0] <= windowx/2+144+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and violet_ctr == 0 and (playerbalance >= bet):
                        # responsible for changing the sprite for the button
                        violet_ctr = 1
                        playerbalance -= bet
                        # adds violet in array user_bet
                        user_bet.append("violet")
                        # plays sound effect button_sound
                        button_sound.play() 
                    elif (windowx/2+144 <= mouse_pos[0] <= windowx/2+144+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32) and violet_ctr == 1:
                        # responsible for changing the sprite for the button
                        violet_ctr = 0
                        playerbalance += bet
                        # removes violet in array user_bet
                        user_bet.remove("violet")
                        # plays sound effect button_sound
                        button_sound.play()  

                    # click event for the endturn button
                    elif (windowx/2+128 <= mouse_pos[0] <= windowx/2+128+64 and windowy/2-12 <= mouse_pos[1] <= windowy/2-12+64) and play_game == False and user_bet!=[]:
                        # variable that gets the number of colors the enemy bot will bet on
                        enemy_bet_count = random.randint(1,6)
                        # loop that gets the color that enemy bot choses
                        for i in range(enemy_bet_count):
                            if enemybalance > bet:
                                enemy_bet_color = enemy_color_array[random.randint(0,5)]
                                if enemy_bet_color not in enemy_bet:
                                    enemybalance -= bet
                                    # adds the color that the enemy choses in array enemy_bet
                                    enemy_bet.append(enemy_bet_color)
                            # breaks the loop if value of enemybalance is less than the bet value
                            elif enemybalance < bet:
                                break
                        # sets the variable play_game to True
                        play_game = True

                # click event for the main menu button in main game
                if (windowx-74 <= mouse_pos[0] <= windowx-74+72 and 2 <= mouse_pos[1] <= 2+24):
                    # resets the values if main menu button is clicked
                    red_ctr, green_ctr, blue_ctr, pink_ctr, yellow_ctr, violet_ctr = 0,0,0,0,0,0
                    user_bet = []
                    enemy_bet = []
                    result_animation_ctr = 0
                    partial_animation_ctr = 0.0
                    # go to function menu() if clicked
                    menu()

            # variable for mouse button hold   
            mouse_hold = pygame.mouse.get_pressed()

            # checks if the certain button is held or not
            if mouse_hold[0] and (windowx/2+128 <= mouse_pos[0] <= windowx/2+128+64 and windowy/2-16 <= mouse_pos[1] <= windowy/2-16+64):
                # responsible for changing the sprite for the button
                endturn_ctr = 1
                # plays sound for endturn button
                endturnbutton_sound.play()
            else:
                # responsible for changing the sprite for the button
                endturn_ctr = 0                 

        # continuously prints the background
        window.blit(maingame_background,(0,0))
        
        # display the all the player buttons on the screen
        window.blit(red_button[red_ctr],(windowx/2-176,windowy/2+144))
        window.blit(green_button[green_ctr],(windowx/2-112,windowy/2+144))
        window.blit(blue_button[blue_ctr],(windowx/2-48,windowy/2+144))
        window.blit(pink_button[pink_ctr],(windowx/2+16,windowy/2+144))
        window.blit(yellow_button[yellow_ctr],(windowx/2+80,windowy/2+144))
        window.blit(violet_button[violet_ctr],(windowx/2+144,windowy/2+144))
        window.blit(endturn_button[endturn_ctr], (windowx/2+128, windowy/2-12))
        window.blit(mainmenu_ingame_button, (windowx-74,2))

        # displays all the colors that the enemy bot chose
        if "red" in enemy_bet:
            window.blit(red_button[1],(windowx/2+144,windowy/2-177))
        if "green" in enemy_bet:
            window.blit(green_button[1],(windowx/2+80,windowy/2-177))
        if "blue" in enemy_bet:
            window.blit(blue_button[1],(windowx/2+16,windowy/2-177))
        if "pink" in enemy_bet:
            window.blit(pink_button[1],(windowx/2-48,windowy/2-177))
        if "yellow" in enemy_bet:
            window.blit(yellow_button[1],(windowx/2-112,windowy/2-177))
        if "violet" in enemy_bet:
            window.blit(violet_button[1],(windowx/2-176,windowy/2-177))

        # displays the result colors for each round
        window.blit(result_array[result[0]], (windowx/2-112, windowy/2-8))
        window.blit(result_array[result[1]], (windowx/2-32, windowy/2-8))
        window.blit(result_array[result[2]], (windowx/2+48, windowy/2-8))

        # displays the playerbalance on the window
        playerbalance_render = balance_font.render(str(playerbalance), True, balance_fontcolor[balance_fontcolor_check])
        window.blit(playerbalance_render,(windowx/2-5, windowy/2+89))

        # displays the enemybalance on the window
        enemybalance_render = balance_font.render(str(enemybalance), True, balance_fontcolor[enemybalance_fontcolor_check])
        window.blit(enemybalance_render, (windowx/2+130.5, windowy/3.436))

        # displays the bet value for each round on the window
        bet_font_render = bet_font.render(str(bet), True, (255,215,0))
        window.blit(bet_font_render, (windowx/2+44, windowy/2-54))

        # displays the round count on the window
        round_count_render = round_count_font.render(str(round_count), True, (255,255,255))
        window.blit(round_count_render, (windowx/2-170, windowy/2-2))

        # if true, displays the value that is added to both playerbalance and enemybalance
        if displayadd == True:
            if playerbalance_add != 0:
                playerbalance_add_render = balance_font.render("+" + str(playerbalance_add), True, balance_fontcolor[0])
                window.blit(playerbalance_add_render, (windowx/2-70.5, windowy/2+89))
            if enemybalance_add != 0:
                enemybalance_add_render = balance_font.render("+" + str(enemybalance_add), True, balance_fontcolor[0])
                window.blit(enemybalance_add_render, (windowx/2+60, windowy/3.436))

        # hover function for each player button
        mouse_pos = pygame.mouse.get_pos()
        if (windowx/2-176 <= mouse_pos[0] <= windowx/2-176+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        elif (windowx/2-112 <= mouse_pos[0] <= windowx/2-112+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        elif (windowx/2-48 <= mouse_pos[0] <= windowx/2-48+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        elif (windowx/2+16 <= mouse_pos[0] <= windowx/2+16+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        elif (windowx/2+80 <= mouse_pos[0] <= windowx/2+80+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        elif (windowx/2+144 <= mouse_pos[0] <= windowx/2+144+32 and windowy/2+144 <= mouse_pos[1] <= windowy/2+144+32):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        elif (windowx/2+128 <= mouse_pos[0] <= windowx/2+128+64 and windowy/2-12 <= mouse_pos[1] <= windowy/2-12+64):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        elif (windowx-74 <= mouse_pos[0] <= windowx-74+72 and 2 <= mouse_pos[1] <= 2+24):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            # returns to arrow if not on top of a button
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
        # checks the amount of player balance for its font color
        # if player balance is less than bet, turn font to red
        if playerbalance >= bet:
            balance_fontcolor_check = 0
        elif playerbalance < bet:
            balance_fontcolor_check = 1

        # checks the amount of enemy balance for its font color
        # if enemy balance is less than bet, turn font to red
        if enemybalance >= bet:
            enemybalance_fontcolor_check = 0
        elif enemybalance < bet:
            enemybalance_fontcolor_check = 1

        # checks if play_game is True
        if play_game == True:
            # locks all button in the main game except for the main menu button
            button_lock = True

            # lines of code for initiating the color game
            # responsible for the animation of the result colors
            if result_animation_ctr <= 12:
                if result_animation_ctr == 0:
                    result = [0,0,0]
                elif result_animation_ctr == 1 or result_animation_ctr == 7:
                    result = [1,0,0]
                elif result_animation_ctr == 2 or result_animation_ctr == 8:
                    result = [0,2,0]
                elif result_animation_ctr == 3 or result_animation_ctr == 9:
                    result = [0,0,3]
                elif result_animation_ctr == 4 or result_animation_ctr == 10:
                    result = [4,0,0]
                elif result_animation_ctr == 5 or result_animation_ctr == 11:
                    result = [0,5,0]
                elif result_animation_ctr == 6 or result_animation_ctr == 12:
                    result = [0,0,6]
                partial_animation_ctr += 0.05
                result_animation_ctr = round(partial_animation_ctr)
            else:
                if result_animation_ctr <= 30:
                    # sets the color of all of the result colors to black before displaying the finals colors for the round
                    result = [0,0,0]
                    partial_animation_ctr += 0.5
                    result_animation_ctr = round(partial_animation_ctr)
                else:
                    # counter for the array result str
                    result_ctr = 0
                    # arrays that stores the result color for each round
                    temp_result = []
                    result_str = []
                    # variables for the values that will be added to playerbalance and enemybalance respectively
                    playerbalance_add = 0
                    enemybalance_add = 0
                    # while loop that is responsible for choosing what the result colors will be for each round
                    while result_ctr < 3 :
                        result_randomize = random.randint(1,6)
                        # if else statements responsible for adding the string values of the colors chosen of the program to result_str
                        if result_randomize == 1:
                            result_str.append("red")
                        elif result_randomize == 2:
                            result_str.append("green")
                        elif result_randomize == 3:
                            result_str.append("blue")
                        elif result_randomize == 4:
                            result_str.append("pink")
                        elif result_randomize == 5:
                            result_str.append("yellow")
                        elif result_randomize == 6:
                            result_str.append("violet")
                        # adds the result color that was chosen by the program to temp_result
                        temp_result.append(result_randomize)
                        result_ctr += 1
                    # stores the values of array temp_result to result so that it could be displayed on the window
                    result = temp_result
                    # plays the sound 
                    endshuffle_sound.play()

                    # checks if the colors that the user chose is in result_str and add twice the value of bet in playerbalance if true
                    for i in user_bet:
                        if i in result_str:
                            playerbalance_add += bet*2
                            playerbalance += bet*2
                    
                    # checks if the colors that the enemy bot chose is in result_str and add twice the value of bet in enemybalance if true
                    for i in enemy_bet:
                        if i in result_str:
                            enemybalance_add += bet*2
                            enemybalance += bet*2

                    # resets values of partial_animation_ctr, result_animation_ctr, and array result_str
                    partial_animation_ctr = 0.0
                    result_animation_ctr = 0
                    result_str = []
                    # sets the value of displayadd to True
                    displayadd = True
                    # sets the value of reset to True
                    reset = True
                    # sets the value of play_game to True
                    play_game = False

        # updates the display
        pygame.display.update()

        # checks if reset is True, if true, reset certain values
        if reset == True:
            # delays the program
            if result_animation_ctr < 10:
                partial_animation_ctr += 0.15
                result_animation_ctr = round(partial_animation_ctr)
            else:
                # increases the value of bet for the next round
                bet *= 2
                # checks if playerbalance, enemybalance, or both of them is less than bet value 
                if playerbalance < bet and enemybalance < bet:
                    # if playerbalance is greater than enemybalance set matchRes to 1
                    if playerbalance > enemybalance:
                        matchRes = 1
                    # if enemybalance is greater than playerbalance set matchRes to 2
                    elif enemybalance > playerbalance:
                        matchRes = 2
                    # if they are equal set matchRes to 3
                    else:
                        matchRes = 3
                else:
                    # if enemybalance is less than bet value set match res to 1    
                    if enemybalance < bet:
                        matchRes = 1
                    # if playerbalance is less than bet value set match res to 2
                    elif playerbalance < bet:
                        matchRes = 2
                # increase round_count
                round_count += 1
                # if round count is equal to 9, compare values of playerbalance and enemybalance
                if round_count == 9:
                    # if playerbalance is greater than enemybalance, set matchRes to 1
                    if playerbalance > enemybalance:
                        matchRes = 1
                    # if enemybalance is greater than playerbalance, set matchRes to 2
                    elif playerbalance < enemybalance:
                        matchRes = 2
                    # if they are equal set matchRes to 3
                    else:
                        matchRes = 3
                # reset user_bet, enemy_bet, result_animation_ctr, partial_animation_ctr, and the counters for each of the colors to reset their colors
                user_bet = []
                enemy_bet = []
                result_animation_ctr = 0
                partial_animation_ctr = 0.0
                red_ctr, green_ctr, blue_ctr, pink_ctr, yellow_ctr, violet_ctr = 0,0,0,0,0,0

                # plays the sound for button reset
                buttonreset_sound.play()
                
                # set displayadd, button_lock, and reset to False
                displayadd = False
                button_lock = False
                reset = False

        # checks if value of matchRes is not None, if true, set ismatchDone to True
        if matchRes != None:
            ismatchDone = True

        # checks if value of ismatchDone is True
        if ismatchDone == True:
            # set buttonn_lock to True
            button_lock = True
            # delays the program
            if result_animation_ctr < 10:
                partial_animation_ctr += 0.1
                result_animation_ctr = round(partial_animation_ctr)
            else:
                # if match res is 1 call function player_win()
                if matchRes == 1:
                    player_win()
                # if match res is 2 call function player_lose()
                elif matchRes == 2:
                    player_lose()
                # if match res is 3 call function draw()
                elif matchRes == 3:
                    draw()

# function if player wins
def player_win():
    # declare global variables needed in this function
    global mainmenu_button

    # loads and plays the music needed for this function
    pygame.mixer.music.load('assets/music/victorymusic.mp3')
    pygame.mixer.music.play()

    # loop for this function
    while True:
        # checks for the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # checks if the main menu button of this function is clicked 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+32 <= mouse_pos[1] <= windowy/2+32+48:
                    menu()
        
        # gets the position of the mouse
        mouse_pos = pygame.mouse.get_pos()

        # hover function for the main menu button in this function
        if windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+32 <= mouse_pos[1] <= windowy/2+32+48:
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
        # displays the background continuously
        window.blit(player_win_bg,(0,0))

        # displays the main menu button of this function
        window.blit(mainmenu_button,(windowx/2-64,windowy/2+32))
        
        # updates the display
        pygame.display.update()

# function if the player loses
def player_lose():
    # declare global variables needed in this function
    global mainmenu_button

    # loads and plays the music needed for this function
    pygame.mixer.music.load('assets/music/losemusic.mp3')
    pygame.mixer.music.play()

    # loop for this function
    while True:
        # checks for the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # checks if a certain button in this function is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # checks if the retry button is clicked
                if windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+32 <= mouse_pos[1] <= windowy/2+32+48:
                    main_game()
                
                # checks if the main menu button is clicked 
                elif windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+98 <= mouse_pos[1] <= windowy/2+98+48:
                    menu()

        # gets the position of the mouse
        mouse_pos = pygame.mouse.get_pos()

        # hover function for the buttons in this function
        if (windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+32 <= mouse_pos[1] <= windowy/2+32+48) or (windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+98 <= mouse_pos[1] <= windowy/2+98+48):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
        # displays the background continuously
        window.blit(player_lose_bg,(0,0))

        # displays the buttons in this function
        window.blit(retry_button,(windowx/2-64,windowy/2+32))
        window.blit(mainmenu_button,(windowx/2-64,windowy/2+98))

        # updates the display
        pygame.display.update()

# function if draw
def draw():
    # declare global variables needed in this function
    global mainmenu_button
    
    # loop for this function
    while True:
        # checks for the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # checks if a certain button in this function is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # checks if the retry button is clicked
                if windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+32 <= mouse_pos[1] <= windowy/2+32+48:
                    main_game()
                
                # checks if the main menu button is clicked
                elif windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+98 <= mouse_pos[1] <= windowy/2+98+48:
                    menu()
        
        # gets the position of the mouse
        mouse_pos = pygame.mouse.get_pos()

        # hover function for the buttons in this function
        if (windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+32 <= mouse_pos[1] <= windowy/2+32+48) or (windowx/2-64 <= mouse_pos[0] <= windowx/2-64+128 and windowy/2+98 <= mouse_pos[1] <= windowy/2+98+48):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
        # displays the background continuously
        window.blit(draw_bg,(0,0))

        # displays the buttons in this function
        window.blit(retry_button,(windowx/2-64,windowy/2+32))
        window.blit(mainmenu_button,(windowx/2-64,windowy/2+98))

        # updates the display
        pygame.display.update()

# calls the menu function to start the game
menu()