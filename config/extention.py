from sqlalchemy import create_engine

from django.conf import settings

engine = create_engine(settings.DATABASE_URL)
