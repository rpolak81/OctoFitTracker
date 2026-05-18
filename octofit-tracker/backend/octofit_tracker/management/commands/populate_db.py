from django.core.management.base import BaseCommand
import datetime
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Usuń istniejące kolekcje
        for col in ['teams', 'users', 'activities', 'workouts', 'leaderboard']:
            db[col].drop()

        # Drużyny
        db['teams'].insert_many([
            {'_id': 1, 'name': 'Marvel'},
            {'_id': 2, 'name': 'DC'},
        ])

        # Użytkownicy
        db['users'].insert_many([
            {'_id': 1, 'username': 'Iron Man',        'email': 'ironman@marvel.com',    'team_id': 1},
            {'_id': 2, 'username': 'Spider-Man',      'email': 'spiderman@marvel.com',  'team_id': 1},
            {'_id': 3, 'username': 'Captain America', 'email': 'captain@marvel.com',    'team_id': 1},
            {'_id': 4, 'username': 'Batman',          'email': 'batman@dc.com',         'team_id': 2},
            {'_id': 5, 'username': 'Superman',        'email': 'superman@dc.com',       'team_id': 2},
            {'_id': 6, 'username': 'Wonder Woman',    'email': 'wonderwoman@dc.com',    'team_id': 2},
        ])

        # Aktywności
        today = datetime.date.today()
        db['activities'].insert_many([
            {'_id': 1, 'user_id': 1, 'type': 'run',   'duration': 30, 'date': str(today)},
            {'_id': 2, 'user_id': 2, 'type': 'cycle', 'duration': 45, 'date': str(today)},
            {'_id': 3, 'user_id': 4, 'type': 'swim',  'duration': 60, 'date': str(today - datetime.timedelta(days=1))},
            {'_id': 4, 'user_id': 5, 'type': 'run',   'duration': 50, 'date': str(today - datetime.timedelta(days=1))},
            {'_id': 5, 'user_id': 6, 'type': 'cycle', 'duration': 40, 'date': str(today - datetime.timedelta(days=2))},
            {'_id': 6, 'user_id': 3, 'type': 'swim',  'duration': 35, 'date': str(today - datetime.timedelta(days=2))},
            {'_id': 7, 'user_id': 4, 'type': 'run',   'duration': 55, 'date': str(today - datetime.timedelta(days=3))},
            {'_id': 8, 'user_id': 2, 'type': 'run',   'duration': 25, 'date': str(today - datetime.timedelta(days=3))},
        ])

        # Treningi
        db['workouts'].insert_many([
            {'_id': 1, 'name': 'Pushups', 'description': 'Do 20 pushups'},
            {'_id': 2, 'name': 'Plank',   'description': 'Hold plank for 1 minute'},
            {'_id': 3, 'name': 'Sprint',  'description': 'Run 100m at full speed'},
            {'_id': 4, 'name': 'Squats',  'description': 'Do 30 squats'},
        ])

        # Leaderboard
        db['leaderboard'].insert_many([
            {'_id': 1, 'user_id': 1, 'score': 120},
            {'_id': 2, 'user_id': 2, 'score': 110},
            {'_id': 3, 'user_id': 4, 'score': 130},
            {'_id': 4, 'user_id': 5, 'score': 140},
            {'_id': 5, 'user_id': 6, 'score': 125},
            {'_id': 6, 'user_id': 3, 'score': 115},
        ])

        # Unikalny indeks na email
        db['users'].create_index('email', unique=True)

        client.close()
        self.stdout.write(self.style.SUCCESS('Baza octofit_db została wypełniona przykładowymi danymi!'))

