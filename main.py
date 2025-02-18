from fastapi import FastAPI, Query
import requests
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# url = f"https://anime-db.p.rapidapi.com/anime/by-id/{anime_id}"

# response = requests.get(url, headers=headers)

# print(response.json())
headers = {
    "x-rapidapi-key": "2167dda3fdmshdf89b78bf25585dp1479aejsn050fa0e1a153",
    "x-rapidapi-host": "anime-db.p.rapidapi.com"
}


@app.get("/by_id/{anime_id}")
async def get_by_id(anime_id: int):
    url = f"https://anime-db.p.rapidapi.com/anime/by-id/{anime_id}"
    response = requests.get(url, headers=headers)
    return response.json()


@app.get("/by_ranking/{by_ranking}")
async def get_by_ranking(by_ranking: int):
    url = f"https://anime-db.p.rapidapi.com/anime/by-ranking/{by_ranking}"
    response = requests.get(url, headers=headers)
    return response.json()


@app.get("/genre")
async def search_by_genres():
    url = "https://anime-db.p.rapidapi.com/genre"
    response = requests.get(url, headers=headers)
    return response.json()


@app.get("/anime/{page}/{by_size}")
async def anime(page: int, by_size: int,
                search: Annotated[str | None, Query(description="Search by title or alternative titles. Search "
                                                                "will ignore sort")] = None,
                genres: str | None = None,
                sortBy: Annotated[str | None, Query(description="Ranking or Title")] = None,
                sortOrder: Annotated[str | None, Query(description="asc or desc")] = None,
                types: Annotated[str | None, Query(description="Anime type, separated by comma")] = None
                ):

    querystring = {
        "page": str(page),
        "size": str(by_size)
    }

    if search:
        querystring["search"] = search

    if genres:
        querystring["genres"] = genres.split(",")  # JSON formatiga mos bo‘lishi uchun

    if sortBy:
        querystring["sortBy"] = sortBy

    if sortOrder:
        querystring["sortOrder"] = sortOrder

    if types:
        querystring["types"] = types

    url = "https://anime-db.p.rapidapi.com/anime"
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
