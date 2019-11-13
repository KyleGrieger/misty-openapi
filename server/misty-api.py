import connexion

def drive_get(message):
    # do something
    print device
    return 'You send the message: {}'.format(message), 200

app = connexion.App(__name__, specification_dir='../reference/')
app.run(server='tornado', port=3000)
