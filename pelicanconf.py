#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nathan Levesque'
SITENAME = u"Rhysyngsun's Blog"
SITEURL = ''

LANDING_PAGE_ABOUT = {
    'title': 'About me',
    'details': '<p>My name is Nathan Levesque. I\'m a software developer who spends his time building software that scales.</p><p>I work at <a href="https://vsnap.com">Vsnap</a> as Lead Developer with Node.js + Postgres and figure out how to make it all work on AWS.</p>'
}

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

THEME = "/Users/nathan/dev/oss/pelican-elegant"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
USE_FOLDER_AS_CATEGORY = False
FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
STATIC_PATHS = ['images', 'CNAME', 'theme/images']

# Blogroll
LINKS = (('https://github.com/rhysyngsun', 'Github'),)

# Social widget
SOCIAL = (('https://twitter.com/rhysyngsun', 'Twitter'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['/Users/nathan/dev/oss/pelican-plugins']
PLUGINS = ["pelican-langcategory", 'sitemap', 'extract_toc', 'tipue_search']

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

LANGUAGES= (('en','english','en'),)

LANGUAGE_URL = '{lang}'
LANGUAGE_SAVE_AS = '{lang}/index.html'

PAGE_URL = "{lang}/{slug}.html"
PAGE_SAVE_AS = "{lang}/{slug}.html"
PAGE_LANG_URL = "{lang}/{slug}.html"
PAGE_LANG_SAVE_AS = "{lang}/{slug}.html"
