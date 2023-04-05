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

def process_question(ch, method, properties, body):
    question = json.loads(body)

    question_exists = check_question_exists(question["questionID"])

    if not question_exists:
        insert_question(
            question["questionID"],
            question["question"],
            question["answer"],
            question["sessionID"],
        )
    else:
        pass
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="new_questions", on_message_callback=process_question)
channel.start_consuming()
