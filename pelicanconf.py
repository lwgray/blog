#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Larry Gray'
SITENAME = u'Larry Gray'
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = "Computational Biologist - Data Addict - Pythonista"
SITEDESCRIPTION = '%s\'s Portal for dispensing and gaining wisdom' % AUTHOR
SITELOGO = '/images/reggae1.png'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'


# Plugmage Theme
THEME = 'themes/plumage'
SITE_THUMBNAIL = 'images/reggae1.png'
GOOGLE_ANALYTICS = 'UA-106437223-1'
TIPUE_SEARCH = True
TEMPLATE_PAGES = {
    'search.html': 'search.html',
    }
# END

ROBOTS = 'index, follow'

# JINJA_ENVIRONMENT = {}
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True


# Blogroll
LINKS = (('Portfolio', 'http://lwgray.github.io'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/larrygray'),
          ('github', 'https://github.com/lwgray'),
          ('linkedin', "https://www.linkedin.com/in/lawrence-gray-ph-d-11b6498/"),
          ('rss', '//igotthegoodstuff.com/feeds/all.atom.xml'),)


MENUITEMS = (('Portfolio', 'http://lwgray.github.io'),
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

COPYRIGHT_YEAR = 2017


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


MARKUP = ('md')
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'related_posts', 'tipue_search']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = "igotthegoodsuff"
STATIC_PATHS = ['images', 'extra']
USE_LESS = True
#
