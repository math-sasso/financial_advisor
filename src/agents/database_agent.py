from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from pathlib import Path

class DatabaseAgent:
    def __init__(self, database_file_path: Path, openai_api_key: str, model: str = "gpt-4o", temperature: float = 0.0):
        self.api_key = openai_api_key
        self.model = model
        self.temperature = temperature
        self.database_file_path= database_file_path

        self.db = SQLDatabase.from_uri(f"sqlite:///{self.database_file_path.as_posix()}")
        self.llm = ChatOpenAI(api_key=self.api_key, model=self.model, temperature=self.temperature)
        self.agent = create_sql_agent(self.llm, db=self.db, agent_type="openai-tools", verbose=True, agent_executor_kwargs={"return_intermediate_steps": True})

    def query(self, question: str, client_id: str):
        response = self.agent(question)
        result_log = None

        for intermediate_step in response["intermediate_steps"]:
            tool_action = intermediate_step[0]
            if tool_action.tool == 'sql_db_query_checker':
                result_log = tool_action.log

        if result_log is None:
            raise ValueError("The AI SQL agent failed")

        if client_id not in result_log:
            raise ValueError("AI is probably exposing information from a non desired client")

        return response['output']
