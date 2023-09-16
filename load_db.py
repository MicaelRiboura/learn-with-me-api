from modules.shared.config.db_sqlite import Session
from modules.user.models import User
from modules.study_trail.models import StudyTrail, Item

def load_db():

    session = Session()

    users = [
        User(name="Nauke", email="nauke@mail.com", password="123456"),
        User(name="Galdir", email="galdir@mail.com", password="123456"),
        User(name="Deysoku", email="deysoku@mail.com", password="123456"),
        User(name="Bugrli", email="bugrli@mail.com", password="123456"),
        User(name="Mexudir", email="mexudir@mail.com", password="123456"),
        User(name="Pacul", email="pacul@mail.com", password="123456"),
        User(name="Zizan", email="zizan@mail.com", password="123456"),
        User(name="Reythza", email="reythza@mail.com", password="123456"),
        User(name="Wevuolg", email="wevuolg@mail.com", password="123456"),
        User(name="Wuol", email="wuol@mail.com", password="123456"),
    ]

    # create users
    session.add_all(users)

    # create study trails
    study_trails = [
        {
            'request': StudyTrail(
                title='Fundamentos de JavaScript',
                description='Aprenda os fundamentos da linguagem JavaScript',
            ),
            'user': users[0],
        },
        {
            'request': StudyTrail(
                title='Fundamentos de Python',
                description='Aprenda os fundamentos da linguagem Python',
            ),
            'user': users[4],
        },
        {
            'request': StudyTrail(
                title='Fundamentos de React',
                description='Aprenda os fundamentos da biblioteca/framework React',
            ),
            'user': users[2],
        },
    ]

    study_trails_response = []

    for study_trail_i in study_trails:
        study_trail_i['user'].add_study_trail(study_trail_i['request'])
        study_trails_response.append(study_trail_i['request'])

    
    # create items
    items = [
        {
            'request': Item(
                title='Hello World',
                type='text',
                description='Aprenda os fundamentos da linguagem JavaScript',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[0],
        },
        {
            'request': Item(
                title='Constantes',
                type='text',
                description='Aprenda os fundamentos da linguagem JavaScript',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[0],
        },
        {
            'request': Item(
                title='Funções',
                type='text',
                description='Aprenda os fundamentos da linguagem JavaScript',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[0],
        },
        {
            'request': Item(
                title='Hello World',
                type='text',
                description='Aprenda os fundamentos da linguagem Python',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[1],
        },
        {
            'request': Item(
                title='Constantes',
                type='text',
                description='Aprenda os fundamentos da linguagem Python',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[1],
        },
        {
            'request': Item(
                title='Funções',
                type='text',
                description='Aprenda os fundamentos da linguagem Python',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[1],
        },
        {
            'request': Item(
                title='Hello World',
                type='text',
                description='Aprenda os fundamentos de React',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[2],
        },
        {
            'request': Item(
                title='Constantes',
                type='text',
                description='Aprenda os fundamentos de React',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[2],
        },
        {
            'request': Item(
                title='Funções',
                type='text',
                description='Aprenda os fundamentos de React',
                resource='https://www.youtube.com/watch?v=HdunotFeGas',
            ),
            'study_trail': study_trails_response[2],
        },
    ]

    for item_i in items:
        item_i['study_trail'].add_item(item_i['request'])
    
    session.commit()

load_db()
