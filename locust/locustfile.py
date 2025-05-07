from locust import HttpUser, task, between

class Story2AudioUser(HttpUser):
    wait_time = between(1, 3)  # Simulates user wait time between requests

    @task
    def generate_audio(self):
        self.client.post("/generate", json={"story_text": "Once upon a time, in a land far away..."})
