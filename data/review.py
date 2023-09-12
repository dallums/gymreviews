from dataclasses import dataclass
from typing import Dict
from data.gym import Gym
from data.reviewer import Reviewer

@dataclass
class Review:
    review_id: str
    gym: Gym
    reviewer: Reviewer
    rating_text: str
    cleanlieness: int
    family_friendly: int
    intensity: int
    quality_of_instruction: int
    price: int
    safety: int
    quality_of_training_patners: int
    wamrups: int
    class_availability: int
    welcoming_of_visitors: int
    cliquey: int
    female_friendly: int
    overall: int