from apiclient.discovery import build

API_KEY = "AIzaSyC669rOKsQJTGxlr7F-blT4SS866RXRu4E"

youtube = build('youtube', 'v3', developerKey=API_KEY)

response = youtube.search().list(
    part="snippet"
    
)
