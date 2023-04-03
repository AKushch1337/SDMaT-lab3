from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'msg': 'Hello, World!',
        'name': 'Artem',
        'surname': 'Kushch',
        'group': 'IM-13',
        'faculty': 'FICE',
        'uni': 'KPI'
        }
