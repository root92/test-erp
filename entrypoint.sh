#!/bin/bash
set -e

show_help() {
  ehco """
  Commands
  ---------------------------------------
  start_dev     : start django dev server
  test          : run tests
  manage        : run django commands
  """
}

export PYTHONPATH="/code/:$PYTHONPATH"
export DJANGO_SETTINGS_MODULE=config.settings

case "$1" in
  "test" )
    # linting first
    flake8 ./apps
    # Run python tests and pass on any args e.g run individual tests
    ./manage.py test "${@:2}"
  ;;
  "start_dev" )
    ./manage.py migrate --noinput
    ./manage.py runserver 0.0.0.0:8000
  ;;
  "manage" )
    ./manage.py "${@:2}"
  ;;
  * )
    show_help
  ;;
esac
