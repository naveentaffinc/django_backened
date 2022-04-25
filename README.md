After cloning the Repo

Make Sure Python and PIP is installed in the machine
	
Install Virtual Environment
	
	pip install virtualenv

Traverse inside your working directory i.e (where manage.py file is there)
Create a VirtualEnv there by running the command below
	
	virtualenv myenv or python -m virtualenv myenv

Now Activate the Virtualenv

	myenv\Scripts\activate	

Now Install Django using the below Command

	python -m pip install django

Now Install the rest framework using the below command
	
	python -m pip install djangorestframework

Now the application will be served at http://127.0.0.1:8000
Postman collection file is under the name "My Momism Django" in the repository
