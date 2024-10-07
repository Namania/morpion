from game import Game

game = Game()
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
