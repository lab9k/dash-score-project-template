from app import app, server
from routes import create_render_function
from environment import settings

if __name__ == '__main__':
    create_render_function(app)
    app.run_server(debug=settings.DEBUG is not None)
