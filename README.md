# Mock vehicle API
A lightweight fake vehicle API written in [API Star](https://docs.apistar.com/) python Web API toolkit framework. 
It is mostly used as a sample API for your project.

Fake data was generated from cool https://www.mockaroo.com source.

## Tools
> - `python 3.8`
> - `RESTful API` approach
> - `pytest`

## Debugging
In case of code debugging we use a contemporary [pdb++](https://pypi.org/project/pdbpp) package as an easy-way to track your code.
It is wrapper of a builtin [pbd](https://docs.python.org/3/library/pdb.html) package but with features extensions.

To make it work just install it from `requirements.txt` file and use [breakpoint()](https://docs.python.org/3/library/functions.html#breakpoint) function call e.g:
```python
class A    
    def do_debug(self) -> None:
        self_: "A" = self
        breakpoint()

a: A = A()
a.do_debug()
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

