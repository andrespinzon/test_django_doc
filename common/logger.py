from config.external_db import ConnectionDb

from datetime import datetime


def create_logger(request, user):
    conn = ConnectionDb.connect()
    data = {
        "IP": request.META.get('REMOTE_ADDR'),
        "endpoint": f"{request.method} - {request.META.get('PATH_INFO')}",
        "user": user.username,
        "datetime": datetime.now()
    }
    conn.insert_one(data)
    print('Done')


def get_all_logger():
    conn = ConnectionDb.connect()
    loggers = conn.find()
    return [
        {
            'IP': logger['IP'],
            'endpoint': logger['endpoint'],
            'user': logger['user'],
            'datetime': logger['datetime']
        }
        for logger in loggers
    ]

