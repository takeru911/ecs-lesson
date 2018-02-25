variable "aws_region" {
  description = "The AWS region to create things in."
  default     = "ap-northeast-1"
}

variable "instance_type" {
  default     = "t2.small"
  description = "AWS instance type"
}
