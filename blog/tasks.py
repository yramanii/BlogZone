from os import name
from celery.decorators import task
from celery.utils.log import get_task_logger

from .email import send_email

logger = get_task_logger(__name__)

@task(name="send_mail_task")
def send_mail_task(First_Name, Email, Description):
    logger.info("Mail Sent.")
    return send_email(First_Name, Email, Description)