"""Every object in the game, including stars, ships and stations.

Can be destroyed, and have a concept of time and position.

@author pgd

"""

from dataclasses import dataclass, field
from typing import Tuple, List

from .position import Position
from .gameobjectaction import GameObjectAction
from .gameobjectstate import GameObjectState


@dataclass(eq=False)
class GameObject:

    actions: Tuple[GameObjectAction] = tuple()
    state: GameObjectState = GameObjectState.IDLE
    listeners: List = field(default_factory=list)

    # position: Position  # Deprecated

    def tick(self, now: int):
        """Tick, now is the absolute game time, which might overflow.

        @param now the current time in millisecond, since game started.

        """

    def assign_position(self, pos: Position, now: int):
        for listener in self.listeners:
            listener.dispatch(GameObjectState.JUMPING, {"position": pos})

    def get_damage(self):
        """Get the damage of this object. 1 means fully operational, 0 means fully
        destroyed.

        @return the damage of this object, [0,1] where 1 is fully operational, 0
        is destroyed.

        """

    def get_possible_actions(self):
        """Get a list of possible actions the object can do.

        @return list of possible actions

        """

    def is_action_possible(self, action: GameObjectAction):
        """
          @return boolean whether action is possible or not
        """

    def name(self) -> str:
        """Some identifier. Every object must provide some identifier

        @return

        """

    def owner(self):
        """Might return null, but if ship or station returns player

        @return

        """
