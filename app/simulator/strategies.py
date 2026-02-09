import random
import math
from abc import ABC, abstractmethod
from typing import Optional


class BaseStrategy(ABC):
    """Base class for all simulation strategies."""

    @abstractmethod
    def next_value(self, current: Optional[float]) -> float:
        """Return the next simulated value."""
        raise NotImplementedError


class RandomStrategy(BaseStrategy):
    """Produces a random value within a range."""

    def __init__(self, low: float = 0.0, high: float = 100.0):
        self.low = low
        self.high = high

    def next_value(self, current: Optional[float]) -> float:
        return random.uniform(self.low, self.high)


class IncrementStrategy(BaseStrategy):
    """Increases the value by a fixed step."""

    def __init__(self, step: float = 1.0):
        self.step = step

    def next_value(self, current: Optional[float]) -> float:
        if current is None:
            return 0.0
        return current + self.step


class SineWaveStrategy(BaseStrategy):
    """Simulates a smooth oscillating value."""

    def __init__(self, amplitude: float = 10.0, frequency: float = 0.1):
        self.amplitude = amplitude
        self.frequency = frequency
        self._t = 0.0

    def next_value(self, current: Optional[float]) -> float:
        value = self.amplitude * math.sin(self._t)
        self._t += self.frequency
        return value


class ConstantStrategy(BaseStrategy):
    """Always returns the same value."""

    def __init__(self, value: float = 0.0):
        self.value = value

    def next_value(self, current: Optional[float]) -> float:
        return self.value
