# --- run/frontend.tf ---

resource "google_cloud_run_service" "frontend" {
  provider = google-beta

  name     = var.FRONTEND_SERVICE_NAME
  project  = var.PROJECT_ID
  location = var.REGION

  metadata {
    annotations = {
      "run.googleapis.com/launch-stage" = "BETA"
    }
  }

  template {
    spec {
      containers {
        image = var.FRONTEND_IMAGE

        # command = []
        # args = []

        ports {
          name           = "http1"
          container_port = 80
        }

        env {
          name  = "NGINX_PORT"
          value = "80"
        }

        env {
          name  = "NGINX_SERVER_NAME"
          value = "_"
        }

        env {
          name  = "NGINX_PROXY_PASS"
          value = "https://${var.API_GATEWAY_URL}"
        }

        # env {
        #   name  = "REACT_APP_AXIOS_PRODUCTION_BASEURL"
        #   value = "https://${var.API_GATEWAY_URL}"
        # }

        resources {
          limits = {
            # CPU usage limit
            # https://cloud.google.com/run/docs/configuring/cpu
            cpu = "1000m" # 1 vCPU

            # Memory usage limit (per container)
            # https://cloud.google.com/run/docs/configuring/memory-limits
            memory = "512Mi"
          }
        }

        # All other probes are disabled if a startup probe is provided, until it succeeds.
        # Container will not be added to service endpoints if the probe fails. 
        startup_probe {
          initial_delay_seconds = 1
          timeout_seconds       = 3
          period_seconds        = 3
          failure_threshold     = 3
          tcp_socket {
            port = 80
          }
        }

        # Periodic probe of container liveness. Container will be restarted if the probe fails.
        liveness_probe {
          http_get {
            path = "/"
          }
        }
      }

      timeout_seconds = 300

      # Maximum concurrent requests per container of the Revision.
      container_concurrency = 80
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  lifecycle {
    ignore_changes = [
      metadata.0.annotations,
    ]
  }

  depends_on = [
    var.API_GATEWAY_URL
  ]
}


# This allow unauthenticated invocations
resource "google_cloud_run_service_iam_policy" "frontend_noauth" {
  location = google_cloud_run_service.frontend.location
  project  = google_cloud_run_service.frontend.project
  service  = google_cloud_run_service.frontend.name

  policy_data = data.google_iam_policy.noauth.policy_data

  depends_on = [
    google_cloud_run_service.frontend
  ]
}