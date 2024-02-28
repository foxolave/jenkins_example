# jenkins_example

Запуск приложения:
```shell
docker build -f Dockerfile -t local_app .
docker run -d --name python_example_latest -p "5000:5000/tcp" local_app
```

Запуск юнит-теста
```shell
docker build -f Dockerfile.unit_test -t unit_test .
docker run --rm --name unit_test unit_test
```

Запуск чек-стайла
```shell
docker run -ti --rm -v app.py:/apps/app.py alpine/flake8 app.py
```