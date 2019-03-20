#!/usr/bin/env python

__author__ = "mhoelzer"


import argparse
import requests
import re
import sys
from bs4 import BeautifulSoup


def scraper(url):
    """does the initial scraping; to be used with other functions"""
    response = requests.get(url)
    souped_url = BeautifulSoup(response.text, 'html.parser')
    return souped_url


def find_urls(souped_url):
    """finds all the urls because urls are better than talking on the phone"""
    unique_urls = set()
    url_regex = r"http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    url_a_tags = souped_url.find_all("a", href=True)  # filters out non-hrefs
    for url in url_a_tags:
        if re.search(url_regex, str(url)):
            unique_urls.add(url.get("href"))
    if not unique_urls:
        print("No urls found")
    print("\n".join(unique_urls))
    return unique_urls


def find_images(souped_url):
    """finds all the images because images are better than talking on the
    phone"""
    unique_images = set()
    images = souped_url.find_all("img", src=True)
    for image in images:
        unique_images.add(image.get("src"))
    if not unique_images:
        print("No images found")
    print("\n".join(unique_images))
    return unique_images


def find_emails(souped_url):
    """finds all the emails because emailing is better than talking on the
    phone"""
    unique_emails = set()
    email_regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
    email_tags = souped_url.find_all("a")
    for email in email_tags:
        if re.search(email_regex, str(email)):
            unique_emails.add(email.get("href").replace("mailto:", ""))
    if not unique_emails:
        print("No emails found")
    print("\n".join(unique_emails))
    return unique_emails


def find_phone_numbers(souped_url):
    """finds all the phone numbers because someone might be crazy enough to
    contact people via phone call"""
    unique_phone_numbers = set()
    phone_number_regex = re.compile(
        r"1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?")
    all_phone_numbers = phone_number_regex.findall(str(souped_url))
    for phone_number in all_phone_numbers:
        if phone_number not in unique_phone_numbers:
            unique_phone_numbers.add(
                "({}) {}-{}".format(phone_number[0], phone_number[1], phone_number[2]))
    if not unique_phone_numbers:
        print("No phone numbers found")
    print("\n".join(unique_phone_numbers))
    return unique_phone_numbers


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("url", help="enter url to be scraped")
    return parser


def main(args):
    """runs all the stuffz"""
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)
    namespace = parser.parse_args(args)
    url_to_be_scraped = namespace.url
    scraped_to_be_souped = scraper(url_to_be_scraped)
    if scraped_to_be_souped:
        print("URLs:")
        find_urls(scraped_to_be_souped)
        print("Images:")
        find_images(scraped_to_be_souped)
        print("Emails:")
        find_emails(scraped_to_be_souped)
        print("Phone Numbers:")
        find_phone_numbers(scraped_to_be_souped)


if __name__ == "__main__":
    # example of cmdln: python scraper.py https://nookpaleo.com
    main(sys.argv[1:])
