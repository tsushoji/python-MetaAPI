from time import sleep
import requests

# ex)BASE_URL='https://graph.facebook.com/v15.0'
BASE_URL='https://graph.facebook.com/個人でセット'

class InstagramGraphAPI:

  def __init__(self):
    self.base_url=BASE_URL

  def get_user_json(self,business_account_id,user_name,access_token):
    url=f"{self.base_url}/{business_account_id}"
    fields=f"business_discovery.username({user_name})"
    params={"fields":fields,"access_token":access_token}

    return requests.get(url,params=params).json()["business_discovery"]

  def get_media_json(self,business_account_id,user_name,access_token,data_fields):
    url=f"{self.base_url}/{business_account_id}"
    fields='business_discovery.username('+user_name+'){media{'+data_fields+'}}'
    params={"fields":fields,"access_token":access_token}

    response=requests.get(url,params=params).json()["business_discovery"]

    media=[]
    for media_data in response["media"]["data"]:
      media.append(media_data)

    # 上限25件までしか取得できないため、25件以降取得
    if 'after' in response["media"]["paging"]["cursors"]:
      after=response["media"]["paging"]["cursors"]["after"]

      while after is not None:
        fields='business_discovery.username('+user_name+'){media.after('+after+'){'+data_fields+'}}'
        params={"fields":fields,"access_token":access_token}

        response=requests.get(url,params=params).json()["business_discovery"]

        for media_data in response["media"]["data"]:
          media.append(media_data)

        if 'after' in response["media"]["paging"]["cursors"]:
          after=response["media"]["paging"]["cursors"]["after"]
        else:
          after=None

        sleep(3)

    return media
    