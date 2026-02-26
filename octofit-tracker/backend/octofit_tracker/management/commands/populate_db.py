from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Eliminando datos existentes...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creando equipos...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creando usuarios...'))
        users = [
            User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel),
            User.objects.create(email='hulk@marvel.com', username='Hulk', team=marvel),
            User.objects.create(email='batman@dc.com', username='Batman', team=dc),
            User.objects.create(email='superman@dc.com', username='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', username='Wonder Woman', team=dc),
        ]

        self.stdout.write(self.style.SUCCESS('Creando actividades...'))
        Activity.objects.create(user=users[0], type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=users[1], type='swim', duration=45, date='2023-01-02')
        Activity.objects.create(user=users[3], type='cycle', duration=60, date='2023-01-03')

        self.stdout.write(self.style.SUCCESS('Creando workouts...'))
        w1 = Workout.objects.create(name='Pushups', description='Upper body')
        w2 = Workout.objects.create(name='Squats', description='Lower body')
        w1.suggested_for.set([users[0], users[3]])
        w2.suggested_for.set([users[1], users[4]])

        self.stdout.write(self.style.SUCCESS('Creando leaderboard...'))
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[3], score=90, rank=2)

        self.stdout.write(self.style.SUCCESS('Asegurando índice único en email de usuarios...'))
        with connection.cursor() as cursor:
            cursor.execute('CREATE INDEX IF NOT EXISTS user_email_unique_idx ON octofit_tracker_user (email)')

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada con datos de prueba!'))
