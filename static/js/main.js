function getReviewsByGymName() {
    var gymName = document.getElementById("gym-name-input").value;
    fetch(`/api/reviews/gym_name/${gymName}`)
      .then((response) => response.json())
      .then((data) => {
        var table = document.getElementById("reviews-table");
        table.innerHTML = "";
        data.forEach((review) => {
          table.appendChild(createReviewRow(review));
        });
      });
  }
  
  function getAllReviews() {
    fetch("/api/reviews")
      .then((response) => response.json())
      .then((data) => {
        var table = document.getElementById("reviews-table");
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
  