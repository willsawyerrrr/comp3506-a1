all: zip

tidy: 
	find -name __pycache__ -type d -exec rm -rf {} +

zip: tidy
	zip upload.zip -r data -r structures execute_refgrid.py test_structures.py

