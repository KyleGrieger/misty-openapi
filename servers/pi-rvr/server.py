import connexion
from flask_cors import CORS

app = connexion.App(__name__)
app.add_api('../../reference/misty-api.yaml')
CORS(app.app)
app.run(port=3000)
