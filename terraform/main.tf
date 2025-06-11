provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "t2s" {
  bucket = var.bucket_name
  acl    = "private"
}
