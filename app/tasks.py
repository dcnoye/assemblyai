import requests
import backoff
from app.models.api_models import Post
from app import db


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException)
def api_process(process_url, process_headers):
    response = requests.get(process_url, headers=process_headers)
    return response.status_code


def api_save(wh_id, wh_status, wh_ip):
    """return the information for later lookup"""
    new = Post(
        webhook_id=wh_id,
        ip_address=wh_ip,
        status=wh_status
    )
    db.session.add(new)
    db.session.commit()
    print("result of api_save", wh_id)


def api_update(job, connection, result, *args, **kwargs):
    """update database upon success"""
    print("testing api_update")
    post = Post.query.filter_by(Post.id == job).first()
    if post:
        post.status = 'success'
        db.session.commit()
    else:
        pass


def api_failure(job, connection, type, value, traceback):
    """update database upon failure"""
    print("entering api_failure")
    post = Post.query.filter_by(Post.id == job).first()
    if post:
        post.status = 'failed'
        db.session.commit()
    else:
        pass
