
import os
import json
from contextlib import contextmanager

chess_players = [
  {"id": 19, "name": "Jobava", "country": "Georgia", "rating": 2588, "age": 41},
  {"id": 28, "name": "Caruana", "country": "USA", "rating": 2781, "age": 32},
  {"id": 35, "name": "Giri", "country": "Netherlands", "rating": 2771, "age": 30},
  {"id": 84, "name": "Carlsen", "country": "Norway", "rating": 2864, "age": 34},
  {"id": 118, "name": "Ding", "country": "China", "rating": 2799, "age": 32},
  {"id": 139, "name": "Karjakin", "country": "Russia", "rating": 2747, "age": 35},
  {"id": 258, "name": "Duda", "country": "Poland", "rating": 2731, "age": 31},
  {"id": 301, "name": "Vachier-Lagrave", "country": "France", "rating": 2737, "age": 34},
  {"id": 403, "name": "Nakamura", "country": "USA", "rating": 2768, "age": 36},
]

with open("test.json", "w", encoding="utf-8") as f:
    json.dump(chess_players, f, ensure_ascii=False, indent=2)

@contextmanager
def file_path_manager(filename: str):
    full_path = os.path.abspath(filename)
    try:
        yield full_path
    finally:
        pass



def read_file_content(filename: str) -> list[dict]:
    with file_path_manager(filename) as path:
        if not os.path.exists(path):
            raise FileNotFoundError(f"ფაილი არ მოიძებნა:{path}")
        
        with open(path, "r", encoding='utf-8') as f:
            return json.load(f)
        


def append_to_file(filename:str, new_entries:list[dict]) -> None:
    with file_path_manager(filename) as path:
        existing_data = read_file_content(filename)

        for entry in new_entries:
            existing_data.append(entry)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii = False, indent=2)

def update_file(filename:str, player_id:int, updated_fields:dict) -> None:
    with file_path_manager(filename) as path:
        existing_data = read_file_content(filename)

        for player in existing_data:
            if player["id"] == player_id:
                player.update(updated_fields)
                break

        else:
            raise ValueError(f"მოთამაშე ID={player_id} ვერ მოიძებნა")
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)



new_players = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

append_to_file("test.json", new_players)
update_file("test.json", player_id=568, updated_fields={"rating": 2812, "age": 57})


print(json.dumps(read_file_content("test.json"), ensure_ascii=False, indent=2))
