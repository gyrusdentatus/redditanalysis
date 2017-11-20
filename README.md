This code is based on https://github.com/ianhussey/RedditCommentScraper 

# Reddit Comment Scraper

Scrape comments from a given thread on reddit.com using PRAW

## License
Copyright (c) gyrusdentatus 2017 (hans.bricks@protonmail.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License

## Version
1.0 (20/11/2017)

## Description
1. Scrapes all comments from a given reddit thread
2. Extracts top level comments
3. Saves to a csv file (??? writer)

## Known issues
None. 

## Notes
1. Although the script only uses publiclly available information, PRAW's call to the reddit API requires a reddit login (see line 44).
2. Reddit API limits number of calls (1 per second IIRC). For a large thread (e.g., 1000s of comments) script execution time may therefore be c.1 hour.
3. To configure, `cp Scraper_config.py.example Scraper_config.py` and edit that file. To extract more comment fields such as author and creation date, override the `comment_to_list` function in the config file.

