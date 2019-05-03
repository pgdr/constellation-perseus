import constellation_perseus as cp
from constellation_perseus import Game


def test_ship_immediate_jump():
    game = Game()
    game.setup()
    ship = cp.ships.ColonialViper(owner=game.get_human_player())
    assert ship.canjump(game.now())


def test_add_ship():
    from constellation_perseus import Stars

    game = Game()
    game.setup()
    ship = cp.ships.ColonialViper(owner=game.get_human_player())
    game.add(ship, Stars.SOL.position)
    assert game.get_position(ship)


def test_ship_jump():
    from constellation_perseus import Stars

    game = Game()
    game.setup()
    ship = cp.ships.ColonialViper(owner=game.get_human_player())
    game.add(ship, Stars.SOL.position)
    assert game.get_position(ship)
    ship.jumpto(Stars.SOL.position, game.now())
    assert game.get_position(ship) == Stars.SOL.position
