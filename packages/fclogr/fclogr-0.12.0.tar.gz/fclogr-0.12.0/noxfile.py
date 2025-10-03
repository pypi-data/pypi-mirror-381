# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: GPL-2.0-or-later OR MIT

from __future__ import annotations

import glob
import os
from collections.abc import Sequence
from glob import iglob
from pathlib import Path
from shutil import copy2
from typing import cast

import nox
import nox.virtualenv

IN_CI = "JOB_ID" in os.environ or "CI" in os.environ
ALLOW_EDITABLE = os.environ.get("ALLOW_EDITABLE", str(not IN_CI)).lower() in (
    "1",
    "true",
)

PROJECT = "fclogr"
SPECFILE = "fclogr.spec"
LINT_SESSIONS = ("formatters", "codeqa", "typing")
LINT_FILES = (f"src/{PROJECT}", "tests/", "noxfile.py")

nox.options.sessions = (*LINT_SESSIONS, "test")


# Helpers


def install(session: nox.Session, *args, editable=False, **kwargs):
    # nox --no-venv
    if isinstance(session.virtualenv, nox.virtualenv.PassthroughEnv):
        session.warn(f"No venv. Skipping installation of {args}")
        return
    if editable and ALLOW_EDITABLE:
        args = ("-e", *args)
    session.install(*args, **kwargs)


def git(session: nox.Session, *args, **kwargs):
    return session.run("git", *args, **kwargs, external=True)


# General


@nox.session(python=["3.9", "3.10", "3.11", "3.12", "3.13"])
def test(session: nox.Session):
    packages = [".[test]"]
    env: dict[str, str] = {}
    tmp = Path(session.create_tmp())

    if any(i.startswith("--cov") for i in session.posargs):
        packages.extend(("coverage[toml]", "pytest-cov"))
        env["COVERAGE_FILE"] = str(tmp / ".coverage")

    install(session, *packages, editable=True)
    session.run("pytest", *session.posargs, env=env)


@nox.session
def coverage(session: nox.Session):
    install(session, "coverage[toml]")
    session.run("coverage", "combine", "--keep", *iglob(".nox/test*/tmp/.coverage"))
    session.run("coverage", "html")
    session.run("coverage", "report", "--fail-under=85")


@nox.session
def covtest(session: nox.Session):
    session.run("rm", "-f", *glob.iglob(".nox/*/tmp/.coverage*"), external=True)
    test_sessions = (f"test-{v}" for v in cast(Sequence[str], test.python))
    for target in test_sessions:
        session.notify(target, ["--cov"])
    session.notify("coverage")


@nox.session(venv_backend="none")
def lint(session: nox.Session):
    """
    Run formatters, codeqa, and typing sessions
    """
    for notify in LINT_SESSIONS:
        session.notify(notify)


@nox.session
def codeqa(session: nox.Session):
    install(session, ".[codeqa]")
    session.run("ruff", "check", *session.posargs, *LINT_FILES)
    session.run("reuse", "lint")


@nox.session
def formatters(session: nox.Session):
    install(session, ".[formatters]")
    posargs = session.posargs
    if IN_CI:
        posargs.append("--check")
    session.run("black", *posargs, *LINT_FILES)
    session.run("isort", *posargs, *LINT_FILES)


@nox.session
def typing(session: nox.Session):
    install(session, ".[typing]", editable=True)
    session.run("mypy", *LINT_FILES)


@nox.session
def bump(session: nox.Session):
    version = session.posargs[0]

    install(session, ".", "releaserr", "flit", "twine")

    session.run("releaserr", "check-tag", version)
    session.run("releaserr", "ensure-clean")
    session.run("releaserr", "set-version", "-s", "file", version)

    install(session, "-U", ".")

    # Bump specfile
    # fmt: off
    session.run(
        "fclogr", "bump",
        "--new", version,
        "--comment", f"Release {version}.",
        SPECFILE,
    )
    # fmt: on

    # Bump changelog, commit, and tag
    git(session, "add", SPECFILE, f"src/{PROJECT}/__init__.py")
    session.run("releaserr", "clog", version, "--tag")
    session.run("releaserr", "build", "--sign", "--backend", "flit_core")


@nox.session
def publish(session: nox.Session):
    # Setup
    install(session, "releaserr", "twine")
    session.run("releaserr", "ensure-clean")

    # Upload to PyPI
    session.run("releaserr", "upload")

    # Push to git, publish artifacts to sourcehut, and release to copr
    if not session.interactive or input(
        "Push to Sourcehut and copr build (Y/n)"
    ).lower() in ("", "y"):
        git(session, "push", "--follow-tags")
        session.run("hut", "git", "artifact", "upload", *iglob("dist/*"), external=True)
        copr_release(session)

    # Post-release bump
    session.run("releaserr", "post-version", "-s", "file")
    git(session, "add", f"src/{PROJECT}/__init__.py")
    git(session, "commit", "-S", "-m", "Post release version bump")


@nox.session
def copr_release(session: nox.Session):
    install(session, "copr-cli", "requests-gssapi", "specfile")
    tmp = Path(session.create_tmp())
    dest = tmp / SPECFILE
    copy2(SPECFILE, dest)
    session.run("python", "contrib/fedoraify.py", str(dest))
    session.run("copr-cli", "build", "--nowait", f"gotmax23/{PROJECT}", str(dest))


@nox.session
def srpm(session: nox.Session, posargs=None):
    install(session, ".", editable=True)
    posargs = posargs or session.posargs
    session.run("python3", "-m", "fclogr", "--debug", "dev-srpm", *posargs, SPECFILE)


@nox.session
def mockbuild(session: nox.Session):
    tmp = Path(session.create_tmp())
    srpm(session, ("-o", tmp, "--keep"))
    margs = [
        "mock",
        "--spec",
        str(Path(tmp, SPECFILE)),
        "--source",
        str(tmp),
        *session.posargs,
    ]
    if not session.interactive:
        margs.append("--verbose")
    session.run(*margs, external=True)
