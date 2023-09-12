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