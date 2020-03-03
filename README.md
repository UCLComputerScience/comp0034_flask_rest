# comp0034_flask_rest
COMP0034 Code as at the start of the REST API lecture

To see a completed version of the REST example created in the lecture refer to https://github.com/UCLComputerScience/comp0034_flask_rest_complete.git

#### Setup
1. Create a venv
2. Install the packages from requirements.txt

### Exercise 1: Update the project structure to add a Python package for the rest api
1. Add a new Python package called `api` to `cscourses` 
2. Create a new `routes.py` in the api directory and add a blueprint for the api
3. Register the blueprint in `cscourses/__init__.py`