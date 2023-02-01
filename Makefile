.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec crc-vv --no-session -- sam deploy

deploy-site:
	aws-vault exec crc-vv --no-session -- aws s3 sync ./resume-site s3://s3-bucket-vv
