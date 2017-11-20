#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
"""
Description:
    1. Scrape all comments from a given reddit thread
    2. Extract top level comments
    3. Save to a csv file

Author:
    Copyright (c) Ian Hussey 2016 (ian.hussey@ugent.be) 
    Released under the GPLv3+ license.

Known issues:
    None. 

Notes:
    1. Although the script only uses publiclly available information, 
    PRAW's call to the reddit API requires a reddit login (see line 47).
    2. Reddit API limits number of calls (1 per second IIRC). 
    For a large thread (e.g., 1000s of comments) script execution time may therefore be c.1 hour.
    3. Because of this bottleneck, the entire data object is written to a pickle before anything is discarded. 
    This speeds up testing etc.
    4. Does not extract comment creation date (or other properties), which might be useful. 
"""

# Dependencies
import praw
import csv
import os
import sys
import pickle
import sys
from os.path import dirname
textFilePath = "/Users/Hans/reddit-analysis/RedditCommentScraper-master/"
textFileFolder = dirname( textFilePath ) # = "/home/me/somewhere/textfiles"

sys.path.append(textFileFolder)

import Scraper_config as cfg
import imp

# Set encoding to utf-8 rather than ascii, as is default for python 2.
# This avoids ascii errors on csv write.
#imp.reload(sys)
#sys.setdefaultencoding('utf-8') 

# Change directory to that of the current script
absolute_path = os.path.abspath(__file__)
directory_name = os.path.dirname(absolute_path)
os.chdir(directory_name)

# Acquire comments via reddit API
r = praw.Reddit(user_agent='Comment Extraction (by/u/USERNAME)',
                client_id='5Ofau0MfjYSsfw', client_secret="NFOZVdPeCNBgX6W7ThdrTUrGkpM", 
                username='gyrusdentatus', password='ou3-ynd-6tn-Kcb')


target_subreddit = 'NEO'

sub = r.subreddit(target_subreddit)
post_generator = sub.top(limit=50)

# override this in config to decide which attributes to save from a comment object
def default_comment_to_list(comment):
    return [comment.body]

if hasattr(cfg, "comment_to_list"):
    comment_to_list = cfg.comment_to_list
else:
    comment_to_list = default_comment_to_list

def target_subreddit(uniq_id):
    submission = r.get_subreddit_comments(submission_id=uniq_id)  # UNIQUE ID FOR THE THREAD GOES HERE - GET FROM THE URL
    submission.replace_more_comments(limit=20, threshold=0)  # all comments, not just first page

   

def get_subreddit_comments(uniq_id='NEO'):
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    comStream = praw.helpers.comment_stream(r, uniq_id[3:], limit=20) # Get the comment string
    comments = [[next(comStream).__str__()] for _ in range(limit)] # Get the raw string of each comment obj
    return list(comments) # Convert to list if running on Python3

    forest_comments = submission.comments  # get comments tree
    already_done = set()
    top_level_comments = [1]
    for comment in forest_comments:
        if not hasattr(comment, 'body'):  # only comments with body text
            continue
        if comment.is_root:  # only first level comments
            if comment.id not in already_done:
                already_done.add(comment.id)  # add it to the list of checked comments
                top_level_comments.append(comment_to_list(comment))  # append to list for saving
                # print(comment.body)
    return top_level_comments

comments = get_subreddit_comments()
print(comments)
# Save comments to disk

#with open(cfg.output_csv_file, "wb") as output:
#    writer = csv.writer(output)
#    writer.writerows(top_level_comments)

