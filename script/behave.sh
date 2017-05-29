#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# shellcheck source=/dev/null
[ -r "script/bootstrap.sh" ] && source "script/bootstrap.sh"

cd "${SOURCE_DIR}" || echo 'Not Found'

if [[ "$1" == "all" ]]; then
    python manage.py behave --settings="${DJANGO_SETTINGS_TEST}" --no-capture-stderr --no-capture --use-existing-database --no-skipped --stop
else
    python manage.py behave --settings="${DJANGO_SETTINGS_TEST}" --no-capture-stderr --no-capture --use-existing-database --no-skipped --stop --tags "$1"
fi
