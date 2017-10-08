#!/bin/bash
set -e

show_help() {
  ehco """
  Commands
  ---------------------------------------
  start_dev     : start django dev server
  manage        : run django commands
  """
}

export PYTHONPATH="/code/:$PYTHONPATH"
export DJANGO_SETTINGS_MODULE=config.settings

case "$1" in
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
