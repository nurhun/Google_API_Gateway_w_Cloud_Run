# -- networking/variables.tf

variable "REGION" {}

### VPC test-vpc ###
variable "PROJECT_ID" {}
variable "vpc_name" {}
variable "vpc_description" {}
variable "vpc_auto_create_subnetworks" {}
variable "vpc_delete_default_routes_on_create" {}
variable "vpc_mtu" {}
variable "vpc_routing_mode" {}


### Subnet subnets ###
variable "subnets" {
  description = "API Gateway-vpc subnets"
  type        = map(any)
  default = {
    "subnet-us-central1" = {
      region                   = "us-central1"
      ip_cidr_range            = "10.128.0.0/20",
      private_ip_google_access = "true",
      # private_ipv6_google_access = "true",
      stack_type = "IPV4_ONLY",
    }
  }
}