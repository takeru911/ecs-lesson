TERRAFORM=terraform

init: terraform/init
plan: terraform/plan
apply: terraform/apply

terraform/%:
	$(TERRAFORM) $(@F)
