from app import create_app
app = create_app() 

if __name__ == "__main__":
    # This block allows you to run the app using 'python wsgi.py' for convenience
    # (though 'flask run' is usually preferred for development).
    app.run()