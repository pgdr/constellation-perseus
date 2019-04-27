import enum

class GameObjectAction(enum.Enum):
    #
    # build specific {@link Ship}s
    #
    BUILD_SHIP=enum.auto()
    BUILD_COLONIALVIPER=enum.auto()
    BUILD_HQSHIP=enum.auto()

    BUILD_CARBONHARVESTER=enum.auto()
    BUILD_OXYGENHARVESTER=enum.auto()
    BUILD_PHOSPHORUSHARVESTER=enum.auto()
    BUILD_SULFURHARVESTER=enum.auto()
    BUILD_SELENIUMHARVESTER=enum.auto()


    #
    # build specific {@link SpaceStation}s
    #
    BUILD_SPACESTATIONS=enum.auto()
    BUILD_SHIPYARD=enum.auto()


    #
    # build specific {@link Celestial}s
    #
    BUILD_CELESTIALS=enum.auto()
    BUILD_MOON=enum.auto()
    BUILD_STAR=enum.auto()


    #
    # build specific {@link Gun}s
    #
    BUILD_GUNS=enum.auto()
    BUILD_VIPERMISSILE=enum.auto()


    # defensive actions
    DEFEND=enum.auto()
    DEFEND_SHIP=enum.auto()
    DEFEND_STATION=enum.auto()
    DEFEND_CELESTIAL=enum.auto()
    DEFEND_COLONIALVIPER=enum.auto()
    DEFEND_HQSHIP=enum.auto()

    DEFEND_CARBONHARVESTER=enum.auto()
    DEFEND_OXYGENHARVESTER=enum.auto()
    DEFEND_PHOSPHORUSHARVESTER=enum.auto()
    DEFEND_SULFURHARVESTER=enum.auto()
    DEFEND_SELENIUMHARVESTER=enum.auto()


    # aggressive actions
    ATTACK=enum.auto()
    ATTACK_SHIP=enum.auto()
    ATTACK_STATION=enum.auto()
    ATTACK_CELESTIAL=enum.auto()
    ATTACK_COLONIALVIPER=enum.auto()
    ATTACK_HQSHIP=enum.auto()

    ATTACK_CARBONHARVESTER=enum.auto()
    ATTACK_OXYGENHARVESTER=enum.auto()
    ATTACK_PHOSPHORUSHARVESTER=enum.auto()
    ATTACK_SULFURHARVESTER=enum.auto()
    ATTACK_SELENIUMHARVESTER=enum.auto()


    # moods
    PATROL=enum.auto()
    HOLD_GROUND=enum.auto()
    PREEMPTIVE_STRIKE=enum.auto()
    INFILTRATE=enum.auto()
    KAMIKAZE=enum.auto()
    SELF_DESTRUCT=enum.auto()


    # harvesting
    HARVEST=enum.auto()
    HARVEST_OXYGEN=enum.auto()
    HARVEST_CARBON=enum.auto()
    HARVEST_PHOSPHORUS=enum.auto()
    HARVEST_SULFUR=enum.auto()
    HARVEST_SELENIUM=enum.auto()


    # travelling
    TRAVEL=enum.auto()
    SUBLIGHT_TRAVEL=enum.auto()
    INTERSTELLAR_TRAVEL=enum.auto()
