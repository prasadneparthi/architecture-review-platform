document.addEventListener(
    "DOMContentLoaded",
    loadDashboard
);

async function loadDashboard() {

    const token = localStorage.getItem("access");

    if (!token) {

        handleUnauthorized({status: 401});

        return;

    }

    const response = await fetch(
        "/api/dashboard/",
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );
    if (handleUnauthorized(response)) {
        return;
    }

    const data = await response.json();

    document.getElementById("total-reviews").textContent =
        data.total_reviews;

    document.getElementById("average-score").textContent =
        data.average_score;

    document.getElementById("latest-review").textContent =
        data.latest_review;

}