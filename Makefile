pip:
	@$(MAKE) prod
	@$(MAKE) dev

prod:
	@pip install -U pip
	@pip install -r requirements/requirement.txt
	@pip install -r requirements/requirement-govern.txt

dev:
	@pip install -r requirements/requirement-test.txt
	@pip install -r requirements/requirement-dev.txt
	@pre-commit install

lint:
	@sh scripts/check_lint.sh

clean:
	@find . -name '__pycache__' -type d -exec rm -rf {} +
	@rm -rf logs htmlcov .pytest_cache