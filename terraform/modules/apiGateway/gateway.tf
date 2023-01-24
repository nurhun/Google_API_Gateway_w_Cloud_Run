# --- apiGateway/gateway.tf ---

resource "google_api_gateway_api_config" "api_config" {
  provider = google-beta

  api           = google_api_gateway_api.api.api_id
  api_config_id = "${var.Gateway_API_Config_ID}-${filemd5(var.OpenAPI_document_file_path)}"
  #   api_config_id = var.Gateway_API_Config_ID

  openapi_documents {
    document {
      path     = var.OpenAPI_document_filename
      contents = filebase64(var.OpenAPI_document_file_path)
    }
  }
  lifecycle {
    create_before_destroy = true
  }
}

resource "google_api_gateway_gateway" "api_gw" {
  provider = google-beta
  region   = var.REGION
  project  = var.PROJECT_ID

  api_config   = google_api_gateway_api_config.api_config.id
  gateway_id   = var.API_GATEWAY_ID
  display_name = var.API_Gateway_Display_Name
}