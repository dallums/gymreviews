// Get the form element
const form = document.querySelector("#add-review-form");

function addReview() {
    // Get the values from the form inputs
  const gymName = document.getElementById("gymNameSubmitInput").value;
  const gymAddress = document.getElementById("gymAddressSubmitInput").value;
  const reviewerName = document.getElementById("reviewerNameInput").value;
  const ratingText = document.getElementById("ratingTextInput").value;
  const overallRating = document.getElementById("overallRatingInput").value;
  const cleanlinessRating = document.getElementById("cleanlinessRatingInput").value;
  const familyFriendlyRating = document.getElementById("familyFriendlyRatingInput").value;
  const intensityRating = document.getElementById("intensityRatingInput").value;
  const qualityOfInstructionRating = document.getElementById("qualityOfInstructionRatingInput").value;
  const priceRating = document.getElementById("priceRatingInput").value;
  const safetyRating = document.getElementById("safetyRatingInput").value;
  const qualityOfTrainingPartnersRating = document.getElementById("qualityOfTrainingPartnersRatingInput").value;
  const warmupsRating = document.getElementById("warmupsRatingInput").value;
  const classAvailabilityRating = document.getElementById("classAvailabilityRatingInput").value;
  const welcomingOfVisitorsRating = document.getElementById("welcomingOfVisitorsRatingInput").value;
  const cliqueyRating = document.getElementById("cliqueyRatingInput").value;
  const femaleFriendlyRating = document.getElementById("femaleFriendlyRatingInput").value;
  
  review = createReviewObject(gymName, gymAddress, reviewerName, ratingText, overallRating, cleanlinessRating,
    familyFriendlyRating, intensityRating, qualityOfInstructionRating, priceRating, safetyRating,
    qualityOfTrainingPartnersRating, warmupsRating, classAvailabilityRating, welcomingOfVisitorsRating,
    cliqueyRating, femaleFriendlyRating);
  
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
        document.getElementById("gymAddressSubmitInput").value = "";
        document.getElementById("reviewerNameInput").value = "";
        document.getElementById("ratingTextInput").value = "";
        document.getElementById("overallRatingInput").value = "";
        document.getElementById("cleanlinessRatingInput").value = "";
        document.getElementById("familyFriendlyRatingInput").value = "";
        document.getElementById("intensityRatingInput").value = "";
        document.getElementById("qualityOfInstructionRatingInput").value = "";
        document.getElementById("priceRatingInput").value = "";
        document.getElementById("safetyRatingInput").value = "";
        document.getElementById("qualityOfTrainingPartnersRatingInput").value = "";
        document.getElementById("warmupsRatingInput").value = "";
        document.getElementById("classAvailabilityRatingInput").value = "";
        document.getElementById("welcomingOfVisitorsRatingInput").value = "";
        document.getElementById("cliqueyRatingInput").value = "";
        document.getElementById("femaleFriendlyRatingInput").value = "";
        
        // display success message
        alert("Review submitted successfully!");
      } else {
        alert('Error submitting review');
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

  function getReviewsByGymId() {
    var gymId = document.getElementById("gymIdInput").value;
    fetch(`/api/reviews/gym_id/${gymId}`)
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
    var gymAddressCell = document.createElement("td");
    var reviewerNameCell = document.createElement("td");
    var ratingTextCell = document.createElement("td");
    var overallRatingCell = document.createElement("td");
    var cleanlinessCell = document.createElement("td");
    var familyFriendlyCell = document.createElement("td");
    var intensityCell = document.createElement("td");
    var qualityOfInstructionCell = document.createElement("td");
    var priceCell = document.createElement("td");
    var safetyCell = document.createElement("td");
    var qualityOfTrainingPartnersCell = document.createElement("td");
    var warmupsCell = document.createElement("td");
    var classAvailabilityCell = document.createElement("td");
    var welcomingOfVisitorsCell = document.createElement("td");
    var cliqueyCell = document.createElement("td");
    var femaleFriendlyCell = document.createElement("td");

    gymNameCell.textContent = review.gym_name;
    gymAddressCell.textContent = review.gym_address;
    reviewerNameCell.textContent = review.reviewer_name;
    ratingTextCell.textContent = review.rating_text;
    overallRatingCell.textContent = review.overall;
    cleanlinessCell.textContent = review.cleanliness;
    familyFriendlyCell.textContent = review.family_friendly;
    intensityCell.textContent = review.intensity;
    qualityOfInstructionCell.textContent = review.quality_of_instruction;
    priceCell.textContent = review.price;
    safetyCell.textContent = review.safety;
    qualityOfTrainingPartnersCell.textContent = review.quality_of_training_partners;
    warmupsCell.textContent = review.warmups;
    classAvailabilityCell.textContent = review.class_availability;
    welcomingOfVisitorsCell.textContent = review.welcoming_of_visitors;
    cliqueyCell.textContent = review.cliquey;
    femaleFriendlyCell.textContent = review.female_friendly;


    row.appendChild(gymNameCell);
    row.appendChild(gymAddressCell);
    row.appendChild(reviewerNameCell);
    row.appendChild(ratingTextCell);
    row.appendChild(overallRatingCell);
    row.appendChild(cleanlinessCell);
    row.appendChild(familyFriendlyCell);
    row.appendChild(intensityCell);
    row.appendChild(qualityOfInstructionCell);
    row.appendChild(priceCell);
    row.appendChild(safetyCell);
    row.appendChild(qualityOfTrainingPartnersCell);
    row.appendChild(warmupsCell);
    row.appendChild(classAvailabilityCell);
    row.appendChild(welcomingOfVisitorsCell);
    row.appendChild(cliqueyCell);
    row.appendChild(femaleFriendlyCell);

    return row;
  }

  function createReviewObject(gym_name, gym_address, reviewer_name, rating_text, overall, cleanliness,
    family_friendly, intensity, quality_of_instruction, price, safety, quality_of_training_partners,
    warmups, class_availability, welcoming_of_visitors, cliquey, female_friendly) {
    const review = {
        gym_name,
        gym_address,
        reviewer_name,
        rating_text,
        overall,
        cleanliness,
        family_friendly,
        intensity,
        quality_of_instruction,
        price,
        safety,
        quality_of_training_partners,
        warmups,
        class_availability,
        welcoming_of_visitors,
        cliquey,
        female_friendly
    };
    return review;
}
  