# DRF-Authentication

_______________________________________________

Author: Dana Al-Abbade

__________________________________

## Description

Weather API using Django REST Framework with Postgres database. To access the data in the API you must have an access token, using **JWT (JSON Web Token)**.

Django REST Framework works alongside the Django web framework to create web APIs. We cannot build a web API with only Django Rest Framework; it always must be added to a project after Django itself has been installed and configured. The most important takeaway is that Django creates websites containing webpages, while Django REST Framework creates web APIs which are a collection of URL endpoints containing available HTTP verbs that return JSON.

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.

______________________________

## Technologies

* Python 3.7 
* Django 
* Django RESTFRAMEWORK 
* JWT: JSON Web Token
* postgres
* Docker
* Gunicorn