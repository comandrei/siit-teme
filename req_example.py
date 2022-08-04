from tqdm import tqdm
import requests


for _ in tqdm(range(100)):
    response = requests.get("https://api.chucknorris.io/jokes/random")

session = requests.Session()

for _ in tqdm(range(100)):
    response = session.get("https://api.chucknorris.io/jokes/random")