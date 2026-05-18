from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Usuń istniejące dane
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Tworzenie drużyn
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Tworzenie użytkowników
        ironman = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel)
        spiderman = User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel)
        captain = User.objects.create(email='captain@marvel.com', username='Captain America', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)
        wonderwoman = User.objects.create(email='wonderwoman@dc.com', username='Wonder Woman', team=dc)

        # Tworzenie aktywności
        Activity.objects.create(user=ironman, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=spiderman, type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=batman, type='swim', duration=60, date=timezone.now().date())
        Activity.objects.create(user=superman, type='run', duration=50, date=timezone.now().date())
        Activity.objects.create(user=wonderwoman, type='cycle', duration=40, date=timezone.now().date())

        # Tworzenie treningów
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout2 = Workout.objects.create(name='Plank', description='Hold plank for 1 minute')
        workout1.suggested_for.add(ironman, batman)
        workout2.suggested_for.add(spiderman, superman)

        # Tworzenie leaderboard
        Leaderboard.objects.create(user=ironman, score=120)
        Leaderboard.objects.create(user=spiderman, score=110)
        Leaderboard.objects.create(user=batman, score=130)
        Leaderboard.objects.create(user=superman, score=140)
        Leaderboard.objects.create(user=wonderwoman, score=125)

        self.stdout.write(self.style.SUCCESS('Baza octofit_db została wypełniona przykładowymi danymi!'))
