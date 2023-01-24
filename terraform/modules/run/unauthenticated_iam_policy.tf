# --- run/unauthenticated_iam_policy.tf ---


# NOTE: "Cloud Run Admin" role is required on terraform service account to be able to all unauthenticated users. 
data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}