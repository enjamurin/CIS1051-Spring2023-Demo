import os
from website import create_app
from flask_migrate import Migrate

app = create_app()

#sets the FLASK_APP environment variable
os.environ['FLASK_APP'] = 'main.py'

if __name__ == '__main__':
    app.run(debug=True)