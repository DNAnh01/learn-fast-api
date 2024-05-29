import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.db.init_db import init_db

app = FastAPI()

# Add SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

# Check if the project has been initialized before
if settings.ENV in ["development", "testing"]:
    init_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



# delete all folders __pycache__ in the project
# `FOR /R . %G IN (__pycache__) DO (IF EXIST "%G" (RMDIR /S /Q "%G"))`

# uninstall all packages in environment python
# `for /F %i in ('pip freeze') do pip uninstall -y %i`

# install all packages in requirements.txt
# `pip install -r requirements.txt`

# remove all unused imports and variables in the project
# `autoflake --remove-all-unused-imports --remove-unused-variables --in-place --recursive .`