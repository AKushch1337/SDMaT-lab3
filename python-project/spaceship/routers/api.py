from fastapi import APIRouter
import numpy as np

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

@router.get('/matrix')
def matrix() -> dict:
    matrix1 = np.random.rand(10, 10)
    matrix2 = np.random.rand(10, 10)
    result = np.matmul(matrix1, matrix2)
    return {
        'matrix1': matrix1.tolist(),
        'matrix2': matrix2.tolist(),
        'result': result.tolist()
    }