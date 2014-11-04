#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nathan Levesque'
SITENAME = u"Rhysyngsun's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

THEME = "/Users/nathan/dev/oss/dev-random3"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
USE_FOLDER_AS_CATEGORY = False
FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
STATIC_PATHS = ['images', 'CNAME']

# Blogroll
LINKS = (('https://github.com/rhysyngsun', 'Github'),)

# Social widget
SOCIAL = (('https://twitter.com/rhysyngsun', 'Twitter'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['/Users/nathan/dev/oss/pelican-plugins']
PLUGINS = ["pelican-langcategory"]

LANGUAGES= (('en','english','en'),)

LANGUAGE_URL = '{lang}/'
LANGUAGE_SAVE_AS = '{lang}/index.html'

PAGE_URL = "{lang}/{slug}.html"
PAGE_SAVE_AS = "{lang}/{slug}.html"
PAGE_LANG_URL = "{lang}/{slug}.html"
PAGE_LANG_SAVE_AS = "{lang}/{slug}.html"
