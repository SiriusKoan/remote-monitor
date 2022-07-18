from os import getenv
import unittest
from app import create_app

app = create_app(getenv("FLASK_ENV", "production"))


@app.shell_context_processor
def make_shell_context():
    return globals()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)
