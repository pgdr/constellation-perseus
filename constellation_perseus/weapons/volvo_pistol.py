class VolvoPistol(Gun):
    ammo: int = 10
    damage_caused: float = 10
    precision: double = 10
    range_: int = 10
    recharge_time: int = 10
    name: str = "My Volvo Pistol"

    def get_damage(self):
        return 0
