# -*- coding: utf-8 -*-

"""
Does the following:

1. Inits git if used
2. Deletes dockerfiles if not going to be used
3. Deletes config utils if not needed
"""

import os
import shutil
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCKER_FILES = (".dockerignore", "docker-compose.yml")


def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)


def init_git():
    """
    Initialises git on the new project folder
    """
    git_commands = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit."],
    ]

    for command in git_commands:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


def remove_docker_files():
    """
    Removes files needed for docker if it isn't going to be used
    """
    for filename in [
        "Dockerfile",
    ]:
        os.remove(os.path.join(PROJECT_DIRECTORY, filename))


def remove_jira_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, ".jira"))


def remove_circleci_files():
    """
    Removes files needed for viper config utils
    """
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, ".circleci"))


# 1. Remove Dockerfiles if docker is not going to be used
if "{{ cookiecutter.use_docker }}".lower() != "y":
    remove_docker_files()

# Remove jira utils if not seleted
if "{{ cookiecutter.use_jira }}".lower() != "y":
    remove_jira_files()

# 5. Remove unused ci choice
if "{{ cookiecutter.use_ci}}".lower() == "travis":
    remove_circleci_files()
elif "{{ cookiecutter.use_ci}}".lower() == "circle":
    remove_file(".travis.yml")
else:
    remove_file(".travis.yml")
    remove_circleci_files()

# 7. Initialize Git (should be run after all file have been modified or deleted)
if "{{ cookiecutter.use_git }}".lower() == "y":
    init_git()
else:
    remove_file(".gitignore")
