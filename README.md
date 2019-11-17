# Misty OpenAPI
The Misty Robot OpenAPI spec



## Server

Use Python 3.7

### Installation

	pip install -r servers/{your-device}/requirements.txt

###Usage

	python servers/{your-device}/server.py

ex.

	python servers/mock/server.py

## Client

Set up [openapi-generator](https://github.com/OpenAPITools/openapi-generator#2---getting-started).

Generate a client library:

	java -jar modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
	  -i {path}/{to}/reference/misty-api.yaml \
	  -g {client language generator} \
	  -o {path}/{to}/{output}/{client}/{lib}


The list of client language generators can be found [here](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators.md).