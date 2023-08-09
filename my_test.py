import os

os.environ["DJANGO_SETTINGS_MODULE"] = "imdb.settings"

import django
django.setup()

from imdb_app.models import Movie
import datetime

if __name__ == '__main__':
    start = datetime.datetime.now()

    num = 0
    while True:
        print(num)
        num += 1
        if num == 276770 + 1:
            break

    end = datetime.datetime.now()
    date = end.strftime("%d.%m.%Y")
    time = end.strftime("%H:%M")
    run_time = (end - start).total_seconds()
    print("\nProgram Run Time:", run_time, "Seconds\n")