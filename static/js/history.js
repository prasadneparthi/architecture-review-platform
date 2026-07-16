document.addEventListener(
    "DOMContentLoaded",
    loadHistory
);

async function loadHistory() {

    const token =
        localStorage.getItem("access");
    if (!token){
        handleUnauthorized({
            status: 401
        });

    return;
    }

    const response =
        await fetch(
            "/api/history/reviews/",
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        );
    if (handleUnauthorized(response)) {
        return;
}

    const reviews =
        await response.json();
    
    if (reviews.length === 0) {

    document.getElementById("history-table").innerHTML = `

        <div class="alert alert-info">

            No reviews found.

        </div>

    `;

    return;

}
    let html = `

<table class="table table-striped">

<thead>

<tr>

<th>System</th>
<th>Score</th>
<th>Date</th>
<th>Actions</th>

</tr>

</thead>

<tbody>

`;

    reviews.forEach(function(review){

        html += `

<tr>

<td>${review.system_name}</td>

<td>${review.review_result.overall_score}</td>

<td>${new Date(review.created_at).toLocaleDateString()}</td>

<td>

<button
class="btn btn-sm btn-primary"
onclick="viewReview('${review.review_id}')">

View

</button>

<button
class="btn btn-sm btn-success"
onclick="downloadPdf('${review.review_id}')">

PDF

</button>

<button
class="btn btn-sm btn-danger"
onclick="deleteReview('${review.review_id}')">

Delete

</button>

</td>

</tr>

`;

    });

    html += `

</tbody>

</table>

`;

    document.getElementById(
        "history-table"
    ).innerHTML = html;

}
async function viewReview(reviewId) {

    const token = localStorage.getItem("access");
    if (!token) {

        handleUnauthorized({
            status: 401
    });

    return;
    }

    const response = await fetch(
        `/api/history/reviews/${reviewId}/`,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );
    if (handleUnauthorized(response)) {
        return;
}

    if (!response.ok) {

        alert("Unable to load review.");

        return;
    }

    const review = await response.json();

    const report = {
        ...review.review_result,
        review_id: review.review_id
    };

    sessionStorage.setItem(
        "review_result",
        JSON.stringify(report)
    );

    window.location.href = "/review/result/?from=history";
}
async function deleteReview(reviewId) {

    if (!confirm("Delete this review?")) {

        return;
    }

    const token = localStorage.getItem("access");
    if (!token) {

        handleUnauthorized({
            status: 401
    });

    return;
}

    const response = await fetch(

        `/api/history/reviews/${reviewId}/`,

        {
            method: "DELETE",

            headers: {
                Authorization: `Bearer ${token}`
            }
        }

    );
    if (handleUnauthorized(response)) {
        return;
}
      

    if (!response.ok) {

        alert("Unable to delete review.");

        return;
    }

    loadHistory();

}
async function downloadPdf(reviewId) {

    const token = localStorage.getItem("access");
    if (!token) {

        handleUnauthorized({
            status: 401
    });

    return;
}

    const response = await fetch(

        `/api/pdf/reviews/${reviewId}/pdf/`,

        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }

    );
    if (handleUnauthorized(response)) {
        return;
    }

    if (!response.ok) {

        alert("Unable to download PDF.");

        return;
    }

    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "ArchitectureReview.pdf";

    a.click();

    window.URL.revokeObjectURL(url);

}