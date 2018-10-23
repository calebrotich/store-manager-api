# store-manager-api

#### Continous Integration badges
[![Build Status](https://travis-ci.com/calebrotich10/store-manager-api.svg?branch=develop)](https://travis-ci.com/calebrotich10/store-manager-api) [![Coverage Status](https://coveralls.io/repos/github/calebrotich10/store-manager-api/badge.svg?branch=develop)](https://coveralls.io/github/calebrotich10/store-manager-api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/e87820f417b8d15c3a64/maintainability)](https://codeclimate.com/github/calebrotich10/store-manager-api/maintainability)


Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. This repository contains the API endpoints for the application.

#### Endpoints
<table>
  <tr>
    <th>Http Method</th>
    <th>Endpoint</th>
    <th>Functionality</th>
  </tr>
  <tr>
    <td>POST</td>
    <td>api/v1/auth/signup</td>
    <td>Creates a new user account</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>api/v1/products</td>
    <td>Used by the admin to add a new product</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>api/v1/saleorder</td>
    <td>Used by the sale attendant to add a new sale order</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v1/auth/signin</td>
    <td>Authenticates and creates a token for the users</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v1/products/&ltproduct_id&gt</td>
    <td>Enables a user to fetch a specific product</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v1/saleorder/&ltsale_order_id&gt</td>
    <td>Enables a user to fetch a specific sale order</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v1/products</td>
    <td>Enables a user to fetch all products</td>
  </tr>
  <tr>
    <td>GET</td>
    <td>api/v1/saleorder</td>
    <td>Enables a user to fetch all sale orders</td>
  </tr>
</table>

#### Installing the application
1. Open a command terminal in your preferred folder
2. Run command `git clone https://github.com/calebrotich10/store-manager-api.git` to have a copy locally
3. `cd store-manager-api`
4. Create a virtual environment for the application `virtualenv venv`
5. Install dependencies from the `requirements.txt` file `pip3 install -r requirements.txt`
6. Export environment variables to your environment ```export JWT_SECRET_KEY=your-secret-key```, ```export FLASK_APP="run.py"```
6. Run the application using flask command `flask run` or using python3 `python3 run.py`

#### Running tests
Inside the virtual environment created above, run command: `coverage run --source=app.api.v1 -m pytest app/tests/v1 -v -W error::UserWarning && coverage report`

#### Technologies used
1. `JWT` for authentication
2. `pytest` for running tests
3. Python based framework `flask`
4. Flask packages

#### Deployment
[Heroku](https://store-manager-api.herokuapp.com/api/v1/products)

#### Documentation
https://documenter.getpostman.com/view/5265531/RWguxwzy

#### Author
[Caleb Rotich](https://github.com/calebrotich10)

#### Credits
This application was build as part of the Andela NBO 33 challenge
