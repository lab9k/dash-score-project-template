from app import app, server
from environment import settings

if __name__ == '__main__':
    app.run_server(debug=settings.DEBUG)
