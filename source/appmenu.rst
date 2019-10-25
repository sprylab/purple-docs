########
App Menu
########

The app menu is a global app UI component which is used for navigation.
It consists of a header area, dynamic entries and a footer area.
The configuration of this menu happens in the :code:`app_menu.xml` file that is
located in the :doc:`dynamic resources </apps/dynamic_resources>`.

.. hint:: All values must be properly escaped as required by the XML standard.

.. |logo1| image:: img/app_menu_android.png
    :scale: 16%
    :align: middle

.. |logo2| image:: img/app_menu_ios.png
    :scale: 19%
    :align: middle

.. table::

   +---------+---------+
   | |logo1| | |logo2| |
   +---------+---------+

Sections
########

Navigation Header / Footer
**************************

The app menu can be configured to show custom logos at the top and bottom.

There can only be one :code:`navigationHeader` and one :code:`navigationFooter`
element. Both are optional. These elements can contain :code:`image` and
:code:`search` child elements.

The :code:`image` element has a required :code:`URL` and :code:`height` attribute
and can optionally also specify a background color and padding at each side.

The :code:`search` element can be used to insert the search field in the menu.
If the :code:`navigationHeader` is used a :code:`search` element must be added
if the search should be shown. If it is missing no search will be visible.

.. note::

  If the search is disabled through the app property adding a :code:`search`
  element will have no effect - no search will be visible.

Example
=======

.. toggle-box:: Structure

  .. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <app_menu>
        <navigationHeader>
            <image URL="top_logo.png"
                   height="20.0"
                   backgroundColor="#fefefe45"
                   paddingLeft="10.0"
                   paddingTop="20.0"
                   paddingRight="30.0"
                   paddingBottom="40.0" />
            <search />
        </navigationHeader>

        <navigation type="app_menu">
            <navigationNode targetURL="beliebige Url">
                <title>Title of this entry</title>
                <iconURL>Icon_for_this_entry.png</iconURL>
            </navigationNode>
        </navigation>

        <navigationFooter>
            <image URL="bottom_logo.png"
                   height="20.0"
                   backgroundColor="#fefefe45"
                   paddingLeft="10.0"
                   paddingTop="20.0"
                   paddingRight="30.0"
                   paddingBottom="40.0" />
        </navigationFooter>
    </app_menu>


Search
======

The search field allows searching for issues in the kiosk. It requires internet access as the actual search is done by the Purple Manager.
The field will only be visible if the app property :code:`kiosk_search_enabled` is enabled.

.. note::

  This feature is not available on the web platform.

Dynamic Entries
***************

This part of the app menu can be freely customized using :code:`navigationNode` nodes in the :code:`app_menu.xml`.
There are some special entries that are being added to the app menu even if they are not declared in the :code:`app_menu.xml` such as the :code:`current issue` or the :code:`settings` entry.

Current Issue
=============

This entry is only visible in single issue apps and navigates to the issue.

Settings
========

Opens a screen where the user can change app settings, e.g. if usage analysis is allowed or storage settings on Android.

This entry is only visible if there are settings available in the app, e.g. tracking or crash reporting or SD card support (only Android) is enabled, so that the user can opt-out.

If no :code:`navigationNode` with the action url :code:`purple://app/settings/open` is
declared in the :code:`app_menu.xml` but there are settings available in the app,
then a default settings entry is automatically added at the end of the app menu

Configuration
=============

Each :code:`navigationNode` entry represents an item in the app menu.

The :code:`targetURL` attribute describes the action that will be called when that
entry is clicked. This can be either an action url or a web url.

The title of an entry can be set by adding a :code:`title` node inside the :code:`navigationNode`.

.. note::

  Menu entries which are not supported on the web platform will be filtered out and not visible in the app menu in the web newsstand.
  A warning popup will inform the user about this in the preview version of the web newsstand.

Translations
------------

As of release 3.11 it is now also possible to set translations in the app menu, so that there is no need to make specific folders. This can be done by adding multiple :code:`title` nodes with :code:`locale` attributes as shown in the following example.
The resolution strategy is the same as the one for the localization folders in the dynamic resources. For further details on the resolution strategy see :ref:`Localization <dyn-res-localization>`.

.. toggle-box:: Translated entries

  .. code-block:: xml

    <navigationNode targetURL="http://google.com">
        <title>default Title</title>
        <title locale="de">German Title</title>
        <title locale="en">English Title</title>
    </navigationNode>

Custom-Icons
------------

Each :code:`navigationNode` can have an :code:`activateIconURL` and an :code:`iconURL` which define the icon that is shown next to the entry.
These icons are then colored according to its state by the properties :code:`app_menu_icon_active_color` and :code:`app_menu_icon_normal_color`

.. toggle-box:: Icon states

  .. code-block:: xml

    <navigationNode targetURL="purple://app/resource/dynamic/faq.html">
        <title>FAQ</title>
        <iconURL>faq_icon.png</iconURL>
        <activeIconURL>faq_icon_active.png</activeIconURL>
    </navigationNode>

At last it is also possible to leave icons in different resolutions by adding :code:`@2x` and :code:`@3x` to the filename. The app then selects the best suited resolution at runtime.

.. toggle-box:: Example: Icons and resolutions

  +-------------------+------------------+
  | Filename          |  Resolution      |
  +===================+==================+
  |  faq_icon.png     |  40 x 40 px      |
  +-------------------+------------------+
  |  faq_icon\@2x.png |  80 x 80 px      |
  +-------------------+------------------+
  |  faq_icon\@3x.png |  120 x 120 px    |
  +-------------------+------------------+

.. _dyn-res-app-menu-roles:

Role-Filters
------------

Starting with version 2.6.0 app menu entries can be filtered by user roles. This is done by adding an :code:`access` attribute to the :code:`navigationNode`.
A complete list of roles and access expressions can be found in the :ref:`roles <entitlement-user-roles>` section.
If the :code:`access` attribute is not set, then it defaults to the :code:`permitAll` expression.

.. toggle-box:: Example Login and logout based on roles

  This app menu will show the login entry only for logged out users and the logout entry only for logged in users.

  The other entries are always visible.

  .. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <app_menu>
        <navigation type="app_menu">
            <navigationNode targetURL="purple://kiosk/feed/open">
                <title>Newsfeed</title>
                <iconURL>newsfeed_icon.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://kiosk/open">
                <title>Kiosk</title>
                <iconURL>kiosk_icon.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://kiosk/entitlement/login/open" access="ROLE_ANONYMOUS">
                <title>Login</title>
                <iconURL>login_icon.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://kiosk/entitlement/logout/perform" access="AUTHENTICATED">
                <title>Logout</title>
                <iconURL>logout_icon.png</iconURL>
            </navigationNode>
        </navigation>
    </app_menu>

.. toggle-box:: Example complete app.xml

  .. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <app_menu>
        <navigationHeader>
            <image URL="logo.png" height="100.0" />
            <search />
        </navigationHeader>
        <navigation type="app_menu">
            <navigationNode targetURL="purple://kiosk/feed/open">
                <title>Newsfeed</title>
                <iconURL>menuicons/newsfeed.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://kiosk/open">
                <title>Newsstand</title>
                <iconURL>menuicons/newsstand.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://kiosk/subscriptions/open">
                <title>Subscriptions</title>
                <iconURL>menuicons/subscriptions.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://app/bookmarks/open">
                <title>Bookmarks</title>
                <iconURL>menuicons/bookmarks.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="https://sprylab.com/home.html">
                <title>Website</title>
                <iconURL>menuicons/website.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://app/share_app_or_issue">
                <title>Share</title>
                <iconURL>menuicons/share.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://app/feedback/mail/open">
                <title>Feedback</title>
                <iconURL>menuicons/feedback.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://app/resource/dynamic/info/index.html">
                <title>Info/Contact</title>
                <iconURL>menuicons/legal.png</iconURL>
            </navigationNode>
            <navigationNode targetURL="purple://app/composer/connect/open">
                <title>Composer Connect</title>
                <iconURL>menuicons/chain.png</iconURL>
            </navigationNode>
        </navigation>
        <navigationFooter>
            <image URL="logo.png" height="100.0" />
        </navigationFooter>
    </app_menu>


Colors
======

.. property:: app_menu_background_color
  :color: blue
  :type: Color

  This property defines the background color of the app menu.

.. property:: app_menu_icon_active_color
  :color: blue
  :type: Color

  This property defines the color of the icon of the currently selected app menu entry.

.. property:: app_menu_icon_normal_color
  :color: blue
  :type: Color

  This property defines the color of the icon of the app menu entries in its normal state.

.. property:: app_menu_item_normal_background_color
  :color: blue
  :type: Color

  This property defines the background color of an app menu entry.

.. property:: app_menu_item_normal_text_color
  :color: blue
  :type: Color

  This property defines the text color of an app menu entry.

.. property:: app_menu_item_pressed_background_color
  :color: blue
  :type: Color

  This property defines the background color of an app menu entry that is currently being pressed.

.. property:: app_menu_item_pressed_text_color
  :color: blue
  :type: Color

  This property defines the text color of an app menu entry that is currently being pressed.

.. property:: app_menu_header_background_color
  :only-available-for: Android and Kindle
  :color: blue
  :type: Color

  This property defines the background color of the app menu header.

.. property:: app_menu_item_separator_color
  :only-available-for: iOS
  :color: blue
  :type: Color

  This property defines the color of the separator between app menu entries.
