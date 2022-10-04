import requests 
import pandas as pd

response = requests.get("http://universities.hipolabs.com/search?country=United+States")
df = pd.json_normalize(response.json())
df.to_csv('university.csv', encoding='utf-8', index=False)