📚 Financial Advisor Chatbot API Documentation
Welcome to the Financial Advisor Chatbot API! This FastAPI application allows you to interact with a database created from CSV files through chat-like queries, providing financial advice. Follow the steps below to get started. 🚀

📁 Prerequisites
Data Folder: Ensure that a data folder exists in the root directory of your project. This folder should contain the CSV files used to create the database.
Environment Variables: Set the OPENAI_API_KEY environment variable with your OpenAI API key.
🚀 Getting Started
Step 1: Create the Database
The create-database endpoint should be called only once to create the database from the CSV files.

bash
Copiar código
curl -X POST "http://127.0.0.1:8000/create-database/"
Step 2: Interact with the Database
Use the chat-with-database endpoint to query the database.

bash
Copiar código
curl -X POST "http://127.0.0.1:8000/chat-with-database/" -H "Content-Type: application/json" -d '{
  "client_id": "your_client_id",
  "question": "your_query",
  "openai_model": "text-davinci-003",
  "temperature": 0.7
}'
📜 API Endpoints
1. /create-database/ (POST)
This endpoint initializes the SQLite database from the CSV files located in the data folder.

Response
200 OK: Database created successfully.
500 Internal Server Error: Error details.
Example
bash
Copiar código
curl -X POST "http://127.0.0.1:8000/create-database/"
2. /chat-with-database/ (POST)
This endpoint allows you to query the database using a chat interface.

Request Body
client_id (str): The client ID.
question (str): The query to ask the database.
openai_model (str): The OpenAI model to use for generating responses.
temperature (float): The temperature setting for the model.
Response
200 OK: The response message from the database.
500 Internal Server Error: Error details.
Example
bash
Copiar código
curl -X POST "http://127.0.0.1:8000/chat-with-database/" -H "Content-Type: application/json" -d '{
  "client_id": "your_client_id",
  "question": "your_query",
  "openai_model": "text-davinci-003",
  "temperature": 0.7
}'
🛠️ Setup
Clone the repository:

bash
Copiar código
git clone <repository_url>
cd <repository_folder>
Install dependencies:

bash
Copiar código
pip install -r requirements.txt
Run the application:

bash
Copiar código
uvicorn src.main:app --reload
Ensure data folder exists and contains the necessary CSV files.

Call the create-database endpoint once to initialize the database.

Interact with the chat-with-database endpoint for querying the database.

📂 Project Structure
css
Copiar código
├── data/
│   ├── your_csv_file1.csv
│   ├── your_csv_file2.csv
│   └── ...
├── src/
│   ├── main.py
│   ├── sqlite_database_creator.py
│   ├── models.py
│   └── agents.py
├── db/
│   └── chat.db
├── requirements.txt
└── README.md
📝 Notes
Make sure the data folder exists and contains the necessary CSV files before running the create-database endpoint.
The database creation should be done only once. Subsequent calls to the create-database endpoint may result in errors.
🔗 References
FastAPI Documentation
Uvicorn Documentation
OpenAI API Documentation
Feel free to reach out for any questions or issues. Happy coding! 🎉