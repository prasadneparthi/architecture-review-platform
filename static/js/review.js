// ======================================================
// Helpers
// ======================================================

function bool(value) {

    return value === "true";

}

function token() {

    const access = localStorage.getItem("access");

    if (!access) {

        handleUnauthorized({
            status: 401
        });

        return null;
    }

    return access;

}

// ======================================================
// Containers
// ======================================================

const servicesContainer =
    document.getElementById("services-container");

const databasesContainer =
    document.getElementById("databases-container");

// ======================================================
// Services
// ======================================================

document
    .getElementById("add-service")
    .addEventListener(
        "click",
        addService
    );

function addService() {

    const div =
        document.createElement("div");

    div.className =
        "card border p-3 mb-3 service-item";

    div.innerHTML = `

        <div class="row">

            <div class="col-md-3">

                <label>
                    Name
                    <span class="text-danger">*</span>
                </label>

                <input
                    class="form-control service-name"
                    required
                >

            </div>

            <div class="col-md-3">

                <label>
                    Technology
                    <span class="text-danger">*</span>
                </label>

                <input
                    class="form-control service-technology"
                    required
                >

            </div>

            <div class="col-md-2">

                <label>
                    Instances
                    <span class="text-danger">*</span>
                </label>

                <input
                    type="number"
                    min="1"
                    value="1"
                    class="form-control service-instances"
                    required
                >

            </div>

            <div class="col-md-2">

                <label>
                    Stateless
                    <span class="text-danger">*</span>
                </label>

                <select
                    class="form-select service-stateless"
                >
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                </select>

            </div>

            <div class="col-md-2">

                <label>
                    Async
                    <span class="text-danger">*</span>
                </label>

                <select
                    class="form-select service-async"
                >
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                </select>

            </div>

        </div>

        <button
            type="button"
            class="btn btn-danger btn-sm mt-3 remove-service"
        >
            Remove
        </button>

    `;

    div
        .querySelector(".remove-service")
        .onclick = () => div.remove();

    servicesContainer.appendChild(div);

}

addService();

// ======================================================
// Databases
// ======================================================

document
    .getElementById("add-database")
    .addEventListener(
        "click",
        addDatabase
    );

function addDatabase() {

    const div =
        document.createElement("div");

    div.className =
        "card border p-3 mb-3 database-item";

    div.innerHTML = `

        <div class="row">

            <div class="col-md-2">

                <label>
                    Name
                    <span class="text-danger">*</span>
                </label>

                <input
                    class="form-control database-name"
                    required
                >

            </div>

            <div class="col-md-2">

                <label>
                    Type
                </label>

                <select
                    class="form-select database-type"
                >
                    <option>MongoDB</option>
                    <option>PostgreSQL</option>
                    <option>MySQL</option>
                    <option>Oracle</option>
                    <option>SQL Server</option>
                    <option>Redis</option>
                </select>

            </div>

            <div class="col-md-2">

                <label>
                    Replication
                    <span class="text-danger">*</span>
                </label>

                <select
                    class="form-select database-replication"
                >
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                </select>

            </div>

            <div class="col-md-2">

                <label>
                    Read Replicas
                </label>

                <select
                    class="form-select database-read"
                >
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                </select>

            </div>

            <div class="col-md-2">

                <label>
                    Sharding
                </label>

                <select
                    class="form-select database-sharding"
                >
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                </select>

            </div>

            <div class="col-md-1">

                <label>
                    Indexes
                    <span class="text-danger">*</span>
                </label>

                <select
                    class="form-select database-indexes"
                >
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                </select>

            </div>

            <div class="col-md-1">

                <label>
                    Pool
                    <span class="text-danger">*</span>
                </label>

                <select
                    class="form-select database-pool"
                >
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                </select>

            </div>

        </div>

        <button
            type="button"
            class="btn btn-danger btn-sm mt-3 remove-database"
        >
            Remove
        </button>

    `;

    div
        .querySelector(".remove-database")
        .onclick = () => div.remove();

    databasesContainer.appendChild(div);

}

addDatabase();
// ======================================================
// Submit Review
// ======================================================

async function submitReview(event) {

    event.preventDefault();

    const architecture = {

        system_name:
            document.getElementById("system-name").value,

        architecture_type:
            document.getElementById("architecture-type").value,

        services: [],

        databases: [],

        load_balancer: {

            enabled: bool(
                document.getElementById("lb-enabled").value
            ),

            health_checks: bool(
                document.getElementById("lb-health-checks").value
            ),

        },

        cache: {

            enabled: bool(
                document.getElementById("cache-enabled").value
            ),

            type:
                document.getElementById("cache-type").value,

            invalidation_strategy: bool(
                document.getElementById("cache-invalidation").value
            ),

        },

        message_queue: {

            enabled: bool(
                document.getElementById("mq-enabled").value
            ),

            type:
                document.getElementById("mq-type").value,

            retry_enabled: bool(
                document.getElementById("mq-retry").value
            ),

        },

        security: {

            authentication: bool(
                document.getElementById("authentication").value
            ),

            authentication_type:
                document.getElementById("authentication-type").value,

            authorization: bool(
                document.getElementById("authorization").value
            ),

            authorization_model:
                document.getElementById("authorization-model").value,

            https: bool(
                document.getElementById("https").value
            ),

            encrypt_at_rest: bool(
                document.getElementById("encrypt-at-rest").value
            ),

            rate_limiting: bool(
                document.getElementById("rate-limiting").value
            ),

            input_validation: bool(
                document.getElementById("input-validation").value
            ),

            secret_management: bool(
                document.getElementById("secret-management").value
            ),

            default_credentials: bool(
                document.getElementById("default-credentials").value
            ),

            cors: bool(
                document.getElementById("cors").value
            ),

            security_headers: bool(
                document.getElementById("security-headers").value
            ),

        },

        monitoring: {

            enabled: bool(
                document.getElementById("monitoring-enabled").value
            ),

            centralized_logging: bool(
                document.getElementById("centralized-logging").value
            ),

            alerting: bool(
                document.getElementById("alerting").value
            ),

            status_endpoint: bool(
                document.getElementById("status-endpoint").value
            ),

        },

        resilience: {

            retry_enabled: bool(
                document.getElementById("retry-enabled").value
            ),

            timeouts: bool(
                document.getElementById("timeouts").value
            ),

            circuit_breaker: bool(
                document.getElementById("circuit-breaker").value
            ),

            graceful_degradation: bool(
                document.getElementById("graceful-degradation").value
            ),

        },

        backup: {

            enabled: bool(
                document.getElementById("backup-enabled").value
            ),

            restore_tested: bool(
                document.getElementById("restore-tested").value
            ),

            rto_rpo_defined: bool(
                document.getElementById("rto-rpo").value
            ),

            dr_documented: bool(
                document.getElementById("dr-documented").value
            ),

        },
                api: {

            pagination: bool(
                document.getElementById("pagination").value
            ),

            compression: bool(
                document.getElementById("compression").value
            ),

            versioning: bool(
                document.getElementById("versioning").value
            ),

        },

        deployment: {

            rollback: bool(
                document.getElementById("rollback").value
            ),

            cicd: bool(
                document.getElementById("cicd").value
            ),

            repeatable_releases: bool(
                document.getElementById("repeatable-releases").value
            ),

            zero_downtime: bool(
                document.getElementById("zero-downtime").value
            ),

            safe_db_migration: bool(
                document.getElementById("safe-db-migration").value
            ),

        },

        architecture: {

            layered_design: bool(
                document.getElementById("layered-design").value
            ),

            separation_of_concerns: bool(
                document.getElementById("separation-of-concerns").value
            ),

            interface_definition: bool(
                document.getElementById("interface-definition").value
            ),

            loose_coupling: bool(
                document.getElementById("loose-coupling").value
            ),

        },

        testing: {

            unit_tests: bool(
                document.getElementById("unit-tests").value
            ),

            integration_tests: bool(
                document.getElementById("integration-tests").value
            ),

            api_tests: bool(
                document.getElementById("api-tests").value
            ),

            component_testability: bool(
                document.getElementById("component-testability").value
            ),

        },

        documentation: {

            api_docs: bool(
                document.getElementById("api-docs").value
            ),

            architecture_docs: bool(
                document.getElementById("architecture-docs").value
            ),

            deployment_docs: bool(
                document.getElementById("deployment-docs").value
            ),

            operations_docs: bool(
                document.getElementById("operations-docs").value
            ),

        },

        configuration: {

            externalized: bool(
                document.getElementById("externalized").value
            ),

            environment_support: bool(
                document.getElementById("environment-support").value
            ),

            centralized: bool(
                document.getElementById("centralized").value
            ),

            no_hardcoded_values: bool(
                document.getElementById("no-hardcoded-values").value
            ),

        }

    };

    // ==========================================
    // Services
    // ==========================================

    document
        .querySelectorAll(".service-item")
        .forEach(function(service) {

            architecture.services.push({

                name:
                    service.querySelector(".service-name").value,

                technology:
                    service.querySelector(".service-technology").value,

                instances:
                    parseInt(
                        service.querySelector(".service-instances").value
                    ),

                stateless:
                    bool(
                        service.querySelector(".service-stateless").value
                    ),

                async_processing:
                    bool(
                        service.querySelector(".service-async").value
                    ),

            });

        });

    // ==========================================
    // Databases
    // ==========================================

    document
        .querySelectorAll(".database-item")
        .forEach(function(database) {

            architecture.databases.push({

                name:
                    database.querySelector(".database-name").value,

                type:
                    database.querySelector(".database-type").value,

                replication:
                    bool(
                        database.querySelector(".database-replication").value
                    ),

                read_replicas:
                    bool(
                        database.querySelector(".database-read").value
                    ),

                sharding:
                    bool(
                        database.querySelector(".database-sharding").value
                    ),

                indexes:
                    bool(
                        database.querySelector(".database-indexes").value
                    ),

                connection_pooling:
                    bool(
                        database.querySelector(".database-pool").value
                    ),

            });

        });
    const access = token();
    if (!access){
        return;
    }
    const response = await fetch(
        "/api/review/",
        {
            method: "POST",

            headers: {

                "Content-Type": "application/json",

                "Authorization": `Bearer ${access}`,

            },

            body: JSON.stringify(architecture),

        }
    );
    if (handleUnauthorized(response)){
        return;
    }

    const data = await response.json();

    if (response.ok) {

        sessionStorage.setItem(
            "review_result",
            JSON.stringify(data)
        );

        window.location.href =
            "/review/result/";

    }
    else {

        alert(
            JSON.stringify(data)
        );

    }

}