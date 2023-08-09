import os

os.environ["DJANGO_SETTINGS_MODULE"] = "imdb.settings"

import django
django.setup()

from imdb_app.models import *

if __name__ == '__main__':
    # movies = (Movie.objects.filter(id='3'))
    # for movie in movies:
    #     print(f"\n Movie name: {movie.name}\n Movie description: {movie.description}\n Movie year: {movie.year}")

    # movie = Movie.objects.filter(id=1)[0]
    # movie.year = 2002
    # movie.save()


   # movie = Movie.objects.get(id=2)
   # movie.name = "The Lord of the Rings: The Return of the King"
   # movie.year = 2003
   # movie.description = "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring."
   # movie.save()

   # movie = Movie(name='The Godfather', description="Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.", year=1972)
   # movie.save()

   # Movie.objects.create(description="check", year=2000)

   # m = Movie.objects.get(description="check")
   # m.delete()

   # m = Movie.objects.get(name='Forrest Gump')
   # print(m.director)

   d = Director.objects.all()[0]
   print(d.movie_set.all())