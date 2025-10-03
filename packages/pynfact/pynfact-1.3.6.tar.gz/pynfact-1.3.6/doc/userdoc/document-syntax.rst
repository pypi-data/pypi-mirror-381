.. vim: set ft=rst fenc=utf-8 tw=72 nowrap:

.. _document-syntax:

***************
Document syntax
***************

Meta tags
=========

Both articles and pages use the same syntax and structure, although the
pages will ignore some tags that are useless outside the chronological
post definition.

Since the title is used to create the post/page slug, it's a mandatory
requirement, and in posts but not in pages, the date is also mandatory,
for the tree structure of the website depends on the date.

A simple example of meta information could be, for a **Markdown**
document::

    Title: Interesting title in English
    Summary: Here I can type diacritics such as naïve
    Date: Wed 11 Mar 2020 11:11:11 AM UTC

and, for a **reStructuredText**, two options:

#. Adding the title as another metainformation tag::

    :Title: Interesting title in English
    :Summary: Here I can type diacritics such as naïve
    :Date: Wed 11 Mar 2020 11:11:11 AM UTC

#. Or, making the title in reStructuredText before the other meta tags::

    Interesting title in English
    ============================

    :Summary: Here I can type diacritics such as naïve
    :Date: Wed 11 Mar 2020 11:11:11 AM UTC

All tags are case insensitive.

List of meta tags
-----------------

Tags are case insensitive.

+--------------+----------------------------------------+----------+----------+
| Meta tag     | Description                            |   Post   | Page     |
+==============+========================================+==========+==========+
| ``title``    | Title of the post                      | Yes [1]_ | Yes [1]_ |
+--------------+----------------------------------------+----------+----------+
| ``summary``  | A brief summary for this post          | Yes      | No       |
+--------------+----------------------------------------+----------+----------+
| ``category`` | Category for this post (only 1)        | Yes      | No       |
+--------------+----------------------------------------+----------+----------+
| ``tags``     | Tag list, comma separated              | Yes      | No       |
+--------------+----------------------------------------+----------+----------+
| ``author/s`` | Author or authors                      | Yes      | No       |
+--------------+----------------------------------------+----------+----------+
| ``date``     | Date of publication                    | Yes [1]_ | No       |
+--------------+----------------------------------------+----------+----------+
| ``updated``  | Post last modification date            | Yes      | No       |
+--------------+----------------------------------------+----------+----------+
| ``comments`` | If comment engine is setup, allow them | Yes      | No       |
+--------------+----------------------------------------+----------+----------+
| ``private``  | Build the post but do not reference it | Yes      | Yes      |
+--------------+----------------------------------------+----------+----------+
| ``nav``      | Indicates if a page is on the nav. bar | No       | Yes      |
+--------------+----------------------------------------+----------+----------+

.. [1] Mandatory fields

Aliases
~~~~~~~

+--------------+-------------------------+
|    Tags      |    Aliases              |
+==============+=========================+
| ``category`` | ``cat``                 |
+--------------+-------------------------+
| ``date``     | ``created``, ``odate``  |
+--------------+-------------------------+
| ``nav``      | ``navigation``          |
+--------------+-------------------------+
| ``private``  | ``priv``                |
+--------------+-------------------------+
| ``summary``  | ``subtitle``            |
+--------------+-------------------------+
| ``updated``  | ``modified``, ``mdate`` |
+--------------+-------------------------+

Not all the tags work on individual pages, as they do not require the
chronological order, nor they have any comments, or tags, or they do not
belong to any category.  For an article or post, ``title`` and ``date``
are mandatory tags.  For a page, only the ``title`` is required.

The ``author`` represents the original author for a post.  If not used,
it will default to the website author.

If you choose an external service for comments, such as Disqus or
TalkYard, you may enter the required script code in the
``entry.html.j2`` template.  This code goes at the end of the page.  The
``comments`` tag allow to load that code for a particular entry or to
ignore it.

The entry ``tags`` is a list of keywords separated by comma.  A page for
tags will be created referencing all posts by their tags, and also a
tagcloud page.

The ``category`` tag is another way of sorting the content, besides
using tags.  Tags a good for doing a keyword search, but not for
categorizing all entries under one only subject.  There could be many
posts in the category of "Computers", each one of the with a different
set of tags.  A post can belong only to one category.

Posts and pages can be ``private``.  This means that the content will be
generated, and it can be accessed if the URI is known, but will not be
referenced by any link or index of the website.

By default, a page will be linked to the navigation bar, after the blog
main features and before the feed link.  If you want a page not to be
linked in such a way, set ``nav`` (or ``navigate``) to "no".  The name
of the blog author is automatically a link to a page with filename
``about.md``.  Because of that, it'll be a good idea to set the
navigation of this page to "no".  There are many reasons for not wanting
a page to appear at the navigation bar, for example, in case of
referencing it from a blog post, and only from that post.

.. note::
    In future versions, some tags will be expanded to pages, and more
    tags will be included:

    +---------------+------------------------------------------+------+------+
    | Meta tag      | Description                              | Post | Page |
    +===============+==========================================+======+======+
    | ``language``  | Language for this particular content     | Yes  | Yes  |
    +---------------+------------------------------------------+------+------+
    | ``slug``      | Slug of the post/page defined by user    | Yes  | Yes  |
    +---------------+------------------------------------------+------+------+

On the date format
------------------

The date accepts a very wide list of variants.  It doesn't need to be
very specific, just with a format ``MM-DD-YYYY`` is enough, although it
also takes a more complex form.  General valid examples are:

* ``MM/DD/YYYY [HH[:MM[:SS]]] [TIMEZONE]``
* ``DD/MM/YYYY [HH[:MM[:SS]]] [TIMEZONE]``
* ``MM-DD-YYYY [HH[:MM[:SS]]] [TIMEZONE]``
* ``DD-MM-YYYY [HH[:MM[:SS]]] [TIMEZONE]``

Take into consideration that the day/month fields depend on the locale
setting. For example, entering ``03-11-2020`` will be understood as:

* Nov  3, 2020: ``DD-MM-YYYY`` in European locales; and
* Mar 11, 2020: ``MM-DD-YYYY`` in English related locales.

For this, it's recommended to use the ISO 8601 standard: ``YYYY-MM-DD``,
that eliminates all ambiguity.  Or, you may use another ways of
specifying the date, such as:

* ``2020 11 Mar``
* ``11 Mar 2020``
* ``Mar 11 2020``

You could use the date, time, and timezone fields in any order.  The
following are also some valid formats:

* ``[HH[:MM[:SS]]] YYYY/MM/DD [TIMEZONE]``
* ``[HH[:MM[:SS]]] [TIMEZONE] YYYY/MM/DD``
* ``[TIMEZONE] YYYY-MM-DD [HH[:MM[:SS]]]``

Text body
---------

It's just regular Markdown or reStructuredText syntax with some loaded
extensions, such as tables, abbreviations, footnotes, definition lists,
and code highlighting when writing snippets of source code.

To learn about Markdown syntax elements, see:

* `Markdown Syntax Guide`_
* `Markdown Cheat Sheet`_

To learn about reStructuredText elements, visit:

* `Quick reStructuredText`_
* `reStructuredText Markup Specification`_

Internal links
--------------

To reference a resource (file, image,...) on the website, just use write
in Markdown the link, noting that the root of the website is ``/``.

For example, to make a link to a PDF file in
``/media/pdfs/document1.pdf`` in **Markdown**::

    This is the [link](/media/pdfs/document1.pdf)

and, in **restructuredtext**::

    This is the `link </media/pdfs/document1.pdf>`_

or, to include an image in **Markdown**::

    My image ![This is a logo](/media/images/logo.png) is here

and, in **restructuredtext**::

    My image |logo| is here

    .. |logo| image:: /media/images/logo.png

But those are just some minimal examples.  Both Markdown and
reStructuredText have a lot of different configurations and variations.
Read the syntax guides for those markup languages.

Currently there's no way to reference another post, unless you know the
year, month, date, and slug.  In that case you can add the link::

    Markdown: [my other post](/posts/2020/03/11/my-other-post)
    reStructuredText: `my other post </posts/2020/03/11/my-other-post>`_

Future versions improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In future versions, there will be an easy way to reference other
internal posts and pages by writing:

* ``this { linkpost file_name_of_post }{alt name}``
* ``this { linkpage file_name_of_post }{alt name}``

or, links to categories or tags:

* ``this tag: { linktag tag_name }{alt name}``
* ``this cat: { linkcat cat-name }{alt name}``

As well of including text from other files using:

* ``{ source media/files/lipsum.txt }``
* ``{ source media/files/data.c }``



.. _`Markdown Syntax Guide`:
    https://sourceforge.net/p/digitalsign/wiki/markdown_syntax/

.. _`Markdown Cheat Sheet`:
    https://www.markdownguide.org/cheat-sheet/

.. _`Quick reStructuredText`:
    https://docutils.sourceforge.io/docs/user/rst/quickref.html

.. _`reStructuredText Markup Specification`:
    https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
