Copy whatever you have in the lambda_function fron AWS lambda console and paste it in a new python script and save it as lambda_function.py.

Make a new folder (I name it as package) and save requests module in it by running the following code in terminal: pip install -t package requests

Move lambda_function.py into the folder (package).

Go to the folder and select all content and zip them.

Go back to the AWS Lambda console. select the function and under the Function code section, click on 'Action' (on the right side) and select Upload a .zip file.

Upload the folder. lambda_function should be uploaded automatically.

Run and Enjoy.