# Crediation Interview Solution
This repository contains code that responds to the second test of the technical interview for Junior Software Engineer at Crediation

## Background
Create a simple Django app with a REST API endpoint. The API should be able to able to fetch a list of users from the json file (Create a JSON file with any number of users). The API should also allow the user to fetch a specific user from the JSON file. Please use the best software development practices you know.


## Tech Stack
Editor:
- VS Code

API Testing
- curl
- Postman

Programming language: 
- Python3

        Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation.
        
        PEP8 Coding style is used.
        
        Test for PEP8 compliance: 
                pycodestyle <python_file>

Frameworks:
- Django
- Django Rest Framework

Test Envrionment: 
 - Ubuntu 20.04.3 LTS

## Dependencies
All the dependencies (external libraries) are defined in the single place - settings.py file in crediation folder.

Dependencies used:
        
        - Django Rest Framework

##


## How to run server

Clone the repository.

Install the follwoing packages in your virtual env or globally:

- Django        ```pip install Django```
- Django rest framework ``` pip install djangorestframework ```

Navigate to the crediation directory.

Open your terminal in the directory.

Start the dev server as shown below:

```python manage.py runserver```

Test end points as you like.

# End Points
On localhost:
        
        POST to add new user
        http://localhost:8000/users/

        
                {
                        "firstname": "John",
                        "lastname": "Doe",
                        "email": "johndoe@gmail.com"
                }

                On success:
                        Status Code: 201
                        Mesaage:
                                {
                                        "message": "success"
                                }


        GET
        http://localhost:8000/users/


        GET with specific user with params
        http://localhost:8000/users/?email=<useremail>

                If not found:
                        {
                                "Message": "Could not find user"
                        }

        <img src="https://github.com/smithjilks/crediation-test-0x01/blob/feature-users-api/images/test.png" width="400"/>

## UNIT Tests
The screenshot below shows the tests that are done on the repo:

### Unit Tests in user model
The unit tests done here are:
- Testing for unique uuid created using python UUID 
- Testing instance of class is of type User Model
<img src="https://github.com/smithjilks/crediation-test-0x01/blob/feature-users-api/images/unit-test.png" width="400"/>

To execute Unit Test run the python script in the crediation directory as shown below:
```python3 manage.py test```


## LICENSE
        MIT License

        Copyright (c) 2021 Smith Jilks

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.