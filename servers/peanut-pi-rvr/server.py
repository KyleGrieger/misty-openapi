import connexion
from connexion.resolver import RestyResolver

#def drive_get(message):
#    # do something
#    print device
#    return 'You send the message: {}'.format(message), 200

app = connexion.App(__name__, specification_dir='../reference/')
app.add_api('../reference/misty-api.v1.yaml')
app.run(server='tornado', port=3000)
