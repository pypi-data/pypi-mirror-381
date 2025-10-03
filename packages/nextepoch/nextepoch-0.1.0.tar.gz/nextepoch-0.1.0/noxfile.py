import nox

@nox.session
def tests(session):
    session.run("uv", "run", "--active", "pytest", "-q", external=True)

@nox.session
def lint(session):
    session.run("uv", "run", "--active", "ruff", "check", "src", "tests", external=True)
    session.run("uv", "run", "--active", "black", "--check", "src", "tests", external=True)

@nox.session
def format(session):
    session.run("uv", "run", "--active", "ruff", "check", "src", "tests", "--fix", external=True)
    session.run("uv", "run", "--active", "black", "src", "tests", external=True)
