from requests_html import HTMLSession
from reference import csv_target, root, markdown, pathway, regex_group
from functions import main

# Establish method
session = HTMLSession()

# Configure references from csv files
links = open(csv_target, "r")
paths = open(pathway, "r")

main(root, markdown, session, regex_group, links, paths)
