from app import app

from dotenv import load_dotenv

# load dotenv
load_dotenv('.env')

app.run(debug=True)
