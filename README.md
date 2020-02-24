# postcode-validator-webapp

[![CircleCI](https://circleci.com/gh/guimunarolo/postcode-validator-webapp.svg?style=shield)](https://circleci.com/gh/guimunarolo/postcode-validator-webapp)
[![codecov](https://codecov.io/gh/guimunarolo/postcode-validator-webapp/branch/master/graph/badge.svg)](https://codecov.io/gh/guimunarolo/postcode-validator-webapp)

A simple webapp to implement [postcode-validator-uk](https://github.com/guimunarolo/postcode-validator-uk)


## Install

```bash
$ git clone git@github.com:guimunarolo/postcode-validator-webapp.git
$ cd postcode-validator-webapp
$ cp local.env .env
$ pipenv shell
$ pipenv install
$ make run
```

Then you should be able to access it at http://localhost:8000


## Running tests

```bash
$ pipenv install --dev
$ make test
```
