clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf build
	rm -rf dist
	rm -rf __pycache__
	rm -rf *.egg-info
	rm -rf data
	pip install -e .['dev'] --upgrade --no-cache
	mkdir data
	touch data/best_score.txt
install:
	pip install -e .['dev']
	mkdir data
	touch data/best_score.txt
test:
	# make tests
coverage:
	# make coverage
run:
	cd snake_game/ && python snake.py
