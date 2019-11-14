import connexion
from connexion.resolver import RestyResolver

app = connexion.App(__name__)
app.add_api('../../reference/misty-api.yaml')
app.run(server='tornado', port=3000)
