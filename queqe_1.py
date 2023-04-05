import pika
import json


def insert_question(question_id, question_text, answer_text, session_id):
    print(
        f"Inserting question {question_id}: {question_text} ({answer_text}) for session {session_id}"
    )


def check_question_exists(question_id):
    return False


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="new_questions")

