# Example test data for OctoFit Tracker (based on Monafit Tracker)
# This file can be imported in the Django management command to populate MongoDB

test_data = {
    "users": [
        {"email": "alice@mergington.edu", "name": "Alice Octopus", "password": "testpass1", "team": "Blue Sharks"},
        {"email": "bob@mergington.edu", "name": "Bob Cat", "password": "testpass2", "team": "Red Dolphins"},
        {"email": "carol@mergington.edu", "name": "Carol Whale", "password": "testpass3", "team": "Blue Sharks"}
    ],
    "teams": [
        {"name": "Blue Sharks", "members": ["alice@mergington.edu", "carol@mergington.edu"]},
        {"name": "Red Dolphins", "members": ["bob@mergington.edu"]}
    ],
    "activities": [
        {"user": "alice@mergington.edu", "type": "run", "distance_km": 2.5, "duration_min": 15, "date": "2025-07-01"},
        {"user": "bob@mergington.edu", "type": "walk", "distance_km": 1.0, "duration_min": 20, "date": "2025-07-01"},
        {"user": "carol@mergington.edu", "type": "strength", "reps": 30, "duration_min": 10, "date": "2025-07-01"}
    ],
    "leaderboard": [
        {"team": "Blue Sharks", "points": 120},
        {"team": "Red Dolphins", "points": 80}
    ],
    "workouts": [
        {"name": "Morning Run", "type": "run", "difficulty": "easy"},
        {"name": "Pushup Challenge", "type": "strength", "difficulty": "medium"}
    ]
}
