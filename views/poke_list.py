import fastapi
from fastapi_chameleon import template
import requests as re
import math

router = fastapi.APIRouter()


@router.get('/poke_list')
@template(template_file='poke_list.pt')
async def poke_list(page: int = 0):
    page = abs(page)
    if page > 0:
        page-=1
    resp = re.get(f'https://pokeapi.co/api/v2/pokemon/?offset={18*page}&limit=18')
    re_json = resp.json()
    pokemons = {}
    print(re_json['count'])
    for poke in re_json['results']:
        r = re.get(poke['url'])
        pokemons[poke['name']] = r.json()
    pages_num = math.ceil(re_json['count'] / 18)

    return {"jd": [15,13,14,12], "json": re_json, "pok": pokemons, "pages_num": pages_num, "curr_page": page}