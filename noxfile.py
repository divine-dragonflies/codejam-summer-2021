"""Development automation."""

import nox

nox.options.sessions = ["run"]


@nox.session(reuse_venv=True, python="3.9")
def lint(session):
    session.install("pre-commit")

    args = list(session.posargs)
    args.append("--all-files")
    session.run("pre-commit", "run", *args)


@nox.session(reuse_venv=True, python="3.9")
def run(session):
    session.install("-r", "requirements-dev.txt")
    session.run("python", "src")


@nox.session(reuse_venv=True, python="3.9")
def test(session):
    session.install("-r", "requirements-dev.txt")
    session.run("pytest", *session.posargs)
