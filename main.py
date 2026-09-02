from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.pessoa_route import router as pessoa_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

app.include_router(pessoa_router)

"""
    PARA EXECUTAR O PROJETO DIGITE A LINHA DE COMANDO:
    uvicorn main:app --reload

    python -m  uvicorn main:app --reload
"""