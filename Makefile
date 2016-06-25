define USAGE
- test
- install target=PACKAGE_NAME
endef
export USAGE

.PHONY: help
help:
	@echo "$${USAGE}"


.PHONY: test
test:
	env2/bin/py.test
	env3/bin/py.test

.PHONY: help
install:
	@env2/bin/pip install -U $(target)
	@env2/bin/pip freeze > requirements/py2.txt

	@env3/bin/pip install -U $(target)
	@env3/bin/pip freeze > requirements/py3.txt

	@git add requirements
	@git commit -m "install $(target)"
