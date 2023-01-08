# python-MetaAPI  
## Release Ver1.0.1  
### InstagramGraphAPIPrj  
### 概要  
InstagramGraphAPIを活用したデータ分析。  
### 事前準備  
1-Facebookアカウント作成  
2-Facebookページ作成  
3-Instagramアカウント作成  
4-InstagramGraphAPIアクセストークン取得  
5-InstagramビジネスアカウントID取得  
### 使用方法  
*コメント「個人でセット」箇所は各個人でセットください。  
### 使用技術  
*pythonバージョン  
3.9.6  
*pythonライブラリー  
requests 2.28.1  
openpyxl 3.0.10  
### リリース事項  
* 以下、「表1-0-1-1」インターフェースを追加。  
<table>
  <tr>
    <th width="50">No</th>
    <th width="150">モジュール名</th>
    <th width="100">クラス名</th>
    <th width="100">メソッド名</th>
    <th width="250">引数</th>
    <th width="350">戻り値</th>
    <th width="350">説明</th>
  </tr>
  <tr>
    <td>1</td>
    <td>instagram_graph_api.py</td>
    <td>InstagramGraphAPI</td>
    <td>get_user_json</td>
    <td>business_account_id <br> InstagramビジネスアカウントID, <br> user_name <br> Instagramユーザ名, <br> access_token <br> InstagramGraphAPIアクセストークン</td>
    <td>Instagramユーザ情報(辞書リスト形式)</td>
    <td>Instagramユーザ情報取得</td>
  </tr>
  <tr>
    <td>2</td>
    <td>instagram_graph_api</td>
    <td>InstagramGraphAPI</td>
    <td>get_media_json</td>
    <td>business_account_id <br> InstagramビジネスアカウントID, <br> user_name <br> Instagramユーザ名, <br> access_token <br> InstagramGraphAPIアクセストークン, <br> data_fields <br> 取得メディアデータキー名</td>
    <td>Instagramメディア情報(辞書リスト形式)</td>
    <td>Instagramメディア情報取得</td>
  </tr>
  <tr>
    <td>3</td>
    <td>convert_result.py</td>
    <td>なし</td>
    <td>convert_result_to_excel</td>
    <td>result <br> 変換データ(辞書リスト形式), <br> excel_file_path <br> 変換excelパス</td>
    <td>なし</td>
    <td>変換データ(辞書リスト形式)をexcelへ変換</td>
  </tr>
</table>
