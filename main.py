from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix=settings.API_V1_STR)

from app.db.init_db import init_db

# Check if the project has been initialized before
if settings.ENV == "development":
    init_db()

# delete all folders __pycache__ in the project
# `FOR /R . %G IN (__pycache__) DO (IF EXIST "%G" (RMDIR /S /Q "%G"))`

# uninstall all packages in environment python
# `for /F %i in ('pip freeze') do pip uninstall -y %i`

# install all packages in requirements.txt
# `pip install -r requirements.txt`
