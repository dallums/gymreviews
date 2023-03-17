from flask import Flask, request, jsonify
import DAL

# Create a Flask app
app = Flask(__name__)

dal = DAL.DataBase()
db = dal.get_connection()

# Define a route to handle GET requests
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    # Create a cursor object to execute queries
    cursor = db.cursor()
    # Execute a SELECT query to retrieve all reviews
    cursor.execute("SELECT * FROM reviews")
    # Fetch all results
    results = cursor.fetchall()
    # Convert the results to a list of dictionaries
    reviews = [{'id': row[0], 'title': row[1], 'body': row[2], 'rating': row[3]} for row in results]
    # Return the reviews as JSON
    return jsonify(reviews)

# Define a route to handle POST requests
@app.route('/api/reviews', methods=['POST'])
def post_review():
    # Extract the review data from the request body
    review = request.get_json()
    title = review['title']
    body = review['body']
    rating = review['rating']
    # Create a cursor object to execute queries
    cursor = db.cursor()
    # Execute an INSERT query to insert the review data into the database
    cursor.execute("INSERT INTO reviews (title, body, rating) VALUES (%s, %s, %s)", (title, body, rating))
    # Commit the changes to the database
    db.commit()
    # Return a success message
    return 'Review posted successfully'