from . import main_bp


@main_bp.route("/api/hosts", methods=["GET"])
def get_hosts_api():
    pass


@main_bp.route("/api/<string:name>/<string:func>", methods=["GET"])
def get_results_api(name, func):
    pass
