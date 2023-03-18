from flask import Flask, request, jsonify, render_template
import DAL

# Create a Flask app
app = Flask(__name__)

dal = DAL.DataBase()
db = dal.get_connection()

# Define the home page
@app.route('/')
def home():
    return render_template('index.html')

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
    # Create a cursor object to execute queries
    cursor = db.cursor()
    # Execute a SELECT query to retrieve all reviews
    cursor.execute(f"SELECT * FROM gym_reviews WHERE gym_reviews.gym_name = '{gym_name}'")
    # Fetch all results
    results = cursor.fetchall()
    # Convert the results to a list of dictionaries
    reviews = [{'gym_name': row[1], 'reviewer_name': row[2], 'review_text': row[3], 'rating': row[4]} for row in results]
    # Return the reviews as JSON
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

if __name__ == '__main__':
    app.run()
