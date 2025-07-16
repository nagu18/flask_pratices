from flask import current_app

def say_hi():
    current_app.logger.info("Saying hi!")
    return "Hello from helper!"