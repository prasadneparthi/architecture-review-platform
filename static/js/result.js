const review = JSON.parse(
    sessionStorage.getItem("review_result")
);

const report = document.getElementById("report");


let scoreLabel = "Needs Improvement";

if (review.overall_score >= 90) {

    scoreLabel = "Excellent";

}
else if (review.overall_score >= 75) {

    scoreLabel = "Good";

}
else if (review.overall_score >= 60) {

    scoreLabel = "Fair";

}

report.innerHTML = `

<div class="card shadow-sm mb-4">

    <div class="card-body">

        <div class="row align-items-center">

            <div class="col-md-8">

                <h3>

                    ${review.system_name}

                </h3>

                <table class="table table-borderless mt-3">

                    <tr>

                        <td width="180">
                            <strong>Review ID</strong>
                        </td>

                        <td>
                            ${review.review_id}
                        </td>

                    </tr>

                    <tr>

                        <td>
                            <strong>Overall Rating</strong>
                        </td>

                        <td>
                            ${scoreLabel}
                        </td>

                    </tr>

                </table>

            </div>

            <div class="col-md-4 text-center">

                <h1 class="display-2 fw-bold">

                    ${review.overall_score}

                </h1>

                <div class="progress mt-3" style="height:12px;">

                    <div
                        class="progress-bar"
                        role="progressbar"
                        style="width:${review.overall_score}%"
                        aria-valuenow="${review.overall_score}"
                        aria-valuemin="0"
                        aria-valuemax="100">

                    </div>

                </div>

                <small class="text-muted">

                    Overall Score

                </small>

            </div>

        </div>

    </div>

</div>

<div id="category-section"></div>

<div id="strength-section"></div>

<div id="weakness-section"></div>

<div id="recommendation-section"></div>

<div id="llm-section"></div>

`;
const categorySection =
    document.getElementById("category-section");

let categoryRows = "";

for (const category in review.category_scores) {

    categoryRows += `

        <tr>

            <td>${category}</td>

            <td class="text-end">

                ${review.category_scores[category]}

            </td>

        </tr>

    `;
}

categorySection.innerHTML = `

<div class="card shadow-sm mb-4">

    <div class="card-header">

        <h5 class="mb-0">

            Category Scores

        </h5>

    </div>

    <div class="card-body">

        <table class="table">

            <thead>

                <tr>

                    <th>Category</th>

                    <th class="text-end">Score</th>

                </tr>

            </thead>

            <tbody>

                ${categoryRows}

            </tbody>

        </table>

    </div>

</div>

`;
const strengthSection =
    document.getElementById("strength-section");

let strengthItems = "";

review.strengths.forEach(function (strength) {

    strengthItems += `

        <li class="list-group-item">

            ${strength}

        </li>

    `;

});

strengthSection.innerHTML = `

<div class="card shadow-sm mb-4">

    <div class="card-header">

        <h5 class="mb-0">

            Strengths

        </h5>

    </div>

    <div class="card-body p-0">

        <ul class="list-group list-group-flush">

            ${strengthItems}

        </ul>

    </div>

</div>

`;
const weaknessSection =
    document.getElementById("weakness-section");

let weaknessItems = "";

if (review.weaknesses.length === 0) {

    weaknessItems = `

        <li class="list-group-item">

            No weaknesses detected.

        </li>

    `;

}
else {

    review.weaknesses.forEach(function (weakness) {

        weaknessItems += `

            <li class="list-group-item">

                ${weakness}

            </li>

        `;

    });

}

weaknessSection.innerHTML = `

<div class="card shadow-sm mb-4">

    <div class="card-header">

        <h5 class="mb-0">

            Weaknesses

        </h5>

    </div>

    <div class="card-body p-0">

        <ul class="list-group list-group-flush">

            ${weaknessItems}

        </ul>

    </div>

</div>

`;
const recommendationSection =
    document.getElementById("recommendation-section");

if (review.recommendations.length === 0) {

    recommendationSection.innerHTML = `

    <div class="card shadow-sm mb-4">

        <div class="card-header">

            <h5 class="mb-0">

                Recommendations

            </h5>

        </div>

        <div class="card-body">

            No recommendations.

        </div>

    </div>

    `;

}
else {

    let recommendationItems = "";

    review.recommendations.forEach(function (recommendation) {

        recommendationItems += `

            <li class="list-group-item">

                ${recommendation.description}

            </li>

        `;

    });

    recommendationSection.innerHTML = `

    <div class="card shadow-sm mb-4">

        <div class="card-header">

            <h5 class="mb-0">

                Recommendations

            </h5>

        </div>

        <div class="card-body p-0">

            <ol class="list-group list-group-numbered list-group-flush">

                ${recommendationItems}

            </ol>

        </div>

    </div>

    `;

}
const llmSection =
    document.getElementById("llm-section");

llmSection.innerHTML = `

<div class="card shadow-sm mb-4">

    <div class="card-header">

        <h5 class="mb-0">

            AI Analysis

        </h5>

    </div>

    <div class="card-body">

        <p class="mb-0">

            ${
                review.llm_analysis ||
                "AI analysis was not generated."
            }

        </p>

    </div>

</div>

<div id="action-section"></div>

`;
const actionSection =
    document.getElementById("action-section");

actionSection.innerHTML = `

<div class="d-flex justify-content-between mb-5">

    <a
        href="/dashboard/"
        class="btn btn-secondary"
    >
        Back to Dashboard
    </a>

    <a
        href="/review/new/"
        class="btn btn-primary"
    >
        New Review
    </a>

    <button
        class="btn btn-success"
        onclick="downloadPdf()"
    >
        Download PDF
    </button>

</div>

`;
async function downloadPdf() {

    const token =
        localStorage.getItem("access");
        if (!token) {

        handleUnauthorized({
            status: 401
    });

    return;
}

    const reviewId =
        review.review_id;

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

    const blob =
        await response.blob();

    const url =
        window.URL.createObjectURL(blob);

    const a =
        document.createElement("a");

    a.href = url;

    a.download = `${review.system_name}_review.pdf`;

    a.click();

    window.URL.revokeObjectURL(url);

}