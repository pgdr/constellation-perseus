"""Every object in the game, including stars, ships and stations.

Can be destroyed, and have a concept of time and position.

@author pgd

"""

from dataclasses import dataclass
from .position import Position
from .gameobjectaction import GameObjectAction
from .players import Player


@dataclass
class GameObject:

    #position: Position  # Deprecated

    def tick(self, time: int):
        """Tick, time is the absolute game time, which might overflow. lol, not!

        @param time the current time in millisecond, since game started.

        """
        pass

    def get_damage(self):
        """Get the damage of this object. 1 means fully operational, 0 means fully
destroyed.

@return the damage of this object, [0,1] where 1 is fully operational, 0 is
        destroyed.

        """
        pass

    def get_possible_actions(self):
        """Get a list of possible actions the object can do.

        @return list of possible actions

        """
        pass

    def is_action_possible(action: GameObjectAction):
        """
          @return boolean whether action is possible or not
        """
        pass

    def name(self) -> str:
        """Some identifier. Every object must provide some identifier

        @return

        """
        pass

    def owner(self) -> Player:
        """Might return null, but if ship or station returns player

        @return

        """
        pass
