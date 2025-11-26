.PHONY: install test

install:
	sage -pip install --upgrade .

test:
	sage -t applications/

doc:
	cd docs && make html

doc-pdf:
	cd docs && make latexpdf
