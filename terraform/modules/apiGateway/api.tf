# --- apiGateway/api.tf ---

resource "google_api_gateway_api" "api" {
  provider = google-beta

  project      = var.PROJECT_ID
  api_id       = var.API_ID
  display_name = var.API_Display_Name
}
# terraform import module.apiGateway.google_api_gateway_api.api projects/nifty-bird-321722/locations/global/apis/moviesapi