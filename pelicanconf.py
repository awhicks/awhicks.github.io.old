#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import datetime

AUTHOR = 'Alex Hicks'
SITENAME = 'Alex Hicks'
SITEURL = 'https://awhicks.github.io'
SITETITLE = 'Alex Hicks'
SITESUBTITLE = 'PhD Student'
SITEDESCRIPTION = 'Alex Hicks'
COPYRIGHT_NAME = 'Alex Hicks'
COPYRIGHT_YEAR = datetime.date.today().year
PATH = 'content'
THEME = 'themes/flex/'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'
CUSTOM_CSS = 'static/custom.css'
DISABLE_URL_HASH = True

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
SOCIAL = (('GitHub', 'https://github.com/awhicks'),
          ('linkedin', 'https://www.linkedin.com/in/awh4kc'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

MAIN_MENU = False
DISPLAY_PAGES_ON_MENU = True
PAGES_SORT_ATTRIBUTE = 'order'


GITHUB_URL = 'https://github.com/awhicks'

# Flex theme
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
