# --- networking/main.tf ---

resource "google_compute_network" "vpc" {
  project                         = var.PROJECT_ID
  name                            = var.vpc_name
  description                     = var.vpc_description
  auto_create_subnetworks         = var.vpc_auto_create_subnetworks
  delete_default_routes_on_create = var.vpc_delete_default_routes_on_create
  mtu                             = var.vpc_mtu
  routing_mode                    = var.vpc_routing_mode

  lifecycle {
    create_before_destroy = true
  }
}
# terraform import module.networking.google_compute_network.vpc apigateway-vpc

resource "google_compute_subnetwork" "subnets" {
  project = var.PROJECT_ID
  network = google_compute_network.vpc.self_link

  for_each = var.subnets

  name                     = each.key
  region                   = each.value.region
  ip_cidr_range            = each.value.ip_cidr_range
  private_ip_google_access = each.value.private_ip_google_access
  # private_ipv6_google_access = each.value.private_ipv6_google_access
  stack_type = each.value.stack_type

  depends_on = [
    google_compute_network.vpc
  ]
}
# terraform import module.networking.google_compute_subnetwork.subnets[\"subnet-us-central1\"]  projects/nifty-bird-321722/regions/us-central1/subnetworks/subnet-us-central1
