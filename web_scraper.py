#!/usr/bin/env python

__author__ = "mhoelzer"


import argparse
import requests
import re
import sys
from bs4 import BeautifulSoup


def scraper(url):
    """"""
    response = requests.get(url)
    souped_url = BeautifulSoup(response.text, 'html.parser')
    return souped_url


def find_urls(souped_url):
    pass


def find_emails(souped_url):
    pass


def find_phone_numbers(souped_url):
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
    scraped_to_be_souped = scraper(url_to_be_scraped)
    if scraped_to_be_souped:
        find_urls(scraped_to_be_souped)
        find_emails(scraped_to_be_souped)
        find_phone_numbers(scraped_to_be_souped)


if __name__ == "__main__":
    # example of cmdl: python scraper.py https://nookpaleo.com
    # print(main(sys.argv[1:]))
    main()
