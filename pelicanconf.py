#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nathan Levesque'
SITENAME = u"Rhysyngsun's Blog"
SITEURL = 'http://localhost:3000/'
SITETITLE = AUTHOR
SITESUBTITLE = 'Senior Software Engineer'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = '//0.gravatar.com/avatar/73bf4b553a05187d21074a7e7539f1ac'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#999999'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

COPYRIGHT_YEAR = '2012-2017'

SUMMARY_MAX_LENGTH = 150

PATH = 'content'

TIMEZONE = 'US/Eastern'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

THEME = "/home/nathan/oss/pelican-themes/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
STATIC_PATHS = ['images', 'CNAME', 'theme/images', 'extra', 'extra/.well-known']

# Blogroll
LINKS = []

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/nathanlevesque'),
    ('twitter', 'https://twitter.com/rhysyngsun'),
    ('gitlab', 'https://gitlab.com/rhysyngsun'),
    ('github', 'https://github.com/rhysyngsun'),
    ('stack-overflow', 'https://stackoverflow.com/users/140999/rhysyngsun'),
)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['/home/nathan/oss/pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'related_posts']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives'))
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
