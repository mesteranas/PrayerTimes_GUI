import json
import os
import settings
jpath=os.path.join(os.getenv('appdata'),settings.app.appName,"regions.json")
if not os.path.exists(jpath):
    with open(jpath,"w",encoding="utf-8") as file:
        file.write("{}")
def get():
    with open(jpath,"r",encoding="utf-8") as data:
        return json.load(data)
def save(data):
    with open(jpath,"w",encoding="utf-8") as file:
        file.write(str(data).replace("'",'"'))