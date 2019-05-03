import constellation_perseus as cp
from constellation_perseus import Game, Allotropes, BasicCarbonHarvester


def test_hq_asset():
    game = Game()
    game.setup()
    player = game.get_human_player()
    assert player
    assert player.hq is not None
    hq = player.hq
    harvester = BasicCarbonHarvester()
    harvester.amount = 123
    assert harvester.amount == 123
    assert hq.get_asset(Allotropes.CARBON.value) == 0
    hq.empty(harvester)
    assert hq.get_asset(Allotropes.CARBON.value) == 123
    assert harvester.amount == 0
