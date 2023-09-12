from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from modules.shared.config.db_sqlite import Session, User, StudyTrail, Item
from flask_cors import CORS

# schemas
from modules.shared.errors.error_schema import ErrorSchema
from modules.user.schemas import UserSchema, UserResponseSchema, UserLoginSchema
from modules.study_trail.schemas import StudyTrailSchema

# usecases
from modules.user.use_cases import create_user, login
from modules.study_trail.use_cases import create_study_trail

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

@app.post('/user/create', tags=[user_tag], responses={'200': UserResponseSchema, '409': ErrorSchema, '400': ErrorSchema})
def create_user_route(form: UserSchema):
    """
        Cria novo usuário
    """
    return create_user(form)

@app.post('/user/login', tags=[user_tag], responses={'200': UserResponseSchema, '400': ErrorSchema, '500': ErrorSchema})
def login_route(form: UserLoginSchema):
    """
        Faz o login de um usuário com seu e-mail e senha.
    """
    return login(form)


# ----------------------------- Study Trails Routes -----------------------------
study_trail_tag = Tag(name="Trilha de Estudo", description="Adição, visualização e deleção de tilhas de estudo à base de dados.")

@app.post('/study_trails/create', tags=[study_trail_tag])
def create_study_trail_route(form: StudyTrailSchema):
    """
        Cria nova trilha de estudos
    """
    return create_study_trail(form)