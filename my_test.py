import datetime
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "imdb.settings"

import django
django.setup()

from imdb_app.models import *

if __name__ == '__main__':

    # m = Movie.objects.create(name='Oppenheimer', description='The story of American scientist, J. Robert Oppenheimer, and his role in the development of the atomic bomb.', year=2023, director=Director.objects.create(name='Christopher Nolan', birth_date=datetime.date(1970,8,30))).save()
    # m = Movie.objects.create(name='Dracula 2000', description='A group of thieves breaks into a chamber expecting to find paintings, but instead they release the count himself, who travels to New Orleans to find his nemesis daughter, Mary Van Helsing.', year=2000, director=Director.objects.create(name='Patrick Lussier', birth_date=datetime.date(1964,8,30))).save()
    # m = Movie.objects.create(name='Barbie',
    #                          description='Barbie suffers a crisis that leads her to question her world and her existence.',
    #                          year=2023,
    #                          director=Director.objects.create(name='Greta Gerwig', birth_date=datetime.date(1983,9,4))).save()


    display = Movie.objects.filter(year=2000)
    for movie in display:
        print(movie)