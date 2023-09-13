from typing import Dict, List
from flask import Flask, request, jsonify, render_template
import DAL
from data.review import Review
from data.gym import Gym
from sql_queries import generate_get_all_reviews_query, generate_get_reviews_by_gym_id_query, generate_get_reviews_by_gym_name_query, generate_insert_review_query

# Create a Flask app
app = Flask(__name__)

dal = DAL.DataBase()
db = dal.get_connection()

# Define the home page
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/add_review.html')
def add_review():
    return render_template('add_review.html')

# TODO: add SQL injection protection
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    cursor = db.cursor()
    cursor.execute(generate_get_all_reviews_query())
    results = cursor.fetchall()
    reviews = [_create_review_from_returned_list_as_dict(row) for row in results]
    return jsonify(reviews)

@app.route('/api/reviews/gym_name/<gym_name>', methods=['GET'])
def get_reviews_by_gym_name(gym_name):
    cursor = db.cursor()
    cursor.execute(generate_get_reviews_by_gym_name_query(gym_name))
    results = cursor.fetchall()
    reviews = [_create_review_from_returned_list_as_dict(row) for row in results]
    return jsonify(reviews)

@app.route('/api/reviews/gym_id/<gym_id>', methods=['GET'])
def get_reviews_by_gym_id(gym_id):
    cursor = db.cursor()
    cursor.execute(generate_get_reviews_by_gym_id_query(gym_id))
    results = cursor.fetchall()
    reviews = [_create_review_from_returned_list_as_dict(row) for row in results]
    return jsonify(reviews)

# TODO: clean this up - pass a Review object and parse json better
# TODO: figure out why this endpoint is not working
@app.route('/api/reviews', methods=['POST'])
def post_review():
    print('Endpoint called!')
    review = request.get_json()
    print(f'Request: {request}')
    print('JSON parsed')
    print(review)
    gym_name = review['gym_name']
    reviewer_name = review['reviewer_name']
    rating_text = review['rating_text']
    overall_rating = review['overall_rating']
    cleanliness = review['cleanliness']
    family_friendly = review['family_friendly']
    intensity = review['intensity']
    quality_of_instruction = review['quality_of_instruction']
    price = review['price']
    safety = review['safety']
    quality_of_training_partners = review['quality_of_training_partners']
    warmups = review['warmups']
    class_availability = review['class_availability']
    welcoming_of_visitors = review['welcoming_of_visitors']
    cliquey = review['cliquey']
    female_friendly = review['female_friendly'] 
    print('Estbalishing cursor')
    cursor = db.cursor()
    cursor.execute(generate_insert_review_query(gym_name, reviewer_name, rating_text, overall_rating,
                                                    cleanliness, family_friendly, intensity, quality_of_instruction,
                                                    price, safety, quality_of_training_partners, warmups, class_availability,
                                                    welcoming_of_visitors, cliquey, female_friendly))
    db.commit()
    return 'Review posted successfully!'

def _create_review_from_returned_list_as_dict(result: List[str]) -> Dict[str, str]:
    return {
    'review_id' : result[0],
    'gym_id' : result[1],
    'gym_name' : result[2],
    'reviewer_name' : result[3],
    'rating_text' : result[4],
    'overall' :result[5],
    'cleanliness' : result[6],
    'family_friendly' : result[7],
    'intensity' : result[8],
    'quality_of_instruction' : result[9],
    'price' : result[10],
    'safety' : result[11],
    'quality_of_training_partners' : result[12],
    'warmups' : result[13],
    'class_availability' : result[14],
    'welcoming_of_visitors' : result[15],
    'cliquey' : result[16],
    'female_friendly' : result[17]
    }


if __name__ == '__main__':
    app.run()
