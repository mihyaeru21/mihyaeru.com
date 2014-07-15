#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

########################################
# basic
########################################

SITENAME = u'みひゃえるどっとこむ'
SITEURL  = u'http://mihyaeru.com'
AUTHOR   = u'Mihyaeru'

TIMEZONE     = u'Asia/Tokyo'
DEFAULT_LANG = u'ja'

PATH = u'content'


########################################
# pages, articles
########################################

PAGE_PATHS    = [u'pages']
ARTICLE_PATHS = [u'articles']
BLOG_PREFIX   = u'blog/'

# ブログ記事系
ARTICLE_URL       = BLOG_PREFIX + u'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS   = BLOG_PREFIX + u'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
TAG_URL           = BLOG_PREFIX + u'tags/{slug}/'
TAG_SAVE_AS       = BLOG_PREFIX + u'tags/{slug}/index.html'
CATEGORY_URL      = u''
CATEGORY_SAVE_AS  = u''
AUTHOR_URL        = u''
AUTHOR_SAVE_AS    = u''

# 記事の集合的なやつ
DIRECT_TEMPLATES      = (u'index', u'tags', u'archives')
INDEX_SAVE_AS         = BLOG_PREFIX + u'index.html'
TAGS_SAVE_AS          = BLOG_PREFIX + u'tags/'
TAGS_SAVE_AS          = BLOG_PREFIX + u'tags/index.html'
ARCHIVES_SAVE_AS      = BLOG_PREFIX + u'archives/'
ARCHIVES_SAVE_AS      = BLOG_PREFIX + u'archives/index.html'
YEAR_ARCHIVE_SAVE_AS  = BLOG_PREFIX + u'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = BLOG_PREFIX + u'posts/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS   = BLOG_PREFIX + u'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'

# ページ系
PAGE_URL     = u'{slug}/'
PAGE_SAVE_AS = u'{slug}/index.html'

# pelicanではなくjinja2だけを噛ませたいもの
TEMPLATE_PAGES = {
    u'templates/index.html': u'index.html'
}


########################################
# feeds
########################################

# http://mihyaeru.com/blog
FEED_DOMAIN    = SITEURL + u'/' + BLOG_PREFIX[:-1]
FEED_MAX_ITEMS = 100

FEED_ATOM             = None
FEED_RSS              = None
FEED_ALL_ATOM         = u'blog/feeds/atom.xml'
FEED_ALL_RSS          = u'blog/feeds/rss.xml'
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None
TAG_FEED_ATOM         = None
TAG_FEED_RSS          = None


########################################
# other そのうち整理する
########################################

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME            = u'theme'
THEME_STATIC_DIR = u''

PLUGIN_PATHS = [u'plugins']
PLUGINS = [u'assets']

ASSET_SOURCE_PATHS = (
    u'scss',
)
