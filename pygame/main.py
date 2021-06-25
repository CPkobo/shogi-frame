from gameboad import Game

game = Game()
game.read_csa(csa="./pygame/csa/sample.csa")
# print(game.get_steps())
# print(game.get_figs())
for (step, fig) in zip(game.get_steps(), game.get_pretty_figs()):
    print(step)
    print(fig)
    print("\n\n")
print(game.get_winner())