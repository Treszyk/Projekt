import fastapi
from fastapi_chameleon import template
import requests as re

router = fastapi.APIRouter()


@router.get('/poke_list')
@template(template_file='poke_list.pt')
async def poke_list(page: int = 0):
    x = re.get(f'https://pokeapi.co/api/v2/pokemon/?offset={18*page}&limit=18')
    xd = x.json()
    d = {}
    print(xd['count'])
    for poke in xd['results']:
        r = re.get(poke['url'])
        d[poke['name']] = r.json()
    pages_num = xd['count'] // 18

    return {"message": xd, "jd": [15,13,14,12], "pokemons": xd, "pok": d, "pages_num": pages_num}