from dataclasses import dataclass

@dataclass
class Review:
    gym_name: str
    gym_address: str
    reviewer_name: str
    rating_text: str
    cleanliness: int
    family_friendly: int
    intensity: int
    quality_of_instruction: int
    price: int
    safety: int
    quality_of_training_partners: int
    warmups: int
    class_availability: int
    welcoming_of_visitors: int
    cliquey: int
    female_friendly: int
    overall: int
    review_id: str = '-1'