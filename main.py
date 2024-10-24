import src.Menu as menu
import src.Gameloop as gl
def main():
    print("hello")
    
      
    main_menu_choice = True
    valeur = "error"
    create_game = False
    load_game = False
    about_page = False
    player = None
    while main_menu_choice:
        menu.print_main_menu()
        try:
            valeur = int(input())
            if valeur == 1:
                create_game = True
                main_menu_choice = False
                break
            elif valeur == 2:
                load_game = True
                #load_game()
                main_menu_choice = False
                break
            elif valeur == 3:
                about_page = True
                #print_about_page()
                main_menu_choice = False
                break
            elif valeur == 4 :
                launchGame = False
                main_menu_choice = False
                break
            else:
                print("please input a correct number between 1 and 4 :")
        except ValueError:
            print("please input a correct number between 1 and 4 :")
            input("press Enter to continue")
    
    if create_game == True:
        username = gl.create_username()
        if username == None:
            return
        player = gl.create_human(username)
    
        gl.game_loop(player, gl.Load_or_new.NEW)
    
        

main()


