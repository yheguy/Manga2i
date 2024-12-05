import requests    
import logging as log
from .. import models as mod

def get_cover_manga(manga_data):

    url_api_cover = "https://api.mangadex.org/cover"
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

    return url_image+"/"+id_manga+"/"+file_names[0]


def get_grade_manga(id_manga):
    url_api = "https://api.mangadex.org/"

    r = requests.get(f"{url_api}/statistics/manga/{id_manga}")

    return r.json()["statistics"][id_manga]['rating']['average']


def fetch_and_update_mangas(offset):
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

    if r.status_code == 200:
        manga_request = r.json()["data"]
        
        for manga_data in manga_request:
            manga_id = manga_data["id"]
            try:  
                if not mod.Manga.objects.filter(id=manga_id).exists():
                    manga = mod.Manga(
                        id=manga_id,
                        title=manga_data["attributes"]["title"]["en"],
                        description=manga_data["attributes"]["description"]["en"],
                        original_language=manga_data["attributes"]["originalLanguage"],
                        last_volume=manga_data["attributes"]["lastVolume"],
                        last_chapter=manga_data["attributes"]["lastChapter"],
                        status=manga_data["attributes"]["status"],
                        year=manga_data["attributes"]["year"],
                        grade=round(get_grade_manga(manga_id),2),
                        url_cover=get_cover_manga(manga_data),
                        price=6.99,
                        stock=0,
                    )
                    
                    manga.save()
                    print(f"Manga ajouté : {manga.title}")
            except Exception as e:
                log.error(f"Erreur avec le manga {manga_id}: {e}")
    

    