import fastapi
from fastapi_chameleon import template
import requests as re

router = fastapi.APIRouter()


@router.get('/poke_detail/{poke_name}')
@template(template_file='poke_detail.pt')
async def poke_detail(poke_name: str):
    url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
    r = re.get(url)
    poke = r.json()

    return {"pokemon": poke}