import constellation_perseus as cp
from constellation_perseus import Game, Allotropes


def test_player_asset():
    game = Game()
    game.setup()
    player = game.get_human_player()
    assert player
    assert player.get_total_selenium() == 0
    assert player.hq is not None
    assert player.get_total_carbon() == 0
    player.hq.add_allotrope(Allotropes.CARBON.value, 17)
    assert player.get_total_carbon() == 17
