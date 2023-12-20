from game import GameLogic


class Menu:
    def __init__(self) -> None:
        self.game = GameLogic()
                          
    def display_menu(self)->None:
        while True:
            print("""Welcome to Python Quizz!
(1)Start
(2)Leaderboard
(0)Exit""")
            try:
                self.option = int(input("Your choice: "))
                print()
                if self.option not in [0,1,2]:
                    raise ValueError("Unknown option.")
                if self.option == 1:
                    self.game.game_play()
                    self.game.get_result()
                    print()
                    self.game.insert_data()
                    print()
                elif self.option == 2:
                    self.game.leader_board()
                    print()
                elif self.option == 0:
                    print("Exiting program.")
                    break
            except ValueError:
                print("Unknown option. Try again.")
                print()

                
            
        
