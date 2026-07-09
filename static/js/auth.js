const API_BASE = "/api";

async function registerUser(event) {

    event.preventDefault();

    const username = document.getElementById("username").value;

    const email = document.getElementById("email").value;

    const password = document.getElementById("password").value;

    const response = await fetch(
        `${API_BASE}/auth/register/`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username,
                email,
                password
            })
        }
    );

    const data = await response.json();

    if (response.ok) {

        alert("Registration successful.");

        window.location.href = "/login/";

    }
    else {

        alert(JSON.stringify(data));

    }

}
async function loginUser(event) {

    event.preventDefault();

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;

    const response = await fetch(
        "/api/auth/login/",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username,
                password
            })
        }
    );

    const data = await response.json();

    if (response.ok) {

        localStorage.setItem(
            "access",
            data.access
        );

        localStorage.setItem(
            "refresh",
            data.refresh
        );

        window.location.href = "/dashboard/";

    }
    else {

        alert(data.detail || "Invalid credentials.");

    }

}
function logoutUser() {

    localStorage.removeItem("access");

    localStorage.removeItem("refresh");

    window.location.href = "/";

}
function handleUnauthorized(response) {

    if (response.status !== 401) {
        return false;
    }

    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    sessionStorage.clear();

    sessionStorage.setItem(
        "session_expired",
        "true"
    );

    window.location.replace("/login/");

    return true;
}
document.addEventListener("DOMContentLoaded", function () {

    const box = document.getElementById("session-message");

    if (
        box &&
        sessionStorage.getItem("session_expired") === "true"
    ) {

        box.innerHTML = `
            <div class="alert alert-warning">
                Your session has expired. Please login again.
            </div>
        `;

        sessionStorage.removeItem("session_expired");
    }

});