from django.shortcuts import render

# Create your views here.
posts = [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "comments": ["quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"],
    "likes": 28,
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "comments": ["est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"],
    "likes": 12,
  },
]

def index(request):
    results = {
        'posts': posts
    }
    return render(request, 'index.html', results)
