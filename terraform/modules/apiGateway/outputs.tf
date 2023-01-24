

output "api_gateway_url" {
  value = google_api_gateway_gateway.api_gw.default_hostname
}