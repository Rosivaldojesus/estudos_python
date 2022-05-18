import requests

q = "Python"
chave = "AIzaSyBYVRDyWuWiYJL3XBGuvjoLzHT2QnH2A1M"
maxResults = 10

youtube = requests.get("https://youtube.googleapis.com/youtube/v3/search?q={}&key={}&{}=25".format(q, chave, maxResults))

print(youtube)
print(youtube.json())