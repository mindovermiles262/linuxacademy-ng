#!/bin/bash
# Uses curl and cookies to get the entered page
# Uses the PHPSESSIONID cookie obtained after LA login
#
# Example:
# $ ./script.sh https://linuxacademy.com/course/3/xxx 2252123287682365235876235
#

if [ $# -ne 2 ]; then
    printf "Usage: ./curl-command.sh <COURSE_URL> <COOKIE>\n"
fi

/usr/bin/curl -Lb "PHPSESSIONID=$2" "$1" > la-course.html
  # -L => Follow Redirects
  # -b => Cookie "NAME=VALUE" format

