clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf build
	rm -rf dist
	rm -rf __pycache__
	rm -rf *.egg-info
	pip install -e .['dev'] --upgrade --no-cache
install:
	pip install -e .['dev']
test:
	# make tests
coverage:
	# make coverage
run:
	python ./snake_game/snake.py
