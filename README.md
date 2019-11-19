# Misty OpenAPI

The Misty Robot OpenAPI spec

## Client

Set up [openapi-generator](https://github.com/OpenAPITools/openapi-generator#2---getting-started).

Generate a client library:

	java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
	  -i {path}/{to}/reference/misty-api.yaml \
	  -g {client language generator} \
	  -o {path}/{to}/{output}/{client}/{lib folder}


- The list of client language generators can be found [here](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators.md).

- Feel free to fork this repo, change the Misty OpenAPI spec and add your own functionality.

- [Stoplight](https://stoplight.io/) is an excellent tool for adding/editing openapi schemas.

## Server

Use Python 3

### Installation

	pip install -r servers/{your-device}/requirements.txt

### Usage

	python servers/{your-device}/server.py

ex.

	python servers/jetbot/server.py

- The api should now be served at http://{host ip}:3000

- There is a user interface with documentation about the available paths that is served at http://{host ip}:3000/ui

#### Notes

The server uses [connextion](https://github.com/zalando/connexion) which uses Python Flask. Other webservers can also be used.  Additionally [connexion](https://github.com/zalando/connexion) supports setting up [authentication](https://github.com/zalando/connexion#oauth-2-authentication-and-authorization) and [SSL](https://github.com/zalando/connexion#https-support)!  `x-openapi-router-controller` defines the module where the implementation is for the path/route. The `operationId` defines the function name.  So `x-openapi-router-controller: api` and `operationId: drive` means that the implementation for the drive path/route is in the function `drive()` and file api.py.  Feel free to fork this repo, extend, modify or implement your own robot api using the Misty API!

## TODO 
- Add websocket endpoint /pubsub
- Add support for the rest of the Misty API
- Generate "cleaner" client libraries where objects are not generic InlineObject and DefaultApi is renamed
- Implement support fo Jetbot
- Create documentation for assembling and setting up other devices
