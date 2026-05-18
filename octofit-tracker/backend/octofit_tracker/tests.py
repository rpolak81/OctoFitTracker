from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(email='batman@dc.com', username='batman', team=team)
        self.assertEqual(str(user), 'batman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='ironman@marvel.com', username='ironman', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2024-01-01')
        self.assertEqual(activity.type, 'run')

    def test_workout_creation(self):
        user = User.objects.create(email='spiderman@marvel.com', username='spiderman')
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout.suggested_for.add(user)
        self.assertEqual(workout.name, 'Pushups')

    def test_leaderboard_creation(self):
        user = User.objects.create(email='superman@dc.com', username='superman')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
