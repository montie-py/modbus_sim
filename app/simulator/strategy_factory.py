from app.simulator.strategies import (
    SineWaveStrategy,
    RandomStrategy,
    IncrementStrategy,
    ConstantStrategy,
)

def strategy_factory(name: str, params: dict | None = None):
    name = name.lower()
    params = params or {}

    if name == "sine":
        return SineWaveStrategy(**params)

    if name == "random":
        return RandomStrategy(**params)

    if name == "increment":
        return IncrementStrategy(**params)

    if name == "constant":
        return ConstantStrategy(**params)

    raise ValueError(f"Unknown strategy: {name}")
