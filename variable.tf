variable "GCP_cred_json" {
  description = "My Credentials"
  default     = "~/.gc/zoomcamp-2024-409714-1a9eec901119.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project_id" {
  description = "Project"
  default     = "zoomcamp-2024-409714"
}

variable "region" {
  description = "Region"
  #VM configured Region "IND"
  default     = "ASIA-SOUTH1"
}

variable "region_zone" {
  description = "zone"
  #Instance configured zone (mumbai)
  default     = "ASIA-SOUTH1-B"
}

variable "location" {
  description = "Project Location"
  #configure location
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "zoom_dataset1"
}

variable "gcp_bucket_name" {
  description = "My Storage Bucket Name"
  #Update the below to a unique bucket name
  default = "zoomcamp-2024-409714-bucket"
}

