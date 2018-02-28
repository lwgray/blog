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
SITE_THUMBNAIL = '/images/reggae1.png'
GOOGLE_ANALYTICS = 'UA-106437223-1'
TIPUE_SEARCH = True
TEMPLATE_PAGES = {
    'search.html': 'search.html',
    }
GITHUB_URL = 'https://github.com/lwgray'
TWITTER_USERNAME = 'larrygray'
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
LINKS = (('Portfolio', 'https://lwgray.github.io'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/larrygray'),
          ('github', 'https://github.com/lwgray'),
          ('linkedin', "https://www.linkedin.com/in/larry-gray-phd/"),
          ('rss', '//igotthegoodstuff.com/feeds/all.atom.xml'),)


MENUITEMS = (('Portfolio', 'https://lwgray.github.io'),
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

COPYRIGHT_YEAR = 2018


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['pelican-plugins', './plugins']
PLUGINS = ['sitemap', 'post_stats', 'related_posts',
           'tipue_search', 'ipynb.markup', 'ipynb.liquid']

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
STATIC_PATHS = ['images', 'extra', 'data', 'scripts']
USE_LESS = True
#

'''
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
'''


MARKDOWN = {
    'extension_configs': {
        # https://pythonhosted.org/Markdown/extensions/index.html#officially-supported-extensions
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {'permalink': True},
        'mdx_video': {},
        'mdx_titlecase': {},
        # https://facelessuser.github.io/pymdown-extensions/
        'pymdownx.extra': {},
        'pymdownx.caret': {'superscript': True},
        'pymdownx.magiclink': {},
        'pymdownx.smartsymbols': {},
    },
    'output_format': 'html5',
    # Allow numbered lists to not start with 1. Used in following article:
    # https://kevin.deldycke.com/2016/12/falsehoods-programmers-believe-about-falsehoods-lists/
    # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
    'lazy_ol': False,
}


IGNORE_FILES = ['.ipynb_checkpoints']
DISPLAY_CATEGORIES_ON_MENU = False
