import random
from data.review import Review


def generate_get_reviews_by_gym_id_query(gym_id: str) -> str:
     return f"""
            SELECT 
                review_id
                , gym_id
                , gym_name
                , gym_address
                , reviewer_name
                , rating_text
                , overall
                , cleanliness
                , family_friendly
                , intensity
                , quality_of_instruction
                , price
                , safety
                , quality_of_training_partners
                , warmups
                , class_availability
                , welcoming_of_visitors
                , cliquey
                , female_friendly
            FROM 
                gymreviews.reviews 
            WHERE 
                reviews.gym_id = '{gym_id}'
        """

def generate_get_reviews_by_gym_name_query(gym_name: str) -> str:
     return f"""
            SELECT 
                review_id
                , gym_id
                , gym_name
                , gym_address
                , reviewer_name
                , rating_text
                , overall
                , cleanliness
                , family_friendly
                , intensity
                , quality_of_instruction
                , price
                , safety
                , quality_of_training_partners
                , warmups
                , class_availability
                , welcoming_of_visitors
                , cliquey
                , female_friendly
            FROM 
                gymreviews.reviews 
            WHERE 
                reviews.gym_name = '{gym_name}'
        """

def generate_get_all_reviews_query() -> str:
     return f"""
            SELECT 
                review_id
                , gym_id
                , gym_name
                , gym_address
                , reviewer_name
                , rating_text
                , overall
                , cleanliness
                , family_friendly
                , intensity
                , quality_of_instruction
                , price
                , safety
                , quality_of_training_partners
                , warmups
                , class_availability
                , welcoming_of_visitors
                , cliquey
                , female_friendly
            FROM 
                gymreviews.reviews
            ORDER BY
                gym_name ASC
        """

# TODO: generate gym id and review id intelligently
def generate_insert_review_query(review: Review) -> str:
     print('Generating the query')

     gym_id = random.randint(0, 1000)
     gym_name = review.gym_name
     gym_address = review.gym_address
     reviewer_name = review.reviewer_name
     rating_text = review.rating_text
     overall_rating = review.overall
     cleanliness = review.cleanliness
     family_friendly = review.family_friendly
     intensity = review.intensity
     quality_of_instruction = review.quality_of_instruction
     price = review.price
     safety = review.safety
     quality_of_training_partners = review.quality_of_training_partners
     warmups = review.warmups
     class_availability = review.class_availability
     welcoming_of_visitors = review.welcoming_of_visitors
     cliquey = review.cliquey
     female_friendly = review.female_friendly 

     return f"""
        INSERT INTO 
            gymreviews.reviews 
        (gym_name
        , gym_address
        , gym_id
        , reviewer_name 
        , rating_text
        , overall
        , cleanliness
        , family_friendly
        , intensity
        , quality_of_instruction
        , price
        , safety
        , quality_of_training_partners
        , warmups
        , class_availability
        , welcoming_of_visitors
        , cliquey
        , female_friendly) 
        VALUES 
        ('{gym_name}', '{gym_address}', {gym_id}, '{reviewer_name}', '{rating_text}', {overall_rating},
        {cleanliness}, {family_friendly}, {intensity}, {quality_of_instruction},
        {price}, {safety}, {quality_of_training_partners}, {warmups}, {class_availability},
        {welcoming_of_visitors}, {cliquey}, {female_friendly});"""