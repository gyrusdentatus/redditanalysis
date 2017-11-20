#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
"""
Description:
    config for the Scraper.py
"""
# change these to your login details
username = "gyrusdentatus"
password = "ou3-ynd-6tn-Kcb"

output_file = "scraped_data.pkl"
output_csv_file = "output.csv"

# UNIQUE ID FOR THE THREAD GOES HERE - GET FROM THE URL
# Set unique id or subreddit
uniq_id = "NEO" 

## override this in config to decide which attributes to save from a comment object
def comment_to_list(comment):
    return [comment.author, comment.body]

