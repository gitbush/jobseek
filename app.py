import os
from jobseek import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=os.getenv("PORT"),
            debug=True)