import pymongo
from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_data


class Command(BaseCommand):
    help = "Populate the octofit_db database with test data."

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient("localhost", 27017)
        db = client["octofit_db"]
        # Clear collections first
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        # Insert test data
        db.users.insert_many(test_data["users"])
        db.teams.insert_many(test_data["teams"])
        db.activity.insert_many(test_data["activities"])
        db.leaderboard.insert_many(test_data["leaderboard"])
        db.workouts.insert_many(test_data["workouts"])
        self.stdout.write(self.style.SUCCESS("Test data populated successfully."))
