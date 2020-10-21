# Create a file that will serve as the entry point for our application.
# This will tell the uWSGI server how to interact with it

from app.main import create_app, db

app = create_app('development')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
