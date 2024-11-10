import src.Menu as menu
import src.Gameloop as gl
import src.Entity as en

def main():
    print("hello")
    launchGame = True
    valeur = "error"
    player = None
    while launchGame:
        create_game = False
        load_game = False
        main_menu_choice = True
        while main_menu_choice:
            #menu.clear_console()
            menu.print_main_menu()
            try:
                valeur = int(input())
                if valeur == 1:
                    create_game = True
                    main_menu_choice = False 
                elif valeur == 2:
                    load_game = True
                    main_menu_choice = False
                elif valeur == 3:
                    menu.print_about_msg()
                    gl.press_enter_clear()
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
            if username == None or username == "error":
                return
            player : "en.Human" = gl.create_human(username)
            gl.game_loop(player, gl.Load_or_new.NEW)
        elif load_game == True:
            player = None
            gl.game_loop(player, gl.Load_or_new.LOAD)
        
        
          
main()


