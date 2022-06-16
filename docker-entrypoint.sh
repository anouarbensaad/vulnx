#!/bin/sh

set -x
set -e

isArgPassed() {
  arg="$1"
  argWithEqualSign="$1="
  shift
  while [ $# -gt 0 ]; do
    passedArg="$1"
    shift
    case $passedArg in
    $arg)
      return 0
      ;;
    $argWithEqualSign*)
      return 0
      ;;
    esac
  done
  return 1
}

case "$1" in

  'cli')
    shift
    exec python vulnx.py $@
  ;;

  'webserver')
    shift
    exec python server.py $@
  ;;

  *)
  	exec python server.py $@
	;;
esac
