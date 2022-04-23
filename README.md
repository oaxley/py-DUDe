# py-DUDe - The DUDe Python Library


![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9.6-blue?style=flat-square)

---

## Presentation

py-DUDe is the Python library to interact with the [DUDe](https://github.com/oaxley/DUDe), a very simplistic user rights management.  

## Pre-requisites

At minimum, you need to have a running instance of the DUDe (the server).  
If your server is running with HTTPS activated, you need to root certificate to validate the communnication.  

Keep the server token (DUDE_SECRET_KEY) on the side as you will need it to use the corresponding admin functions.


## Basic usage

### Library and Server version

The library version is available with

``` python
client = pyDUDe.Client()
print(f'Library version is {client.__version__}')
```

While the server version, is available with

``` python
client = pyDUDe.Client()
print(f'Server version is {client.version()}')
```

Both versions follow the [Semantic Versioning](https://semver.org/).


### Validating a user

If your application, user(s) and right(s) are already registered in the database, checking for them requires 2 steps:

1. Authenticate with the DUDe and retrieve the JSON Web Token
2. Validate your user with the requested right

``` python
# the client to the DUDe server
client = pyDUDe.Client()

# initialize and load the configuration
# from this point onward, your api-key should also be retrieved
# ...

# ... do something

# request a new token from the server
token = client.authenticate(appname='StoryBuilder', apikey='daeabf7c-9345-4af0-abcb-0c3e50b1b3aa')

# validate the user / right for this application
result = client.validate(email='john@acme.com', right='read', token=token)
if result:
    print('User is authorized.')

```

### Admin endpoints

In order to use the administrative endpoints, you must define the variable *x_api_token* in the configuration.  
This corresponds to the *DUDE_SECRET_KEY* when starting the server, and not the *api-key* of your software.

If it's correctly defined, any administrative functions will use it when communicating with the server.

## Functions documentation

The documentation for the available functions is available [here](./docs/index.md)

---

## License

his program is under the **Apache License 2.0**.  
A copy of the license is available [here](https://choosealicense.com/licenses/apache-2.0/).
