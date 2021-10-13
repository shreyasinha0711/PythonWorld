Copy whatever you have in the lambda_function fron AWS lambda console and paste it in a new python script and save it as lambda_function.py.

Make a new folder (I name it as package) and save requests module in it by running the following code in terminal: pip install -t package requests

Move lambda_function.py into the folder (package).

Go to the folder and select all content and zip them.

Go back to the AWS Lambda console. select the function and under the Function code section, click on 'Action' (on the right side) and select Upload a .zip file.

Upload the folder. lambda_function should be uploaded automatically.

Run and Enjoy.



"""Install these in cmd for pytest"""

pip install -u pytest
pip install pytest-html
pip install pytest-mock
pip install jsonschema

"""Install these in cmd for test coverage"""
pip install coverage
pip install pytest-cov

"""To run test cases """
python -m pytest test_lambda_function.py

""" To run single test cases """
python -m pytest test_lambda_function.py::<test_case_function_name>
ex: python -m pytest test_lambda_function.py::test_lambda_invalid_response

"""To run the coverage of code"""

coverage run lambda_function.py
coverage report
coverage report -m


coverage run test_lambda_function.py
coverage report
coverage report -m

"""To run the coverage of test cases"""
pytest --cov=lambda_function