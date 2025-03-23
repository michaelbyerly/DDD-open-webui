#!/usr/bin/env python
import uvicorn

if __name__ == "__main__":
    # "app.main:app" means we're importing the 'app' instance from the main.py file inside the app folder.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
