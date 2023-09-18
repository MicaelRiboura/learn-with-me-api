from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from modules.shared.config.db_sqlite import *
from flask_cors import CORS

# schemas
from modules.shared.errors.error_schema import ErrorSchema
from modules.study_trail.schemas import \
    CreateStudyTrailSchema, \
    CreateItemSchema, \
    CreateStudyTrailResponseSchema, \
    ItemResponseSchema, \
    ListStudyTrailsSchema, \
    ListStudyTrailsQuerySchema, \
    ListStudyTrailsByUserQuerySchema, \
    StudyTrailResponseSchema, \
    GetStudyTrailSchema, \
    DeleteItemSchema, \
    DeleteResponseSchema
from modules.user.schemas import UserSchema, UserResponseSchema, UserLoginSchema

# usecases
from modules.user.use_cases import create_user, login
from modules.study_trail.use_cases import \
    create_study_trail, \
    create_item, \
    list_study_trails, \
    list_study_trails_by_user, \
    get_study_trail, \
    delete_study_trail, \
    delete_item

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
user_tag = Tag(name="Usuário", description="Criação e login de usuários à base de dados.")

@app.post('/users/create', tags=[user_tag], responses={'200': UserResponseSchema, '409': ErrorSchema, '400': ErrorSchema})
def create_user_route(form: UserSchema):
    """
        Cria novo usuário
    """
    return create_user(form)

@app.post('/users/login', tags=[user_tag], responses={'200': UserResponseSchema, '400': ErrorSchema, '500': ErrorSchema})
def login_route(form: UserLoginSchema):
    """
        Faz o login de um usuário com seu e-mail e senha.
    """
    return login(form)


# ----------------------------- Study Trails Routes -----------------------------
study_trail_tag = Tag(name="Trilha de Estudo", description="Adição, visualização e deleção de tilhas de estudo à base de dados.")

@app.post('/study_trails/create', tags=[study_trail_tag], responses={'200': CreateStudyTrailResponseSchema, '400': ErrorSchema, '404': ErrorSchema})
def create_study_trail_route(form: CreateStudyTrailSchema):
    """
        Cria nova trilha de estudos
    """
    return create_study_trail(form)

@app.get('/study_trails/list', tags=[study_trail_tag], responses={'200': ListStudyTrailsSchema, '404': ErrorSchema})
def list_study_trails_route(query: ListStudyTrailsQuerySchema):
    """
        Lista trilhas de estudos: todas ou filtrando por titulo
    """
    return list_study_trails(query)

@app.get('/study_trails/user', tags=[study_trail_tag], responses={'200': ListStudyTrailsSchema, '404': ErrorSchema})
def list_study_trails_by_user_route(query: ListStudyTrailsByUserQuerySchema):
    """
        Lista trilhas de estudos de um usuário
    """
    return list_study_trails_by_user(query)

@app.get('/study_trails/one', tags=[study_trail_tag], responses={'200': StudyTrailResponseSchema, '404': ErrorSchema})
def get_study_trail_route(query: GetStudyTrailSchema):
    """
        Mostra uma trilha de estudos através de seu identificador
    """
    return get_study_trail(query)

@app.delete('/study_trails/delete', tags=[study_trail_tag], responses={'200': DeleteResponseSchema, '404': ErrorSchema})
def delete_study_trail_route(query: GetStudyTrailSchema):
    """
        Remove uma trilha de estudos através de seu identificador
    """
    return delete_study_trail(query)

# ----------------------------- Items Routes -----------------------------
item_tag = Tag(name="Item de Estudo", description="Adição, visualização e deleção de itens de estudo à base de dados.")

@app.post('/items/create', tags=[item_tag], responses={'200': ItemResponseSchema, '400': ErrorSchema, '404': ErrorSchema})
def create_item_route(form: CreateItemSchema):
    """
        Cria novo item na trilha de estudos
    """
    return create_item(form)

@app.delete('/items/delete', tags=[item_tag], responses={'200': DeleteResponseSchema, '404': ErrorSchema})
def delete_item_route(query: DeleteItemSchema):
    """
        Remove um item na trilha de estudos através de seu identificador
    """
    return delete_item(query)