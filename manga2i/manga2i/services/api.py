import requests    
import logging as log
from .. import models as mod

def dict_to_class_manga(manga_data):

    tags = [mod.Tag(id=tag["id"], type=tag["type"], attributes=mod.TagAttributes(
        name=tag["attributes"]["name"],
        description=tag["attributes"]["description"],
        group=tag["attributes"]["group"],
        version=tag["attributes"]["version"]
    )) for tag in manga_data["attributes"]["tags"]]

    url_api = "https://api.mangadex.org/"
    url_api_cover = url_api+"cover"
    id_manga = manga_data["id"]

    cover_art_id = next(
        (relationship["id"] for relationship in manga_data["relationships"] if relationship["type"] == "cover_art"),
        None  
    )

    params = {
        "ids[]": cover_art_id
    }

    response = requests.get(url_api_cover, params=params)

    data = response.json()

    file_names = [item["attributes"]["fileName"] for item in data.get("data", [])]

    url_image="https://mangadex.org/covers"

    cover_url = url_image+"/"+id_manga+"/"+file_names[0]

    r = requests.get(f"{url_api}/statistics/manga/{id_manga}")

    grade = r.json()["statistics"][id_manga]['rating']['average']

    attributes = mod.Attributes(
        title=manga_data["attributes"]["title"]["en"],
        description=manga_data["attributes"]["description"]["en"],
        originalLanguage=manga_data["attributes"]["originalLanguage"],
        lastVolume=manga_data["attributes"]["lastVolume"],
        lastChapter=manga_data["attributes"]["lastChapter"],
        publicationDemographic=manga_data["attributes"]["publicationDemographic"],
        status=manga_data["attributes"]["status"],
        year=manga_data["attributes"]["year"],
        grade=round(grade,2),
        tags=tags,
        availableTranslatedLanguages=manga_data["attributes"]["availableTranslatedLanguages"],
        url_cover=cover_url
    )

    manga = mod.Manga(
        id=id_manga,
        type=manga_data["type"],
        attributes=attributes
    )

    return manga

def get_mangas(offset):
    base_url = "https://api.mangadex.org"

    order = {"rating": "desc"}

    final_order_query = {}

    for key, value in order.items():
        final_order_query[f"order[{key}]"] = value

    r = requests.get(
        f"{base_url}/manga",
        params={
            **{"limit": 20, "offset": offset},
            **final_order_query,
        }
    )


    manga_request = r.json()["data"]

    manga_list = []
    
    for manga_dict in manga_request:
        try:
            manga_list.append(dict_to_class_manga(manga_dict))
        except Exception as e:
            log.error(f"Erreur avec le manga {manga_dict.get('id', 'inconnu')}: {e}")

    return manga_list

def get_manga_by_id(manga_id):
    base_url = "https://api.mangadex.org"


    r = requests.get(
        f"{base_url}/manga/{manga_id}",
    )

    try:
        manga = dict_to_class_manga(r.json()["data"])
        
        return manga
    except Exception as e:
        log.error(f"Erreur avec le manga {manga_id}: {e}")

    

    