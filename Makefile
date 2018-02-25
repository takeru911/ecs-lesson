REGISTRY_NAME=044768335503.dkr.ecr.ap-northeast-1.amazonaws.com
CONTAINER_TAG=0.2
CONTAINER_NAME=$(REGISTRY_NAME)/simple_server:$(CONTAINER_TAG)


.PHONY: push login build run

push: login
	docker push $(CONTAINER_NAME)

build:
	docker build -t $(CONTAINER_NAME) -f docker_env/Dockerfile .

run:
	docker run  -p 8080:8080 -it $(CONTAINER_NAME)

login:
	$$(aws ecr get-login --no-include-email --region ap-northeast-1)
