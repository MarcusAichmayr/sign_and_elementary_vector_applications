.PHONY: install test

install:
	sage -pip install --upgrade .

test:
	sage -t applications/

test-long:
    sage -t --long --warn-long 5 applications/

doc:
	cd docs && make html

doc-pdf:
	cd docs && make latexpdf
