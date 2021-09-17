from flask import (
    Blueprint,
    request,
    jsonify,
)
from app.models.api_models import Post
from rq import Queue
from redis import Redis
from app.tasks import api_process, api_save, api_update, api_failure


api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')


@api_blueprint.route('/hooks', methods=['GET'])
def api_hooks():
    """return the information for all"""
    posts = Post.query.all()
    xlist = []
    for x in posts:
        xlist.append(x.webhook_id+", "+x.ip_address+", "+x.status)
    return jsonify(xlist), 200


@api_blueprint.route('/hooks/<hook_id>', methods=['GET'])
def api_hook(hook_id):
    """return the information for hook_id"""
    post = Post.query.filter_by(webhook_id=hook_id).first()
    return jsonify(post.status), 200


@api_blueprint.route('/hooks', methods=['POST'])
def process_webhook():
    """process the webhook, assign webhook_id"""
    try:
        post_data = request.get_json()
        url = post_data.get('url')
        headers = post_data.get('headers')
    except Exception as e:
        return jsonify(str(e)), 500

    q = Queue('high', connection=Redis(host='redis', port=6379, decode_responses=True))
    task = q.enqueue(
        api_process,
        args=(url, headers),
        on_success=api_update,
        on_failure=api_failure)

    response_object = {
        "status": "success",
        "data": {
            "id": task.get_id(),
            "status": task.get_status()
        }
    }
    api_save(task.get_id(), task.get_status(), request.remote_addr)

    return jsonify(response_object), 200
