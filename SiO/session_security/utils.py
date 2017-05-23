from datetime import datetime


def set_last_activity(session, dt):
    session['_session_security'] = dt.strftime('%Y-%m-%dT%H:%M:%S.%f')


def get_last_activity(session):
    try:
        return datetime.strptime(session['_session_security'],
                '%Y-%m-%dT%H:%M:%S.%f')
    except AttributeError:

        return datetime.now()
    except TypeError:
        return datetime.now()

