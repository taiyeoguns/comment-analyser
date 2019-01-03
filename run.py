from dotenv import load_dotenv
from app import app

# load dotenv
load_dotenv('.env')

if __name__ == "__main__":
    app.run(debug=True)
