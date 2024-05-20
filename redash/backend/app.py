# Imoprting necessary modules and libraries
import logging
import sys
from IPython.display import Markdown, display
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
from llama_index.core import SQLDatabase
import os
from dotenv import load_dotenv
import openai
from llama_index.core.indices.struct_store.sql_query import NLSQLTableQueryEngine
from llama_index.core import ServiceContext, PromptHelper
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.text_splitter import TokenTextSplitter
from llama_index.core.node_parser import SimpleNodeParser


# Configure the logging module to output log messages to stdout (standard output, usually the terminal).
# The level parameter sets the threshold for what messages will be logged. INFO means that all messages of level INFO and above will be logged.
# force=True ensures that the configuration is applied even if there are other handlers already configured.
logging.basicConfig(stream=sys.stdout, level=logging.INFO, force=True)

# Get the root logger and add a handler to it. This handler will also output log messages to stdout.
# This is done to ensure that log messages are displayed in the environment where the script is running.
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# Define the database credentials and connection details.
db_user = "postgres"
db_password = "postgres"
db_host = "localhost"
db_port = "5432"
db_name = "youtube_data"

# Construct the connection string using the defined credentials and connection details.
# The format is specific to PostgreSQL databases.
connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create an engine instance using the connection string.
# The engine is the starting point for any SQLAlchemy application.
# It's "home base" for the actual database and its DBAPI, delivered to the SQLAlchemy application through a connection pool and a Dialect.
engine = create_engine(connection_string)

# Test the connection to the database by executing a raw SQL query.
# This is done within a context manager to ensure that the connection is properly closed after use.
with engine.connect() as connection:
    # Execute a SQL query to select the first 3 rows from the 'cities_chart' table.
    # The text function is used to create a SQL expression from the provided string.
    result = connection.execute(text("select * from cities_chart limit 3"))

    # Iterate over the result set, printing each row.
    for row in result:
        print(row)

# Descriging each table for accurate SQL
table_details = {
"cities_chart": "Cities chart data",
"cities_table": "Cities table data",
"content_type_chart": "Content type chart data",
"content_type_table ": "Content type data",
"device_type_chart ": "Device type chart data",
"device_type_table ": "Device type table data",
"geography_chart": "Geographyb chart data",
"geography_table": "Geography table data",
"new_and_returning_viewers_chart": "Vew and returning viewers chart data",
"new_and_returning_viewers_table": "New and returning viewers table data",
"operating_system_chart": "Operating system chart data",
"operating_system_table": "Operating system table data",
"sharing_service_chart": "Sharing service chart data",
"sharing_service_table": "Sharing service table data",
"subscription_source_chart": "Subscription source chart data",
"subscription_source_table": "Subscription source table data",
"subscription_status_chart": "Subscription status chart data",
"subscription_status_table": "Subscription status table data",
"subtitles_and_cc_chart": "Subtitles and closed caption chart data",
"subtitles_and_cc_table": "Subtitles and closed caption table data",
"traffic_source_chart": "Traffic source chart data",
"traffic_source_table": "Traffic source table data",
"viewer_age_table": "Viewer age table data",
"viewer_gender_table": "Viewer gender table data",
"viewership_by_age_table": "Viewership by age table data",
"viewership_by_date_table": "Viewership by date table data"
}

# Creating an instance of SQLDatabase with the specified engine and sample_rows_in_table_info parameter set to 2
# Note: The include_tables parameter is commented out, so only the tables specified in the tables list will be included
sql_database = SQLDatabase(engine, sample_rows_in_table_info=2)

# Listing all tables in the SQL database
list(sql_database._all_tables)

# Creating an engine instance for connecting to the PostgreSQL database
# Replace the placeholders with actual database credentials
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Creating a MetaData instance
metadata = MetaData()

# Reflecting the database schema to load table metadata
metadata.reflect(bind=engine)

# Iterating through each table in the database
for table_name, table in metadata.tables.items():
    # Printing the name of the current table
    print(f"Table Name: {table_name}")

    # Printing the names of the columns in the current table
    print(f"Columns: {table.columns.keys()}")

# Load environment variables from.env file
load_dotenv()

# Access OPENAI_API_KEY using os.environ
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Set the OPENAI_API_KEY environment variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Assign the API key to the openai module
openai.api_key = os.environ["OPENAI_API_KEY"]

# Instantiate the OpenAI language model with specific parameters
language_model = OpenAI(model="gpt-3.5-turbo", temperature=0.1)

# Initialize the OpenAIEmbedding model
embedding_model = OpenAIEmbedding()

# Instantiate a TokenTextSplitter for splitting text into chunks
text_splitter_instance = TokenTextSplitter(chunk_size=1024, chunk_overlap=20)

# Initialize a SimpleNodeParser instance
# Note: Modify this line if `text_splitter` is not a valid argument for SimpleNodeParser
node_parser_instance = SimpleNodeParser()

# Instantiate a PromptHelper with specified parameters
prompt_helper_instance = PromptHelper(
    context_window=4096,
    num_output=256,
    chunk_overlap_ratio=0.1,
    chunk_size_limit=None,
)

# Instantiate a ServiceContext with the specified components
service_context_instance = ServiceContext.from_defaults(
    llm=language_model,
    embed_model=embedding_model,
    node_parser=node_parser_instance,
    prompt_helper=prompt_helper_instance,
)

# Creating an instance of NLSQLTableQueryEngine
# This engine is configured with the specified SQL database and service context
query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    service_context=service_context_instance
)

# Defining the query string to ask about the highest view for Addis Ababa
query_str = "when was the highest view in Addis Ababa?"
query_str1 = "which city has the highest view?"
query_str2 = "How long was the video watched in the city that has the first non-zero view?"

# Executing the query using the NLSQLTableQueryEngine
response = query_engine.query(query_str)
response1 = query_engine.query(query_str1)
response2 = query_engine.query(query_str2)

# Printing response
print(response.response)
print(response1.response)
print(response2.response)

# Printing processed SQL query
print(response.metadata['sql_query'])
print()
print(response1.metadata['sql_query'])
print()
print(response2.metadata['sql_query'])