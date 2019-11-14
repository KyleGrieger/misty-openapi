import connexion
from connexion.resolver import RestyResolver

app = connexion.App(__name__)
app.add_api('../../reference/misty-api.v1.yaml')
app.run(server='tornado', port=3000)
