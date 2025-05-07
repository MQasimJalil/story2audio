# Makefile

install:
	pip install -r requirements.txt

run-server:
	python app/main.py

run-tests:
	pytest test

download-models:
	python app/load_models.py

build:
	python -m grpc_tools.protoc -I=app/proto --python_out=. --grpc_python_out=. app/proto/story.proto

docker-build:
	docker build -t story2audio .

docker-run:
	docker run -p 50051:50051 -v "$(USERPROFILE)/.cache/suno:/root/.cache/suno" -v "$(USERPROFILE)/.cache/huggingface:/root/.cache/huggingface" story2audio