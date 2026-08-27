.PHONY: build run test clean docker-up

build:
	docker build -t paybridge:latest .

run:
	python main.py

test:
	cd backend && python -m pytest

docker-up:
	docker-compose up --build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
