#!/usr/bin/env python3

import requests
import sys
import log
logger = log.get_logger(__name__)


def get_repository(user_name):

    '''
        The script lists all GitHub repository of given user

        Command line:
        python3 githubrepos.py username
    '''

    url = 'https://api.github.com/users/{}/repos'.format(user_name)
    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException as e:
        logger.debug(e)
        sys.exit()

    objects = resp.json()
    result = [_object['name'] for _object in objects]

    return result


def main():
    try:
        user_name = sys.argv[1]
        logger.debug(get_repository(user_name))
    except IndexError:
        logger.debug("Need user name")


if __name__ == "__main__":
    main()
