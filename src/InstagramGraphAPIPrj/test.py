from instagram_graph_api import InstagramGraphAPI

BUSINESS_ACCOUNT_ID='個人でセット'
USER_NAME='個人でセット'
ACCESS_TOKEN='個人でセット'

def get_user_json_test():
  instagram_graph_api=InstagramGraphAPI()
  print(instagram_graph_api.get_user_json(BUSINESS_ACCOUNT_ID,USER_NAME,ACCESS_TOKEN))

def get_media_json_test():
  instagram_graph_api=InstagramGraphAPI()
  data_fields='like_count,permalink'
  print(instagram_graph_api.get_media_json(BUSINESS_ACCOUNT_ID,USER_NAME,ACCESS_TOKEN,data_fields))

def main():
  try:
    get_media_json_test()
  except Exception as e:
    print(e)
    print(type(e))

if __name__ == "__main__":
  main()