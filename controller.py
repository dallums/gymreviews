from typing import Dict, List
from flask import Flask, request, jsonify, render_template
import DAL
from sql_queries import generate_get_reviews_by_gym_id_query

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

# TODO: create necessary tables and refactor to take into account dataclasses instead of the garbage below
# TODO: add SQL injection protection

# Define a route to handle GET requests
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    # Create a cursor object to execute queries
    cursor = db.cursor()
    # Execute a SELECT query to retrieve all reviews
    cursor.execute("SELECT * FROM gym_reviews")
    # Fetch all results
    results = cursor.fetchall()
    # Convert the results to a list of dictionaries
    reviews = [{'gym_name': row[1], 'reviewer_name': row[2], 'review_text': row[3], 'rating': row[4]} for row in results]
    # Return the reviews as JSON
    return jsonify(reviews)

@app.route('/api/reviews/gym_name/<gym_name>', methods=['GET'])
def get_reviews_by_gym_name(gym_name):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM gym_reviews WHERE gym_reviews.gym_name = '{gym_name}'")
    results = cursor.fetchall()
    reviews = [{'gym_name': row[1], 'reviewer_name': row[2], 'review_text': row[3], 'rating': row[4]} for row in results]
    return jsonify(reviews)

@app.route('/api/reviews/gym_id/<gym_id>', methods=['GET'])
def get_reviews_by_gym_id(gym_id):
    cursor = db.cursor()
    print('\n Cursor established \n')
    cursor.execute(generate_get_reviews_by_gym_id_query(gym_id))
    print('\n Query sent \n')
    results = cursor.fetchall()
    print('\n Results fetched \n')
    reviews = [_create_review_from_returned_list_as_dict(row) for row in results]
    print(reviews)
    return jsonify(reviews)

# Define a route to handle POST requests
@app.route('/api/reviews', methods=['POST'])
def post_review():
    # Extract the review data from the request body
    review = request.get_json()
    gym_name = review['gym_name']
    reviewer_name = review['reviewer_name']
    review_text = review['review_text']
    rating = review['rating']
    # Create a cursor object to execute queries
    cursor = db.cursor()
    # Execute an INSERT query to insert the review data into the database
    cursor.execute("INSERT INTO gym_reviews (gym_name, reviewer_name, review_text, rating) VALUES (%s, %s, %s, %s)",
                   (gym_name, reviewer_name, review_text, rating))
    # Commit the changes to the database
    db.commit()
    # Return a success message
    return f'Review posted successfully! {gym_name}'

def _create_review_from_returned_list_as_dict(result: List[str]) -> Dict[str, str]:
    #{'gym_name': row[1], 'reviewer_name': row[2],
    return {
    'review_id' : result[0],
    'gym.gym_id' : result[1],
    'gym.gym_name' : result[2],
    'reviewer.reviewer_name' : result[3],
    'rating_text' : result[4],
    'overall' :result[5],
    'cleanlieness' : result[6],
    'family_friendly' : result[7],
    'intensity' : result[8],
    'quality_of_instruction' : result[9],
    'price' : result[10],
    'safety' : result[11],
    'quality_of_training_patners' : result[12],
    'wamrups' : result[13],
    'class_availability' : result[14],
    'welcoming_of_visitors' : result[15],
    'cliquey' : result[16],
    'female_friendly' : result[17]
    }


if __name__ == '__main__':
    app.run()
