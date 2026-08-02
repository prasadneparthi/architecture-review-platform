document.addEventListener("DOMContentLoaded", function () {

    const token = localStorage.getItem("access");

    const navbar =
        document.getElementById("navbar-links");

    if (token) {

        navbar.innerHTML = `
            <li class="nav-item">
                <a class="nav-link" href="/dashboard/">
                    Dashboard
                </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/history/">
                    History
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/account/">
                    Account
                </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="#" onclick="logoutUser()">
                    Logout
                </a>
            </li>
        `;

    }

    else {

        navbar.innerHTML = `
            <li class="nav-item">
                <a class="nav-link" href="/">
                    Home
                </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/login/">
                    Login
                </a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/register/">
                    Register
                </a>
            </li>
        `;

    }

});
