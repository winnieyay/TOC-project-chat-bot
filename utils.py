import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAARWNqzVnn4BAGiVgb3PZBkGCmEy4v3FtXcRtGZB53Q9u4C2zC3KdhWe07PlkDW52aKYZA8uLMbjQz84G48lphggT72ftJooDvNIKJTNUeQo7i4OCZB1YqBYmYye0dLb0ltcZBpPRFZBldH44ZA3Jf3sIP9AHZCzrbQPnCcZCkJi07gZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
