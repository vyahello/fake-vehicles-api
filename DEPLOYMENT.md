Heroku deployment
===============

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