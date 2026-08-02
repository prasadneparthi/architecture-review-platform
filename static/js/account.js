document
    .getElementById("change-password-form")
    .addEventListener(
        "submit",
        changePassword
    );

document
    .getElementById("delete-account-form")
    .addEventListener(
        "submit",
        deleteAccount
    );

loadProfile();


async function loadProfile() {

    const response = await fetch(

        "/api/auth/profile/",

        {
            headers: {
                "Authorization":
                    `Bearer ${localStorage.getItem("access")}`
            }
        }

    );

    if (handleUnauthorized(response)) {

        return;

    }

    if (!response.ok) {

        return;

    }

    const data = await response.json();

    document.getElementById(
        "account-username"
    ).textContent = data.username;

    document.getElementById(
        "account-email"
    ).textContent = data.email;

}


async function changePassword(event) {

    event.preventDefault();

    const response = await fetch(

        "/api/auth/change-password/",

        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
                "Authorization":
                    `Bearer ${localStorage.getItem("access")}`
            },

            body: JSON.stringify({

                old_password:
                    document.getElementById(
                        "old-password"
                    ).value,

                new_password:
                    document.getElementById(
                        "new-password"
                    ).value,

                confirm_password:
                    document.getElementById(
                        "confirm-password"
                    ).value

            })

        }

    );

    if (handleUnauthorized(response)) {

        return;

    }

    const data = await response.json();

    if (!response.ok) {

        if (data.message) {

            alert(data.message);

        }

        else if (data.confirm_password) {

            alert(data.confirm_password[0]);

        }

        else if (data.old_password) {

            alert(data.old_password[0]);

        }

        else if (data.new_password) {

            alert(data.new_password[0]);

        }

        else if (data.non_field_errors) {

            alert(data.non_field_errors[0]);

        }

        else {

            alert("Unable to change password.");

        }

        return;

    }

    alert(data.message);

    logoutUser();

}


async function deleteAccount(event) {

    event.preventDefault();

    if (
        !confirm(
            "This action cannot be undone.\n\nDelete your account?"
        )
    ) {

        return;

    }

    const response = await fetch(

        "/api/auth/delete-account/",

        {
            method: "DELETE",

            headers: {
                "Content-Type": "application/json",
                "Authorization":
                    `Bearer ${localStorage.getItem("access")}`
            },

            body: JSON.stringify({

                password:
                    document.getElementById(
                        "delete-password"
                    ).value

            })

        }

    );

    if (handleUnauthorized(response)) {

        return;

    }

    const data = await response.json();

    if (!response.ok) {

        if (data.message) {

            alert(data.message);

        }

        else if (data.password) {

            alert(data.password[0]);

        }

        else {

            alert("Unable to delete account.");

        }

        return;

    }

    alert(data.message);

    logoutUser();

}