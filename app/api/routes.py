from fastapi import FastAPI, File, UploadFile, HTTPException
from app.services.file_processor import process_file

app = FastAPI()

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
