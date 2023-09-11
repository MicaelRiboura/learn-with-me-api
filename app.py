from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from modules.shared.config.db_sqlite import Session, User, StudyTrail, Item
from flask_cors import CORS

# schemas
from modules.shared.errors.error_schema import ErrorSchema
from modules.user.schemas import UserSchema, UserResponseSchema

# usecases
from modules.user.use_cases import create_user

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# ----------------------------- Home Route -----------------------------
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# ----------------------------- Users Routes -----------------------------
user_tag = Tag(name="Usuários", description="Criação e visualização de usuários à base de dados.")

@app.post('/user/create', tags=[user_tag], responses={'200': UserResponseSchema, '400': ErrorSchema})
def create_user_route(form: UserSchema):
    """
        Cria novo usuário
    """
    return create_user(form)


