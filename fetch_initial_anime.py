import httpx
from consts import QUERY


def fetch_top_anime() -> list:
    """Fetches data on the top 250 anime by score from the AniList API."""
    anime_list = []
    base_url = "https://graphql.anilist.co"

    
    for page in range(1, 6):
        variables = {
            "page": page
        }

        response = httpx.post(f"{base_url}", json={"query": QUERY, "variables": variables})
        response = response.json()

        media_list = response["data"]["Page"]["media"]
        anime_list.extend(media_list)

    return anime_list


fetch_top_anime()