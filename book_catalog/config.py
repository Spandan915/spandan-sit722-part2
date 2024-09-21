import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://spandan_sit722_part2_lycy_user:j7xxxWhCjseSBa0WicI0teXqzFadNOfd@dpg-crmo5h08fa8c73am6fcg-a.oregon-postgres.render.com/spandan_sit722_part2_lycy")

settings = Settings()
