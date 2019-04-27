"""This class controls the main logic behind the game, and keeps complete lists
  for the main objects in this game: players, celestials and ships.

@author pgd

"""

from . import Player


class Game:
    initialize_time: int
    players: list[Player] = []
    celestials: list[Celestial] = []
    ships: list[Ship] = []
    stations: list[Spacestation] = []
    contributors: list[str] = []
    soundsystem: Soundsystem = Soundsystem.get_sound_system()

    pos_to_obj: dict[Position, GameObject] = {}
    obj_to_pos: dict[GameObject, Position] = {}

    is_instantiated: bool = False

    instance: Game

    def __init__(self):
        self._setup()

    def setup(self):
        human = HumanPlayer()
        harkonnen = Harkonnen()
        players = [human, harkonnen]

        add = self.add_game_object
        add(Star.SOL)

        add(Star.ALCYONE)
        add(Star.ATLAS)
        add(Star.ELECTRA)
        add(Star.MAIA)
        add(Star.MEROPE)

        add(Star.TAYGETA)
        add(Star.PLEIONE)
        add(Star.CELAENO)
        add(Star.STEROPE)
        add(Star.ASTEROPE)

        hqship = Hq("HeadQuarter", self.get_position(Star.SOL), human)
        human.add_hq(hq)
        add(hq)
        hq.star = Star.SOL

        yard = Shipyard(hq.position.add(Position(0, 50, 0)), hq, human)
        add(yard)

        self.set_contributors()

        for i in range(6):
            v = ColonialViper(Star.ELECTRA.position, human)
            add(v)

        harkonnen_hq = Hq("Harkonnen", Star.PLEIONE.position, harkonnen)
        harkonnen.add_hq(harkonnenHq)
        add(harkonnenHq)
        harkonnen_hq.star = Star.PLEIONE

        def get_human_player(self):
            return players.get(0)

        def buy(self, ship: Ship, player: Player):
            """ Returns true if player can afford to buy ship AND the money is withdrawn
            from the Hq's assets!"""
            hq = player.hq
            return hq.buy(ship)

        def now(self) -> int:
            """
   Returns the current time in milliseconds relative to when the game
   started, i.e. it will be 0 immediately when the game starts.
"""

            n = time.time()
            return n - initialize_time

        # @icontract...
        def sendShipToCelestial(self, ship: Ship, cel: Celestial) -> Position:
            """"
            Returns None if ship not ready to jump
"""
            if not ship.isReadyToJump():
                return

            ship.jumpto(objToPos[cel])
            return self.assign_position(ship, objToPos[cel])

        def assign_position(self, obj: GameObject, pos: Position) -> Position:
            """
   Finds the nearest uninhabitated position in space and puts obj there.
   This method calls setPosition on obj with the position it returns.
   Returns the position it was moved to.
"""
            with asyncio.lock():
                if obj in objToPos:
                    oldpos = objToPos[obj]
                    if oldPos == position:
                        return position  # nothing to do
                    obj_to_pos[obj] = pos
                    pos_to_obj[oldpos] = None
                    pos_to_obj[pos] = obj

        def get_position(self, obj: GameObject) -> Position:
            return obj_to_pos.get(obj)

        # @singledispatch
        def add(self, obj: GameObject):
            if isinstance(obj, Ship):
                ships.add(obj)
            elif isinstance(obj, Celestial):
                celestials.add(obj)
            elif isinstance(obj, Spacestation):
                stations.add(obj)

            self.assign_position(obj, obj.position)

        def getObject(self, target: Position, range_: float) -> GameObject:
            """Returns the object closest to given position. Returns null if no object is
            closer than range.

            """

            with asyncio.lock():
                opt_dist = 10 ** 10
                opt_obj = None
                opt_pos = None
                for pos, obj in self.pos_to_obj.items:
                    dist = target.distance(pos)
                    if dist < optDist:
                        opt_obj = obj
                        opt_pos = pos
                        opt_dist = dist

            if optDist > range_:
                return None

            return opt_obj

    def tick(self):
        def T(o):
            o.tick(self.now())

        with asyncio.lock():
            for obj in players + celestials + stations + ships:
                T(obj)

    def __str__(self):
        def ntjoin(lst, header=""):
            return header + "\n\t".join([str(obj) for obj in lst])

        return (
            ntjoin(players, "Players:")
            + ntjoin(celestials, "Celestials:")
            + ntjoin(stations, "Stations:")
            + ntjoin(ships, "Ships:")
        )

    def set_contributors(self):
        self.contributors = ["Jonas Grønås Drange", "Pål Grønås Drange"]
