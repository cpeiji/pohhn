import requests

class RequestUtil:

    @staticmethod
    def create_json_requ(url,payload,header):
        try:
            json = requests.get(url+"?"+payload,headers=header)
            return json.json()
        except Exception as e:
            return ""

    @staticmethod
    def create_html_requ(url, payload, header,encode):
        try:
            html = requests.get(url,params=payload, headers=header)
            html.encoding = encode
            return html.text
        except Exception as e:
            return ""