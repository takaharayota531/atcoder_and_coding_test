import json
import urllib.request

def Hello():
  return "Hello World"

def getUser(user_id):
  check_data={}
  check_data["user_id"]="TaroYamada"
  check_data["nickname"]="たろー"
  check_data["comment"]="僕は元気です"
  return {
    # "stastuscode": 
    "message": "User details by user_id",
    "user": {
    "user_id": "TaroYamada",
    "nickname": "たろー",
    "comment": "僕は元気です"
    }
    }


def post_user(user_data):
  return  {
    "message": "Account successfully created",
    "user": {
      "user_id": user_data["user_id"],
      "nickname": "TaroYamada"
    }
    }