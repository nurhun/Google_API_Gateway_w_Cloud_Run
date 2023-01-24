# --- root/main.tf ---

data "google_project" "project" {
}

data "google_client_config" "project_config" {
}

data "google_container_engine_versions" "central1-a" {
  provider       = google-beta
  location       = "us-central1-a"
  version_prefix = "1.24."
}

resource "google_project_service" "enabled_services" {
  for_each = toset(var.services)
  service  = each.key

  provisioner "local-exec" {
    command = "sleep 60"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "sleep 15"
  }

  disable_on_destroy = false

}


module "networking" {
  source = "./modules/networking"

  REGION                              = var.REGION
  PROJECT_ID                          = var.PROJECT_ID
  vpc_name                            = "apigateway-vpc"
  vpc_description                     = "API Gateway VPC."
  vpc_auto_create_subnetworks         = false
  vpc_delete_default_routes_on_create = false
  vpc_mtu                             = 1460
  vpc_routing_mode                    = "REGIONAL"
}


module "run" {
  source = "./modules/run"

  REGION     = var.REGION
  PROJECT_ID = var.PROJECT_ID

  # API_GATEWAY = module.apiGateway.google_api_gateway_gateway.api_gw

  # Frontend Service
  FRONTEND_SERVICE_NAME = "front"
  FRONTEND_IMAGE        = "gcr.io/nifty-bird-321722/django_rest_framework_movies_apis_w_react_frontend-nginx:run-template-v1"
  API_GATEWAY_URL       = module.apiGateway.api_gateway_url

  # Backend Service
  BACKEND_SERVICE_NAME = "back"
  BACKEND_IMAGE        = "gcr.io/nifty-bird-321722/django_rest_framework_movies_apis_w_react_frontend_backend:run-v8"
}

module "apiGateway" {
  source = "./modules/apiGateway"

  REGION           = var.REGION
  PROJECT_ID       = var.PROJECT_ID

  # API
  API_ID           = "moviesapi"
  API_Display_Name = "moviesAPI"

  # OpenAPI Config file
  Gateway_API_Config_ID      = "config"
  OpenAPI_document_filename  = "swagger.yml"
  OpenAPI_document_file_path = "./modules/apiGateway/swagger.yml"

  # Gateway
  API_GATEWAY_ID           = "moviesapigw"
  API_Gateway_Display_Name = "Movies API Gateway - us-central1"
}