# --- root/outputs.tf ---

output "project" {
  value = data.google_client_config.project_config.project
}

output "vpc_id" {
  value = module.networking.vpc_id
}

output "subnets" {
  value = module.networking.subnets
}

output "frontend_url" {
  value = module.run.frontend_url
}

output "backend_url" {
  value = module.run.backend_url
}

output "api_gateway_url" {
  value = module.apiGateway.api_gateway_url
}