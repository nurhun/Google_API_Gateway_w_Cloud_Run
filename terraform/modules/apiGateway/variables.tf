# --- apiGateway/variables.tf ---

variable "REGION" {}

variable "PROJECT_ID" {}

variable "API_ID" {}

variable "API_Display_Name" {}

variable "Gateway_API_Config_ID" {}

variable "OpenAPI_document_filename" {
  description = "OpenAPI spec 2.0 file name"
}

variable "OpenAPI_document_file_path" {
  description = "OpenAPI spec 2.0 file path"
}

variable "API_GATEWAY_ID" {}

variable "API_Gateway_Display_Name" {}