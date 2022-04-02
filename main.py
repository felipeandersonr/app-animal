from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from random import randint


class Animal(BaseModel):
    id: Optional[int]
    name: str
    age: int
    sex: str
    color: str


app = FastAPI()


animal_list: List[Animal] = []


@app.get("/animals")
async def show_animals():
    return animal_list


@app.post("/animals")
async def create_animal(animal: Animal):
    animal.id = randint(1, 999)
    animal_list.append(animal)

    return "Animal adicionado com sucesso!"


@app.get("/animals/{id}")
async def show_animals_by_id(id: int):
    for animal in animal_list:
        if animal.id == id:
            return animal

    return "Este id não corresponde a um animal adicionado."


@app.delete("/animals/{id}")
async def delete_animal_by_id(id: int):
    for index, animal in enumerate(animal_list):
        if animal.id == id:
            animal_list.pop(index)

            return "Animal removido com sucesso!"

    return "Este id não corresponde a um animal adicionado."
