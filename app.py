import os
from jobseek import app, routes

if __name__ == "__main__":
    app.run(host=("0.0.0.0"),
            port=os.getenv("PORT"),
            debug=True)