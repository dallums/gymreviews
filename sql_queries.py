import random


def generate_get_reviews_by_gym_id_query(gym_id: str) -> str:
     return f"""
            SELECT 
                review_id
                , gym_id
                , gym_name
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
def generate_insert_review_query(gym_name, reviewer_name, rating_text, overall_rating,
                                 cleanliness, family_friendly, intensity, quality_of_instruction,
                                 price, safety, quality_of_training_partners, warmups, class_availability,
                                 welcoming_of_visitors, cliquey, female_friendly):
     print('Generating the query')
     review_id = random.randint(0, 1000)
     gym_id = random.randint(0, 1000)
     return f"""
        INSERT INTO 
            gymreviews.reviews 
        (review_id
        , gym_name
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
        ({review_id}, '{gym_name}', {gym_id}, '{reviewer_name}', '{rating_text}', {overall_rating},
        {cleanliness}, {family_friendly}, {intensity}, {quality_of_instruction},
        {price}, {safety}, {quality_of_training_partners}, {warmups}, {class_availability},
        {welcoming_of_visitors}, {cliquey}, {female_friendly});"""