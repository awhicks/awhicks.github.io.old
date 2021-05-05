#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Alex Hicks'
SITENAME = 'Alex Hicks'
SITEURL = 'https://awhicks.github.io'
SITETITLE = 'Alex Hicks'
SITESUBTITLE = 'PhD Student'
SITEDESCRIPTION = 'Alex Hicks'
PATH = 'content'
THEME = '/home/awh4kc/misc/pelican-themes/flex'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/awhicks'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
MAIN_MENU = True
HOME_HIDE_TAGS = True
