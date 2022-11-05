import pymongo
from dataclasses import dataclass, asdict


@dataclass
class Photo:
    url: str

    def to_dict(self):
        return asdict(self)


class MongoManager:
    def __init__(self):
        self._client = pymongo.MongoClient("mongodb://localhost:27017/")

        media_db = self._client["media_db"]
        self.photo_collection = media_db["photos"]

    def add(self, photo: Photo):
        response = self.photo_collection.insert_one(photo.to_dict())

        return response

    def get(self):
        response = self.photo_collection.find_one()

        return response