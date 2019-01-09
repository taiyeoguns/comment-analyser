from dotenv import load_dotenv
from app import create_app

app = create_app()

# load dotenv
load_dotenv('.env')

if __name__ == "__main__":
    app.run()
