# Mock vehicle API
A lightweight fake vehicle API written in [API Star](https://docs.apistar.com/) python WEB API toolkit framework. 
This project is built only as a sample REST API toolkit.

Fake data was generated from cool https://www.mockaroo.com source.

## Tools
> - `python 3.8`
> - `RESTful API` approach
> - `pytest`

## Usage
Run next command from the root of the project:
```bash
~ python vehicle_api.py
```

### API endpoints
There are several endpoints already developed (others will be added soon):
  - `GET` request on `/rest` endpoint to get list of all vehicles e.g:
    > `curl localhost:5000/rest`
  - `POST` request on `/rest` endpoint to create a vehicle e.g:
    > `curl -X POST \` \
    `-H "Content-type: application/json \"` \
    `-d {"manufacturer": "BMW", "model": "X5", "year": 2011, "vin": "WBAWV53589P465532"}' \` \
    `localhost:5000/rest`
  - `GET` request on `/rest/{id}` endpoint to get single vehicle e.g:
    > `curl localhost:5000/rest/99`
  - `PUT` request on `/rest/{id}` endpoint to update single vehicle e.g:
    > `curl -X PUT \` \
    `-H "Content-type: application/json" \` \
    `-d '{"manufacturer": "BMW", "model": "X5", "year": 2011, "vin": "WBAWV53589P465532"}' \` \
    `localhost:5000/rest/99`
  - `DELETE` request on `/rest/{id}` to delete single vehicle e.g:
    > `curl -X DELETE localhost:5000/rest/99`

### Testing
Project is covered with both **_unittests_** on code basis and **_functional_** tests on REST API endpoints with [pytest](https://docs.pytest.org/en/latest) testing framework.
It uses [pytest.ini](pytest.ini) configuration file.

Please run next command from the root directory to start testing:
```bash
~ pytest
```
> If you would like to run only `smoke` tests or `unittests` please run tests with corresponding marker e.g:
> 
>`~ pytest -m smoke`

Please open `test-report.html` file in your browser to see testing report.

### Debugging
In case of code debugging we use a contemporary [pdb++](https://pypi.org/project/pdbpp) package as an easy-way to track your code.
It is wrapper of a builtin [pbd](https://docs.python.org/3/library/pdb.html) package but with features extensions.

To make it work just install it from `requirements-dev.txt` file and use [breakpoint()](https://docs.python.org/3/library/functions.html#breakpoint) function call e.g:
```python
class A:    
    def do_debug(self) -> None:
        self_: "A" = self
        breakpoint()

a: A = A()
a.do_debug()
```

To be able debug your application please pass `debug=True` parameter into `Setup` object while running an app e.g:
```python
if __name__ == "__main__":
    _run_vehicle_api(Setup(debug=True))
```

## Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `pip install -r requirements.txt` to install all project dependencies
- `pip install -r requirements-dev.txt` to install all development dependencies
