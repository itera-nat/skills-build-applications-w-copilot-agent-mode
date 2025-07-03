from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Activities
        Activity.objects.create(user=user1, activity_type='run', duration=30)
        Activity.objects.create(user=user2, activity_type='walk', duration=45)
        Activity.objects.create(user=user3, activity_type='cycle', duration=60)

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=80)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='all')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='all')
        Workout.objects.create(name='Running', description='Run for 20 minutes', suggested_for='runners')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
