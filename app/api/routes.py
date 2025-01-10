from fastapi import FastAPI, File, UploadFile, HTTPException
from app.services.file_processor import process_file
from fastapi.responses import JSONResponse
import os
import json

app = FastAPI()

JSON_FILES_DIR = "app/data/json_files/"


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    API endpoint to upload and process a file.

    Args:
        file (UploadFile): The uploaded file from the client.

    Returns:
        dict: Processed data from the file.
    """
    try:
        # Read the file content
        content = await file.read()

        # Process the file content using the original file name
        processed_data = process_file(content, file.filename)

        # Return JSON response
        return {"status": "success", "data": processed_data}
    except ValueError as e:
        # Handle known errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

@app.get("/get-json/{file_name}")
async def get_json_file(file_name: str):
    """
    API endpoint to retrieve a JSON file by name (from the URL path).

    Args:
        file_name (str): Name of the JSON file to retrieve.

    Returns:
        JSONResponse: The contents of the JSON file.
    """
    try:
        # Construct the full path to the JSON file
        file_path = os.path.join(JSON_FILES_DIR, file_name)

        # Check if the file exists
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="JSON file not found.")

        # Read and parse the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)

        # Return the JSON data
        return JSONResponse(content=data)
    except FileNotFoundError:
        # Handle missing file error
        raise HTTPException(status_code=404, detail="JSON file not found.")
    except json.JSONDecodeError:
        # Handle JSON parsing error
        raise HTTPException(status_code=400, detail="Error decoding JSON file.")
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")