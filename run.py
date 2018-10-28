from app import app
import os

from dotenv import load_dotenv

# load dotenv
load_dotenv('.env')

app.run(debug=True)
