from sqlalchemy import Column, Integer, String, \
    LargeBinary, DateTime, Text, text

from app.db.base_class import Base


class CeleryTaskmeta(Base):
    __tablename__ = 'celery_taskmeta'

    id = Column(Integer, primary_key=True, server_default=text("nextval('celery_taskmeta_id_seq'::regclass)"))
    task_id = Column(String(155), unique=True)
    status = Column(String(50))
    result = Column(LargeBinary)
    date_done = Column(DateTime)
    traceback = Column(Text)
    name = Column(String(155))
    args = Column(LargeBinary)
    kwargs = Column(LargeBinary)
    worker = Column(String(155))
    retries = Column(Integer)
    queue = Column(String(155))


class CeleryTasksetmeta(Base):
    __tablename__ = 'celery_tasksetmeta'

    id = Column(Integer, primary_key=True, server_default=text("nextval('celery_tasksetmeta_id_seq'::regclass)"))
    taskset_id = Column(String(155), unique=True)
    result = Column(LargeBinary)
    date_done = Column(DateTime)
