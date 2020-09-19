[![Build Status](https://travis-ci.org/vyahello/fake-vehicles-api.svg?branch=master)](https://travis-ci.org/vyahello/fake-vehicles-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/fake-vehicles-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/fake-vehicles-api?branch=master)
[![Issues](https://img.shields.io/github/issues/vyahello/fake-vehicles-api)](https://github.com/vyahello/fake-vehicles-api/issues)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/fake-vehicles-api)](https://hitsofcode.com/view/github/vyahello/fake-vehicles-api)

# Fake Vehicles API
> A lightweight fake vehicle API written in [API Star](https://docs.apistar.com/) 🌟 python WEB API toolkit framework. 
> This project is built only as a sample REST API toolkit.
>
> Fake data was generated from cool https://www.mockaroo.com source.


## Tools
- `python 3.8`
- `RESTful API`
- `pytest`
- `travis CI`
- `heroku`

In addition it is `fully type annotated` and covered with bunch of static code analysis tools like `mypy`, `flake8`, `pylint`, `pydocstyle` and `black`.

## Usage

![Screenshot](static/demo.png)

### Quick start

Run next command from the root directory of the project:
```bash
python -m api
```

After please open [localhost:5000/](http://localhost:5000/) or [localhost:5000/index.html](http://localhost:5000/index.html) path in your browser to obtain home page. 

## Development notes

### API endpoints
There are several endpoints already developed (others will be added soon):
  - `GET` request on `/api` endpoint to get list of all vehicles e.g:
    ```bash
    curl localhost:5000/api
    ```
  - `POST` request on `/api` endpoint to create a vehicle e.g:
    ```bash
     curl -X POST \
    -H "Content-type: application/json \"
    -d {"manufacturer": "BMW", "model": "X5", "year": 2011, "vin": "WBAWV53589P465532"}' \
    localhost:5000/api
    ```
  - `GET` request on `/api/{id}` endpoint to get single vehicle e.g:
    ```bash
    curl localhost:5000/api/99
    ```
  - `PUT` request on `/api/{id}` endpoint to update single vehicle e.g:
    ```bash
    curl -X PUT \
    -H "Content-type: application/json" \
    -d '{"manufacturer": "BMW", "model": "X5", "year": 2011, "vin": "WBAWV53589P465532"}' \
    localhost:5000/api/99
    ```
  - `DELETE` request on `/api/{id}` to delete single vehicle e.g:
    ```bash
    curl -X DELETE localhost:5000/api/99
    ```

### Testing
Project is covered with both **_unittests_** and **_functional_** tests on REST API endpoints using [pytest](https://docs.pytest.org/en/latest) testing framework.

Please run next command from the root directory to start testing:
```bash
pytest
```
> If you would like to run only `smoke` tests or `unittests` please run tests with corresponding marker e.g:
> 
> ```bash
> pytest -m smoke
> ```

Please open `test-report.html` file in your browser to see testing report.


### Heroku deployment
Please follow instructions from - https://python-responder.org/en/latest/deployment.html

- Install heroku following by - https://devcenter.heroku.com/articles/heroku-cli#download-and-install
- Configure [Procfile](Procfile)
```text
web: gunicorn vehicle_api:api_app
```
- Create `runtime.txt` file
```text
python-3.8.0
```
- Login to heroku
```bash
heroku login
```
- Create an application
```bash
heroku create fake-vehicles-api
```
- Commit and push repo into a heroku
```bash
git add . && git commit -m "My first heroku app" && git push heroku master
```
- Spin up dynos for web
```bash
heroku ps:scale web=1
```
- Check heroku logs
```bash
heroku logs --tail
```
- Open an application via browser: https://fake-vehicles-api.herokuapp.com

## Meta
Author – _Volodymyr Yahello_.

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/fake-vehicles-api/issues). 
If you have ideas you want to change/implement please do not hesitate and create an issue.