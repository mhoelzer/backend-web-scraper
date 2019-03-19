#!/usr/bin/env python

__author__ = "mhoelzer"


import argparse
import requests
import re
import sys


def scraper(url):
    """"""
    response = requests.get(url)
    for url in response:
        pass


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("url", help="enter url to be scraped")
    return parser


def main(args):
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)
    namespace = parser.parse_args(args)
    url_to_be_scraped = namespace.url
    return scraper(url_to_be_scraped)


if __name__ == "__main__":
    # example of cmdl: python scraper.py https://nookpaleo.com
    print(main(sys.argv[1:]))
