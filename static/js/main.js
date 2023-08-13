// Get the form element
const form = document.querySelector("#add-review-form");

// Add an event listener to the form's submit event
form.addEventListener("submit", function (event) {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the values from the form inputs
  const gymName = document.querySelector("#gym-name-input").value;
  const reviewerName = document.querySelector("#reviewer-name-input").value;
  const reviewText = document.querySelector("#review-text-input").value;
  const rating = document.querySelector("#rating-input").value;

  // Create a new review object
  const review = {
    gym_name: gymName,
    reviewer_name: reviewerName,
    review_text: reviewText,
    rating: rating,
  };

  // Call the addReview function with the review object as the argument
  addReview(review);
});

function addReview() {
    const gymName = document.getElementById("gymNameSubmitInput").value;
    const reviewerName = document.getElementById("reviewerNameInput").value;
    const reviewText = document.getElementById("reviewTextInput").value;
    const rating = document.getElementById("ratingInput").value;
    
    const review = {
      gym_name: gymName,
      reviewer_name: reviewerName,
      review_text: reviewText,
      rating: rating
    };
    
    fetch('/api/reviews', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(review)
    })
    .then(response => {
      if (response.ok) {
        // clear the form fields
        document.getElementById("gymNameSubmitInput").value = "";
        document.getElementById("reviewerNameInput").value = "";
        document.getElementById("reviewTextInput").value = "";
        document.getElementById("ratingInput").value = "";
        
        // display success message
        alert("Review submitted successfully!");
      } else {
        alert("Error submitting review.");
      }
    });
  }
  


function getReviewsByGymName() {
    var gymName = document.getElementById("gymNameInput").value;
    fetch(`/api/reviews/gym_name/${gymName}`)
      .then((response) => response.json())
      .then((data) => {
        var table = document.getElementById("reviewsTable");
        table.innerHTML = "";
        data.forEach((review) => {
          table.appendChild(createReviewRow(review));
        });
      });
  }
  
  function getAllReviews() {
    fetch(`/api/reviews`)
      .then((response) => response.json())
      .then((data) => {
        var table = document.getElementById("reviewsTable");
        table.innerHTML = "";
        data.forEach((review) => {
          table.appendChild(createReviewRow(review));
        });
      });
  }
  
  function createReviewRow(review) {
    var row = document.createElement("tr");
    var gymNameCell = document.createElement("td");
    var reviewerNameCell = document.createElement("td");
    var reviewTextCell = document.createElement("td");
    var ratingCell = document.createElement("td");
    gymNameCell.textContent = review.gym_name;
    reviewerNameCell.textContent = review.reviewer_name;
    reviewTextCell.textContent = review.review_text;
    ratingCell.textContent = review.rating;
    row.appendChild(gymNameCell);
    row.appendChild(reviewerNameCell);
    row.appendChild(reviewTextCell);
    row.appendChild(ratingCell);
    return row;
  }
  