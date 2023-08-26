from dataclasses import dataclass
from typing import Dict
from gym import Gym
from reviewer import Reviewer
from rating_category import RatingCategory

@dataclass
class Review:
    gym: Gym
    reviewer: Reviewer
    rating_text: str
    numeric_ratings: Dict[RatingCategory, int]