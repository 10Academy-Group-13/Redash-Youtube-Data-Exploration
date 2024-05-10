import os
import openai
from IPython.display import Markdown, display
from llama_index.core import SQLDatabase
from llama_index.llms.openai import OpenAI
import sqlalchemy
import psycopg2
import requests
import os
from dotenv import load_dotenv

# Set the OPENAI_API_KEY environment variable to your OpenAI API key
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Assign the value of the OPENAI_API_KEY environment variable to the openai.api_key attribute
# This is necessary for authenticating requests to the OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the database connection parameters
db_name = "postgres"  # Name of the database to connect to
db_user = "postgres"  # Username for the database connection
db_password = "postgres"  # Password for the database connection
db_host = "localhost"  # Hostname where the database server is running

# Establish a connection to the PostgreSQL database using the defined parameters
connection = psycopg2.connect(
    dbname=db_name,  # Specify the database name
    user=db_user,  # Specify the username
    password=db_password,  # Specify the password
    host=db_host  # Specify the host
)

# Create a cursor object using the connection
cursor = connection.cursor()

# Function to convert a natural language query prompt into a SQL query
def question_to_prompt(natural_language_query):
    template = ""
    # Placeholder for NLP conversion logic to SQL
        
    return template


# Function to send a prompt to the OpenAI API and receive a SQL query in response
def get_sql_query(prompt, api_key, model="gpt-3.5-turbo"):
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json={
        'messages': [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        'max_tokens': 100,
        'temperature': 0.7,
        'top_p': 1,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0,
        'model': model
    })
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")


# Function to parse the SQL query from the API response
def parse_sql_query(response_json):
    # Extracts the SQL query from the API response
    return response_json['choices'][0]['message']['content'].strip()


# Main function to generate and execute a SQL query based on a natural language question
def generate_and_execute_sql(question, api_key):
    prompt = question_to_prompt(question)
    response_json = get_sql_query(prompt, api_key, model="gpt-3.5-turbo")
    parsed_sql_query = parse_sql_query(response_json)
    # Placeholder for executing the parsed SQL query against a database
    # This part of the function should be implemented to actually run the SQL query
    print(parsed_sql_query)


# Function call
api_key = os.environ["OPENAI_API_KEY"] 
question = "What is the total view from 'Addis Ababa'?"
generate_and_execute_sql(question, api_key)