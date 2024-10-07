from game import Game

def main():

    want_play_again = True
    game = Game()

    while want_play_again:

        while game.isRunning():

            game.switch()
            game.display()

            if not game.place(game.pos()):
                game.switch()
            else:
                winner = game.hasWinner()
                if winner is not None:
                    winner.set("score", winner.get("score") + 1)
                    game.end(winner)
                elif game.isFinish():
                    game.end()
        
        game.display_score()
        want_play_again = input("Do you want to play again ? (y or n): ") == "y"
        if want_play_again:
            game = Game(game.get("players"))
        else:
            exit(0)

if __name__ == "__main__":
    main()
