docs:
	cd docs
	make html
isort:
	isort enamlnativecli
	isort tests
typecheck:
	mypy enamlnativecli/main.py --ignore-missing-imports
lintcheck:
	flake8 --ignore=E501 enamlnativecli --per-file-ignores=enamlnativecli/templates/*:E999
	flake8 --ignore=E501 tests
reformat:
	black enamlnativecli/main.py
	black tests
test:
	pytest -v tests --cov enamlnativecli --cov-report xml --asyncio-mode auto

precommit: isort reformat lintcheck typecheck
