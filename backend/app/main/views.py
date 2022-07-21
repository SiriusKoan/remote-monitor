import json
from flask import jsonify
from . import main_bp
from ..monitor import funcs, start_monitor
from ..monitor.hosts import hosts
from ..redis import get_record


@main_bp.before_app_first_request
def start_monitoring():
    start_monitor()


@main_bp.route("/api/hosts", methods=["GET"])
def get_hosts_api():
    res = [
        {
            "name": host["name"],
            "addr": host["addr"],
            "bool_functions": [
                func.__name__ for func in host["bool_functions"]
            ],
            "text_functions": [
                func.__name__ for func in host["text_functions"]
            ],
        }
        for host in hosts
    ]
    return jsonify(res)


@main_bp.route("/api/<string:host>/<string:func>", methods=["GET"])
def get_results_api(host, func):
    return get_record(host, func)
