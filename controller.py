import sys
from typing import Dict, List
from flask import Flask, request, jsonify, render_template
import DAL
from data.review import Review
from authorizer import AuthorizationError, Authorizer, SMSAuthorizer
from sql_queries import (
    generate_get_all_reviews_query, 
    generate_get_reviews_by_gym_id_query, 
    generate_get_reviews_by_gym_name_query,
    generate_insert_review_query)

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

@app.route('/api/reviews', methods=['POST'])
def post_review():
    # Would be nice to inject this
    authorizer = SMSAuthorizer()
    try:
        authorizer.authorize()
        review = request.get_json()
        new_review = Review(**review)
        cursor = db.cursor()
        cursor.execute(generate_insert_review_query(new_review))
        db.commit()
        return 'Review posted successfully!'
    except AuthorizationError as e:
        print(f'Exception: {e}', file=sys.stderr)
        return str(e), 401

def _create_review_from_returned_list_as_dict(result: List[str]) -> Dict[str, str]:
    return {
    'review_id' : result[0],
    'gym_id' : result[1],
    'gym_name' : result[2],
    'gym_address': result[3],
    'reviewer_name' : result[4],
    'rating_text' : result[5],
    'overall' :result[6],
    'cleanliness' : result[7],
    'family_friendly' : result[8],
    'intensity' : result[9],
    'quality_of_instruction' : result[10],
    'price' : result[11],
    'safety' : result[12],
    'quality_of_training_partners' : result[13],
    'warmups' : result[14],
    'class_availability' : result[15],
    'welcoming_of_visitors' : result[16],
    'cliquey' : result[17],
    'female_friendly' : result[18]
    }


if __name__ == '__main__':
    # Default port from flask is 5000
    app.run()
