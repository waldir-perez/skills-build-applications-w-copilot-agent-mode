from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(email='batman@dc.com', username='batman', team=team)
        self.assertEqual(str(user), 'batman@dc.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='spiderman@marvel.com', username='spiderman', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2023-01-01')
        self.assertEqual(str(activity), 'spiderman@marvel.com - run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='ironman@marvel.com', username='ironman', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(str(leaderboard), 'ironman@marvel.com - 100')
