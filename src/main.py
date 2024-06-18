import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
from pathlib import Path
from fastapi.responses import JSONResponse
from .sqlite_database_creator import DatabaseCreator
from .models import ChatWithDatabaseInput
from .agents import DatabaseAgent


app = FastAPI()
data_folder = Path.cwd() / 'data'
database_dirpath = Path.cwd() / "db"
database_filename= 'chat.db'

database_file_path = database_dirpath/ database_filename

@app.post("/create-database/")
def create_database():
    try:
        
        db_creator = DatabaseCreator(data_path=data_folder, db_dirpath=database_dirpath, database_filename=database_filename)
        message = db_creator.create_database_from_csv()
        return JSONResponse(content={"message": message})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat-with-database/")
async def chat_with_database(
    params:ChatWithDatabaseInput,
):
    
    db_agent = DatabaseAgent(
        database_file_path=database_file_path,
        model=params.openai_model,
        openai_api_key=os.environ['OPENAI_API_KEY'],
        temperature=params.temperature
    )

    output = db_agent.query(client_id=params.client_id,question=params.question) 
    return JSONResponse(content={"message": output})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # In the command line run
    # uvicorn src.main:app