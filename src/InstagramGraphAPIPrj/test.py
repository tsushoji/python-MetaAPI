from instagram_graph_api import InstagramGraphAPI
from convert_result import convert_result_to_excel

BUSINESS_ACCOUNT_ID='個人でセット'
USER_NAME='個人でセット'
ACCESS_TOKEN='個人でセット'

def get_user_json_test():
  instagram_graph_api=InstagramGraphAPI()
  print(instagram_graph_api.get_user_json(BUSINESS_ACCOUNT_ID,USER_NAME,ACCESS_TOKEN))

def get_media_json_test():
  instagram_graph_api=InstagramGraphAPI()
  data_fields='timestamp,like_count,permalink'
  print(instagram_graph_api.get_media_json(BUSINESS_ACCOUNT_ID,USER_NAME,ACCESS_TOKEN,data_fields))

def main():
  try:
    # get_user_json_test()
    # get_media_json_test()
    instagram_graph_api=InstagramGraphAPI()
    # ex)data_fields='timestamp,like_count,permalink'
    data_fields='個人でセット'
    result=instagram_graph_api.get_media_json(BUSINESS_ACCOUNT_ID,USER_NAME,ACCESS_TOKEN,data_fields)
    output_path='個人でセット'
    convert_result_to_excel(result,output_path)
  except Exception as e:
    print(e)
    print(type(e))

if __name__ == "__main__":
  main()