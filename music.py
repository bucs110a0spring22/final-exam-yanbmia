import requests

class Music:
  def music():
    req = requests.get("https://musicbrainz.org/ws/2/genre")
    mus = req.json()
    print(mus)
  music()
  