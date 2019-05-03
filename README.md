# constellation-perseus [![Build Status](https://travis-ci.org/pgdr/constellation-perseus.svg?branch=master)](https://travis-ci.org/pgdr/constellation-perseus)

Mark I Colonial Viper, equipped with kinetic energy weapons and conventional missiles


## Contract-driven Game development

We are using [`icontract`](https://pypi.org/project/icontract/) for
contract driven development, where we can specify **class invariants**
with `icontract.invariant`:

```python
import icontract

@icontract.invariant(lambda self: 0 <= self.damage <= 1))
@dataclass(eq=False)
class Ship(GameObject):
    owner: Player
    damage: float = 1.0
```

**pre-conditions** with `icontract.require`:

```python
@icontract.require(lambda obj: isinstance(obj, GameObject))
@icontract.require(lambda pos: isinstance(pos, Position))
def assign_position(self, obj: GameObject, pos: Position) -> Position:
    pass
```



and **post-conditions** with `icontract.ensure`:

```python
@icontract.ensure(lambda result: isinstance(result, Position))
def add(self, obj: GameObject, pos: Position = None, ...):
    ...
```
