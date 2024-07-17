from fastapi import FastAPI
from app.database import engine, Base
from app.controllers import category_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS para permitir acesso do frontend
origins = ["http://localhost:4200"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inclusão dos routers dos controladores
app.include_router(category_controller.router, prefix="/api", tags=["categories"])