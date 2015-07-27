from reminders import celery 

@celery.task()
def send_sms_reminder(appointmend_id):
    pass
