from dataclasses import dataclass
from gym_type import GymType

@dataclass
class Gym:
    gym_id: int
    gym_name: str
    gym_type: GymType