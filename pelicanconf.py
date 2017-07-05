#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'The Kuberati'
SITENAME = u'containerleaks'
SITEURL = 'https://containerleaks.com'
SITELOGO = SITEURL + '/images/containerfire.jpg'
SITETITLE = 'containerleaks'
SITESUBTITLE = 'the truth about containing all the things'
SITEDESCRIPTION = 'the unvarnished, anonymous truth about container technology'
SITEABOUTTITLE = 'experts, opinions, scary truths'
SITEABOUT = 'something soon'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017
MAIN_MENU = True
MENUITEMS = (
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
            )
DEFAULT_PAGINATION = 10

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'containerleaks.com'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = 'feeds/rss.xml'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'native'

# Blogroll
LINKS = (
         ('',''),
        )

# Social widget
SOCIAL = (
        ('twitter', ''),
        ('github', ''),
        ('github', ''),
        ('facebook', ''),
        ('linkedin', ''),
    )

PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['asciidoc_reader',
#             'sitemap',
#             'gravatar',
#             'filetime_from_git',
#             'gallery',
#             'thumbnailer',
#             'disqus_static',
#             'post_stats',
#            ]
PLUGINS = ['asciidoc_reader',
            'sitemap',
            'gravatar',
            'filetime_from_git',
            'gallery',
            'thumbnailer',
            'post_stats',
           ]
THEME = "pelican-theme"
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

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

GOOGLE_ANALYTICS = 'UA-9093834-2'

# blueidea settings
DISPLAY_CATEGORIES_ON_SUBMENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SEARCH_FORM = True

# thumbnailer settings
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'images'
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_KEEP_TREE = True

# disqus_static settings
DISQUS_SITENAME = ''
DISQUS_PUBLIC_KEY = ''
DISQUS_SECRET_KEY = ''

ASCIIDOC_BACKEND = 'html5'

GALLERY_PATH = 'images/gallery'
RESIZE = [
        ('images/gallery', False, 200,200),
      ]
