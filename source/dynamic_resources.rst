#################
Dynamic Resources
#################

.. toctree::
  :hidden:

Overview
########

The dynamic resources are some files that can change some configuration (e.g. `App Menu`_, `Channels`_, `Tracking`_, ...) without submitting an app update.
The app checks for updated dynamic resources on every app start and resume.

Structure
#########

The minimal setup of the dynamic resources requires a ``default`` folder which contains the configuration files.

.. toggle-box:: Example

  ::

    default/
    ├── app_menu.xml
    ├── channel_configs.json
    ├── sharing.properties
    └── ...

.. _dyn-res-localization:

Localization
************

It is possible to add translations by adding folders such as ``de``, ``en`` or ``de_DE``, ``en_US`` next to the ``default`` folder.
Depending on the device's preferred languages the app loads the best fitting configuration files from these folders.
Starting with Android 7.0 the system supports multiple preferred languages just like iOS. On earlier Android versions only the device's system language is used.
The look-up happens in the following way:

For each of the system's preferred language check if there is a folder that

1. matches the exact locale (e.g. ``de_DE`` or ``en_US``)

2. matches the exact language (e.g. use ``en`` folder for ``en_US``)

3. uses the same language but different region (e.g. use ``en_UK`` folder for ``en_US``)

In the case that there is no matching folder, the configuration falls back to the contents of the ``default`` folder.

.. toggle-box:: Example: Resource resolution

  Dynamic resources:

  ::

    /
    ├── default/
    ├── de_DE/
    └── it_IT/

  |

  Preferred languages:

  1. fr_CH

  2. it_CH

  Resolution:

  1. check exact locale (fr_CH) -> no match

  2. check exact language (fr) -> no match

  3. check same language but different region (fr) -> no match

  4. check exact locale (it_CH) -> no match

  5. check exact language (it) -> no match

  6. check same language but different region (it) -> it_IT

.. toggle-box:: Example: Different sharing settings

  ::

    /
    ├── default/
    │   ├── app_menu.xml
    │   ├── channel_configs.json
    │   ├── sharing.properties
    │   └── ...
    ├── en/
    │   └── sharing.properties
    └── de/
        └── sharing.properties

Platform-specific Configuration
*******************************

Additionally to translations it is also possible to add platform-specific configurations. This is done by adding some platform folders such as ``android``, ``ios``, ``kindle`` or ``web``. The structure of these folders is the same as mentioned above.

.. toggle-box:: Example: Platform-specific structure

  ::

    /
    ├── android/
    │   ├── default/
    │   │   └── app_menu.xml
    │   ├── en/
    │   │   └── app_menu.xml
    │   └── de/
    │       └── app_menu.xml
    ├── ios/
    │   ├── default/
    │   │   └── app_menu.xml
    │   ├── en/
    │   │   └── app_menu.xml
    │   └── de/
    │       └── app_menu.xml
    ├── web/
    │   ├── default/
    │   │   └── app_menu.xml
    │   ├── en/
    │   │   └── app_menu.xml
    │   └── de/
    │       └── app_menu.xml
    ├── en/
    │   ├── channel_configs.json
    │   └── sharing.properties
    ├── de/
    │   ├── channel_configs.json
    │   └── sharing.properties
    └── default/
        ├── channel_configs.json
        └── sharing.properties

.. toggle-box:: Result on Android

  ::

    /
    ├── default/
    │   ├── app_menu.xml (android-default)
    │   ├── channel_configs.json (default)
    │   └── sharing.properties (default)
    ├── en/
    │   ├── app_menu.xml (android-en)
    │   ├── channel_configs.json (default)
    │   └── sharing.properties (default)
    └── de/
       ├── app_menu.xml (android-de)
       ├── channel_configs.json (default)
       └── sharing.properties (default)

.. toggle-box:: Result on iOS

  ::

    /
    ├── default/
    │   ├── app_menu.xml (ios-default)
    │   ├── channel_configs.json (default)
    │   └── sharing.properties (default)
    ├── en/
    │   ├── app_menu.xml (ios-en)
    │   ├── channel_configs.json (default)
    │   └── sharing.properties (default)
    └── de/
       ├── app_menu.xml (ios-de)
       ├── channel_configs.json (default)
       └── sharing.properties (default)

.. toggle-box:: Result on web

  ::

    /
    ├── default/
    │   ├── app_menu.xml (web-default)
    │   ├── channel_configs.json (default)
    │   └── sharing.properties (default)
    ├── en/
    │   ├── app_menu.xml (web-en)
    │   ├── channel_configs.json (default)
    │   └── sharing.properties (default)
    └── de/
       ├── app_menu.xml (web-de)
       ├── channel_configs.json (default)
       └── sharing.properties (default)

If two folders contain the same file, then the more specific file overwrites the more generic one. E.g. some file in ``default`` gets overwritten by the same file from ``android``.

Configuration
#############

.. _dyn-res-app-menu:

App Menu
********

The app's side menu can be configured using the :code:`app_menu.xml` file.
For a detailed explanation of all its features and configuration see :doc:`App Menu </apps/appmenu>`.

.. _dyn-res-dynamicconfig:

Dynamic Configuration
*********************

Starting with PK 5.2.0 it is possible to place a :code:`config.json` in the dynamic resources.
This is a simple key-value file which can be used by the app for some dynamic configuration.

Currently only the :code:`onboarding_version` key is used by the app to determine the version of the current onboarding.

.. _dyn-res-channels:

Channels
********

Configuration
=============

The channel view can be set up using the ``channel_configs.json``. This file consists of multiple configurations for device types and orientations.

.. toggle-box:: Structure

  ::

    {
        "phone": {
            "portrait": {
                ...
            },
            "landscape": {
                ...
            }
        },
        "tablet": {
            "portrait": {
                ...
            },
            "landscape": {
                ...
            }
        }
    }

Inside those nodes is where the actual configuration lies. The first part of that node contains the general configuration, such as the ideal teaser size and the visibility of some page indicators.

.. toggle-box:: Example: General configuration

  ::

    "multiColumn": false,
    "teaserWidth": 256,
    "teaserHeight": 144,
    "pageArrowsEnabled": false,
    "pageIndicatorsEnabled": true,
    "pageIndicatorAlignment": "right",

+------------------------+---------+---------------------+----------------------------------------------------------+
| Name                   | Type    | Values              | Description                                              |
+========================+=========+=====================+==========================================================+
| multiColumn            | boolean | true, false         | defines whether there are multiple columns of teasers    |
+------------------------+---------+---------------------+----------------------------------------------------------+
| teaserWidth            | int     |                     | defines the ideal tile width in dp                       |
+------------------------+---------+---------------------+----------------------------------------------------------+
| teaserHeight           | int     |                     | defines the ideal tile height in dp                      |
+------------------------+---------+---------------------+----------------------------------------------------------+
| pageArrowsEnabled      | boolean | true, false         | toggles the pages arrows on the side of the screen       |
+------------------------+---------+---------------------+----------------------------------------------------------+
| pageIndicatorsEnabled  | boolean | true, false         | toggles the page indicator dots on the top of the screen |
+------------------------+---------+---------------------+----------------------------------------------------------+
| pageIndicatorAlignment | String  | left, center, right | sets the position of the page indicator dots             |
+------------------------+---------+---------------------+----------------------------------------------------------+

The teaserWidth and teaserHeight define the layout of the channel. These values are in density-independent pixels (dp). A list of some common devices and their screen sizes in dp can be found `here <https://design.google.com/devices/>`_.
If ``multiColumn`` is ``true``, then the layout process tries to fit as many teasers next to each other as possible. While doing so, the teasers are never scaled down, so e.g. on a display with 1024 dp in the width only 4 tiles with a width of 250 dp can be displayed.
Once the amount of column is calculated, the tiles are stretched equally to fill the screen while maintaining the aspect ratio defined by the teaserWidth and teaserHeight.

The next part of the configuration defines the teaser types. Currently there are only two types: ``topTeaser`` which is the first teaser in a channel and ``teaser`` for all the remaining ones.

.. toggle-box:: Example: Teaser types

  ::

    "types": {
        "topTeaser": {
            "thumbnailKind" : "phone_portrait_top",
            "factorY": 1,
            "spanX": 1,
            "spanY": 1,
            "gradient": {
                "height": 0.6,
                "alphaStart": 1.0,
                "alphaEnd": 0.0
            },
            "title": {
                "fontSize": 20,
                "font": "Roboto-Condensed",
                "maxLines": 3
            },
            "headline": {
                "fontSize": 12,
                "font": "Roboto-Condensed",
                "maxLines": 1
            }
        },
        "teaser": {
            "thumbnailKind" : "phone_portrait_normal",
            "gradient": {
                "height": 0.6,
                "alphaStart": 1.0,
                "alphaEnd": 0.0
            },
            "title": {
                "fontSize": 20,
                "font": "Roboto-Condensed",
                "maxLines": 3
            },
            "headline": {
                "fontSize": 12,
                "font": "Roboto-Condensed",
                "maxLines": 1
            }
        }
    }

The configuration for both teaser types is mostly the same. The ``topTeaser`` has three additional attributes. The ``factorY`` is only evaluated when ``multiColumn`` is ``false``. In this case the first teaser's height is multiplied by this value.
For the case that ``multiColumn`` is ``true``, then the top teaser's width is multiplied by the value of ``spanX`` and its height is multiplied by ``spanY``.

+---------+-------+--------------------------------------------------------------------+
| Name    | Type  | Description                                                        |
+=========+=======+====================================================================+
| factorY | float | (multiColumn=false) multiplier for the height of the top teaser    |
+---------+-------+--------------------------------------------------------------------+
| spanX   | int   | (multiColumn=true) amount of columns that the top teaser will take |
+---------+-------+--------------------------------------------------------------------+
| spanY   | int   | (multiColumn=true) amount of rows that the top teaser will take    |
+---------+-------+--------------------------------------------------------------------+

The rest of the configuration consists of a ``thumbnailKind`` which defines the teaser image that is loaded from the Purple Manager, the ``gradient`` which configures the gradient behind the text and at last the ``headline`` and ``title`` nodes which define the configuration for the article title and article description respectively. The ``thumbnailKind`` is a value that is a composition of the device type (phone or tablet), the device orientation (portrait or landscape) and the teaser type (normal or top). Valid values are e.g. ``phone_portrait_top`` or ``tablet_landscape_normal``.

+------------+-------+-----------------------------------------------------------------------------+
| Name       | Type  | Description                                                                 |
+============+=======+=============================================================================+
| height     | float | the height of the gradient ranged from 0 to 1 where 1 means the full height |
+------------+-------+-----------------------------------------------------------------------------+
| alphaStart | float | the transparency value at the bottom of the gradient                        |
+------------+-------+-----------------------------------------------------------------------------+
| alphaEnd   | float | the transparency value at the top of the gradient                           |
+------------+-------+-----------------------------------------------------------------------------+

The upper text is called ``headline`` and it displays the article's **title**. The lower text is called ``title`` and contains the article's **description** text. Both of these texts have configurable sizes, fonts and maximum lines which can be set in their respective configuration nodes.

+----------+--------+---------------------+
| Name     | Type   | Description         |
+==========+========+=====================+
| fontSize | int    | size of the text    |
+----------+--------+---------------------+
| font     | String | name of the font    |
+----------+--------+---------------------+
| maxLines | int    | max amount of lines |
+----------+--------+---------------------+

Currently colors can only be configured in the Purple Manager.

.. toggle-box:: Example: Complete example configuration

  ::

    {
        "phone": {
            "portrait": {
                "multiColumn": false,
                "teaserWidth": 256,
                "teaserHeight": 144,
                "pageArrowsEnabled": false,
                "pageIndicatorsEnabled": true,
                "pageIndicatorAlignment": "right",
                "types": {
                    "topTeaser": {
                        "thumbnailKind" : "phone_portrait_top",
                        "factorY": 1,
                        "spanX": 1,
                        "spanY": 1,
                        "gradient": {
                            "height": 0.6,
                            "alphaStart": 1.0,
                            "alphaEnd": 0.0
                        },
                        "title": {
                            "fontSize": 20,
                            "font": "Roboto-Condensed",
                            "maxLines": 3
                        },
                        "headline": {
                            "fontSize": 12,
                            "font": "Roboto-Condensed",
                            "maxLines": 1
                        }
                    },
                    "teaser": {
                        "thumbnailKind" : "phone_portrait_normal",
                        "gradient": {
                            "height": 0.6,
                            "alphaStart": 1.0,
                            "alphaEnd": 0.0
                        },
                        "title": {
                            "fontSize": 20,
                            "font": "Roboto-Condensed",
                            "maxLines": 3
                        },
                        "headline": {
                            "fontSize": 12,
                            "font": "Roboto-Condensed",
                            "maxLines": 1
                        }
                    }
                }
            },
            "landscape": {
                "multiColumn": true,
                "teaserWidth": 256,
                "teaserHeight": 144,
                "pageArrowsEnabled": false,
                "pageIndicatorsEnabled": true,
                "pageIndicatorAlignment": "left",
                "types": {
                    "topTeaser": {
                        "thumbnailKind" : "phone_landscape_top",
                        "factorY": 1.5,
                        "spanX": 2,
                        "spanY": 2,
                        "gradient": {
                            "height": 0.6,
                            "alphaStart": 1.0,
                            "alphaEnd": 0.0
                        },
                        "title": {
                            "fontSize": 20,
                            "font": "Roboto-Condensed",
                            "maxLines": 3
                        },
                        "headline": {
                            "fontSize": 12,
                            "font": "Roboto-Condensed",
                            "maxLines": 1
                        }
                    },
                    "teaser": {
                        "thumbnailKind" : "phone_landscape_normal",
                        "gradient": {
                            "height": 0.6,
                            "alphaStart": 1.0,
                            "alphaEnd": 0.0
                        },
                        "title": {
                            "fontSize": 20,
                            "font": "Roboto-Condensed",
                            "maxLines": 3
                        },
                        "headline": {
                            "fontSize": 12,
                            "font": "Roboto-Condensed",
                            "maxLines": 1
                        }
                    }
                }
            }
        },
        "tablet": {
            "portrait": {
                "multiColumn": true,
                "teaserWidth": 256,
                "teaserHeight": 144,
                "pageArrowsEnabled": false,
                "pageIndicatorsEnabled": true,
                "pageIndicatorAlignment": "center",
                "types": {
                    "topTeaser": {
                        "thumbnailKind" : "tablet_portrait_top",
                        "factorY": 1.5,
                        "spanX": 2,
                        "spanY": 2,
                        "gradient": {
                            "height": 0.6,
                            "alphaStart": 1.0,
                            "alphaEnd": 0.0
                        },
                        "title": {
                            "fontSize": 28,
                            "font": "Roboto-Condensed",
                            "maxLines": 3
                        },
                        "headline": {
                            "fontSize": 23,
                            "font": "Roboto-Condensed",
                            "maxLines": 1
                        }
                    },
                    "teaser": {
                        "thumbnailKind" : "tablet_portrait_normal",
                        "gradient": {
                            "height": 0.6,
                            "alphaStart": 1.0,
                            "alphaEnd": 0.0
                        },
                        "title": {
                            "fontSize": 17,
                            "font": "Roboto-Condensed",
                            "maxLines": 3
                        },
                        "headline": {
                            "fontSize": 14,
                            "font": "Roboto-Condensed",
                            "maxLines": 1
                        }
                    }
                }
            },
            "landscape": {
                "multiColumn": true,
                "teaserWidth": 341,
                "teaserHeight": 192,
                "pageArrowsEnabled": true,
                "pageIndicatorsEnabled": false,
                "pageIndicatorAlignment": "center",
                "types": {
                    "topTeaser": {
                        "thumbnailKind" : "tablet_landscape_top",
                        "factorY": 1.5,
                        "spanX": 2,
                        "spanY": 2,
                        "gradient": {
                            "height": 0.6,
                            "alphaStart": 1.0,
                            "alphaEnd": 0.0
                        },
                        "title": {
                            "fontSize": 29,
                            "font": "Roboto-Condensed",
                            "maxLines": 3
                        },
                        "headline": {
                            "fontSize": 14,
                            "font": "Roboto-Condensed",
                            "maxLines": 1
                        }
                    },
                    "teaser": {
                        "thumbnailKind" : "tablet_landscape_normal",
                        "gradient": {
                            "height": 0.6,
                            "alphaStart": 1.0,
                            "alphaEnd": 0.0
                        },
                        "title": {
                            "fontSize": 17,
                            "font": "Roboto-Condensed",
                            "maxLines": 3
                        },
                        "headline": {
                            "fontSize": 11,
                            "font": "Roboto-Condensed",
                            "maxLines": 1
                        }
                    }
                }
            }
        }
    }

Background Image
----------------

The default background image for the channel tiles can be changed by adding a ``channel_placeholder.png`` image to the dynamic resources. Just like other images, it is possible to leave multiple images with different resolutions.

Tutorials
==========

Channel tutorials can be configured in the ``onboarding_channel_overview.json`` file. It consists of two configurations, one for portrait and landscape each.

.. toggle-box:: Structure

  ::

    {
        "phone": {
            "config": {
                   ...
            }
        },
        "tablet": {
            "config": {
                   ...
            }
        }
    }

The first part of the ``config`` node consists of the style configuration. This is currently only evaluated by iOS. For Android devices colors have to be set in the Purple Manager.

.. toggle-box:: Example: Style configuration

  ::

    "delay": 1.0,
    "titleFontSize": 22.0,
    "titleFontPostScriptName": "Roboto-Condensed",
    "titleTextColor": "#f00000ff",
    "titleShadowEnabled": true,
    "captionFontSize": 18.0,
    "captionFontPostScriptName": "Roboto-Condensed",
    "captionTextColor": "#ffffffff",
    "captionShadowEnabled": true,
    "buttonFontSize": 18.0,
    "buttonFontPostScriptName": "Roboto-Condensed",
    "buttonTextColor": "#ffffffff",
    "buttonBackgroundColor": "#f00000ff",
    "focusRingColor": "#f0000000",

The next part defines the initial tutorial screen. Its possible to set texts for the title, description, footer and button here. Also there is an option to disable the initial tutorial screen.

.. toggle-box:: Example: Initial tutorial screen configuration

  ::

    "intro":
    {
        "enabled": true,
        "title": "Die neue Channel App",
        "description": "Erleben Sie multimedial aufbereitete Ausgaben und News in einer App!",
        "labelFormat": "",
        "buttonTitle": "Los geht's"
    },

The configuration of the initial screen is followed by the header config. The header is shown at the top of the display for the whole duration of the tutorial. Its also possible to disable the header.

.. toggle-box:: Example: Header configuration

  ::

    "header":
    {
        "enabled": false,
        "title": "",
        "subtitle": ""
    },

At last the configuration for the individual tutorial screens happens. The ``views`` node is a list that contains configurations for all the screens that are shown during the tutorial. These screens will be displayed in the same order as they are defined in the file. These entries are mostly the same as config for the initial screen with the exception of one additional value. The ``name`` value defines the item that will be highlighted by the current tutorial screen. Currently only the following values are supported.

+---------------------------+---------------------------------------------------------+
| Name                      | Description                                             |
+===========================+=========================================================+
| left_side_panel_button    | the menu button on the top left of the screen           |
+---------------------------+---------------------------------------------------------+
| any_channel_article       | first teaser on the screen                              |
+---------------------------+---------------------------------------------------------+
| channel_next_button       | the next channel button on the right side of the screen |
+---------------------------+---------------------------------------------------------+
| channel_page_indicator    | channel indicator dots on the top of the screen         |
+---------------------------+---------------------------------------------------------+

.. toggle-box:: Example: Views configuration

  ::

    "views": [
         {
         "name": "left_side_panel_button",
         "enabled": true,
         "title": "Seitenmenü",
         "description": "Ihre digitalen Ausgaben können Sie im KIOSK herunterladen.",
         "labelFormat": "Tipp %d von %d",
         "buttonTitle": "Weiter"
         },
         {
         "name": "any_channel_article",
         "enabled": true,
         "title": "Täglich neue Artikel",
         "description": "Täglich aktuelle Artikel für Sie ausgewählt.",
         "buttonTitle": "Weiter",
         "labelFormat": "Tipp %d von %d",
         "scale": 0.7
         },
         {
         "name": "channel_next_button",
         "enabled": false,
         "title": "Weitere Kategorien",
         "description": "Per Swipe zu vielen weiteren Kategorien und Videos gelangen! ",
         "labelFormat": "Tipp %d von %d",
         "buttonTitle": "Fertig"
         },
         {
         "name": "channel_page_indicator",
         "enabled": true,
         "title": "Weitere Kategorien",
         "description": "Per Swipe zu vielen weiteren Kategorien und Videos gelangen! ",
         "labelFormat": "Tipp %d von %d",
         "buttonTitle": "Fertig"
         }
         ]
    }

.. toggle-box:: Example: Full example tutorial configuration

  ::

    {
        "phone": {
            "config": {
                "delay": 1.0,
                "titleFontSize": 22.0,
                "titleFontPostScriptName": "Roboto-Condensed",
                "titleTextColor": "#f00000ff",
                "titleShadowEnabled": true,
                "captionFontSize": 18.0,
                "captionFontPostScriptName": "Roboto-Condensed",
                "captionTextColor": "#ffffffff",
                "captionShadowEnabled": true,
                "buttonFontSize": 18.0,
                "buttonFontPostScriptName": "Roboto-Condensed",
                "buttonTextColor": "#ffffffff",
                "buttonBackgroundColor": "#f00000ff",
                "focusRingColor": "#f0000000",
                "intro":
                {
                    "enabled": true,
                    "title": "Die neue Channel App",
                    "description": "Erleben Sie multimedial aufbereitete Ausgaben und News in einer App!",
                    "labelFormat": "",
                    "buttonTitle": "Los geht's"
                },
                "header":
                {
                    "enabled": false,
                    "title": "",
                    "subtitle": ""
                },
                "views": [
                          {
                          "name": "left_side_panel_button",
                          "enabled": true,
                          "title": "Seitenmenü",
                          "description": "Ihre digitalen Ausgaben können Sie im KIOSK herunterladen.",
                          "labelFormat": "Tipp %d von %d",
                          "buttonTitle": "Weiter"
                          },
                          {
                          "name": "any_channel_article",
                          "enabled": true,
                          "title": "Täglich neue Artikel",
                          "description": "Täglich aktuelle Artikel für Sie ausgewählt.",
                          "buttonTitle": "Weiter",
                          "labelFormat": "Tipp %d von %d",
                          "scale": 0.7
                          },
                          {
                          "name": "channel_next_button",
                          "enabled": false,
                          "title": "Weitere Kategorien",
                          "description": "Per Swipe zu vielen weiteren Kategorien und Videos gelangen! ",
                          "labelFormat": "Tipp %d von %d",
                          "buttonTitle": "Fertig"
                          },
                          {
                          "name": "channel_page_indicator",
                          "enabled": true,
                          "title": "Weitere Kategorien",
                          "description": "Per Swipe zu vielen weiteren Kategorien und Videos gelangen! ",
                          "labelFormat": "Tipp %d von %d",
                          "buttonTitle": "Fertig"
                          }
                          ]
            }
        },
        "tablet": {
            "config": {
                "delay": 1.0,
                "titleFontSize": 22.0,
                "titleFontPostScriptName": "Roboto-Condensed",
                "titleTextColor": "#f00000ff",
                "titleShadowEnabled": true,
                "captionFontSize": 18.0,
                "captionFontPostScriptName": "Roboto-Condensed",
                "captionTextColor": "#ffffffff",
                "captionShadowEnabled": true,
                "buttonFontSize": 18.0,
                "buttonFontPostScriptName": "Roboto-Condensed",
                "buttonTextColor": "#ffffffff",
                "buttonBackgroundColor": "#f00000ff",
                "focusRingColor": "#f0000000",
                "intro":
                {
                    "enabled": true,
                    "title": "Die neue Channel App",
                    "description": "Erleben Sie multimedial aufbereitete Ausgaben und News in einer App!",
                    "labelFormat": "",
                    "buttonTitle": "Los geht's"
                },
                "header":
                {
                    "enabled": false,
                    "title": "",
                    "subtitle": ""
                },
                "views": [
                          {
                          "name": "left_side_panel_button",
                          "enabled": true,
                          "title": "Seitenmenü",
                          "description": "Ihre digitalen Ausgaben können Sie im KIOSK herunterladen.",
                          "labelFormat": "Tipp %d von %d",
                          "buttonTitle": "Weiter"
                          },
                          {
                          "name": "any_channel_article",
                          "enabled": true,
                          "title": "Täglich neue Artikel",
                          "description": "Täglich aktuelle Artikel für Sie ausgewählt.",
                          "buttonTitle": "Weiter",
                          "labelFormat": "Tipp %d von %d",
                          "scale": 0.5
                          },
                          {
                          "name": "channel_next_button",
                          "enabled": true,
                          "title": "Weitere Kategorien",
                          "description": "Per Swipe zu vielen weiteren Kategorien und Videos gelangen! ",
                          "labelFormat": "Tipp %d von %d",
                          "buttonTitle": "Fertig"
                          },
                          {
                          "name": "channel_page_indicator",
                          "enabled": false,
                          "title": "Weitere Kategorien",
                          "description": "Per Swipe zu vielen weiteren Kategorien und Videos gelangen! ",
                          "labelFormat": "Tipp %d von %d",
                          "buttonTitle": "Fertig"
                          }
                          ]
            }
        }
    }

Tracking
********

The tracking is configured by editing ``tracking_config.json``. For further details about configuring tracking see: :doc:`Tracking </tracking>`

.. _dynamic-resources-sharing:

Sharing
*******

The ``sharing.properties`` contains the texts that will displayed during the share process. This file will be evaluated by the Purple Manager and not the app itself. The contents of this file will be delivered to the app during the status request which happens on every app start.
The purpose of this file is to set an app url and texts that will be printed during app or issue shares.

.. toggle-box:: Example

  ::

    app.url=http://www.example.com
    app=Hallo, ich möchte Dir die App empfehlen: {appUrl}
    issue=Hallo, folgende Ausgabe möchte ich dir empfehlen: {issueUrl} Hier kannst Du dir die App herunterladen: http://www.example.com

    app.plaintext=Hallo, ich möchte Dir die App empfehlen
    issue.plaintext=Hallo, folgende Ausgabe möchte ich dir empfehlen. Hier kannst Du dir die App herunterladen: http://www.example.com


.. hint:: This file must be encoded as ISO 8859-1.

.. _dyn-res-feedback-mail:

Feedback E-Mail
***************

The feedback e-mail can be configured using the ``email_feedback_config.json``, ``email_feedback_subject.mustache`` and ``email_feedback_body.mustache`` files.
The recipients can be set in the ``email_feedback_config.json``, while the other two files define the subject and the body for the e-mail.

Every file has a default configuration. These files can be configured independently.
You can override the default configuration by putting your custom configuration file into the root directory (e.g. default/email_feedback_body.mustache). Your custom file must have the same name like the default file.

All templates are encoded in UTF-8.

Placeholder for Templates
=========================

+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
| Key                   | Description                   | Example Value                                                   | Localization Key       |
+=======================+===============================+=================================================================+========================+
|  appName              |  app name                     |  "Example Test App"                                             |  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  appVersionLabel      |  label for app version        |  "App Version"                                                  |  app_version_title     |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  appVersion           |  app version                  |  "1.0-SNAPSHOT"                                                 |  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  versionSectionLabel  |  headline: version section    |  "Versionen"                                                    |  version_title         |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  deviceSectionLabel   |  headline: device section     |  "Device"                                                       |  device_title          |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  deviceModelLabel     |  label for device model       |  "Device Model"                                                 |  device_model          |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  deviceModel          |  device model                 |  "Pixel C"                                                      |  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  osVersionLabel       |  label for os version         |  "OS Version"                                                   |  os_version            |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  osVersion            |  os version                   |  Android: "7.0", iOS: ??                                        |  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  manufacturerLabel    |  label for manufacturer       |  "Manufacturer"                                                 |  manufacturer          |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  manufacturer         |  manufacturer of the device   |  Android: "Samsung" / "Google" etc, iOS: "Apple"                |  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  connectionLabel      |  label for connection         |  "Connection"                                                   |  connection            |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  connection           |  connection info              |  Android: z.B. "WIFI", iOS: "OFFLINE", "WIFI", "WWAN"           |  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  deviceIdLabel        |  label for device-id          |  "Device Id"                                                    |  device_id_title       |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  deviceId             |  device-id                    |  Android: 31c290b15bn6adee, iOS: 8C224FG9-4665-BEFO-834F2C7D7AFF|  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  purpleVersionBlock   |  all relevant Purple versions |  "Purple: 3.1.0, Engine: 2.0.0"                                 |  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+
|  platform             |  platform identifier          |  "Android", "Kindle" oder "iOS"                                 |  \-                    |
+-----------------------+-------------------------------+-----------------------------------------------------------------+------------------------+

|

Example for Files
=========================

.. toggle-box:: email_feedback_config.json

  .. code-block:: json

    {
      "recipients": {
        "to": [
          "receiver1@example.com",
          "receiver2@example.com"
        ],
        "cc": [
          "cc1@example.com",
          "cc2@example.com"
        ],
        "bcc": [
          "bcc1@example.com",
          "bcc2@example.com"
        ]
      }
    }

.. toggle-box:: email_feedback_subject.mustache

  .. code-block:: none

    {{appName}} - App Feedback ({{platform}})

.. toggle-box:: email_feedback_body.mustache

  .. code-block:: none

    --
    {{versionSectionLabel}}
    {{appVersionLabel}}: {{appVersion}}
    {{purpleVersionBlock}}

    {{deviceSectionLabel}}
    {{deviceModelLabel}}: {{deviceModel}}
    {{osVersionLabel}}: {{osVersion}}
    {{manufacturerLabel}}: {{manufacturer}}
    {{deviceIdLabel}}: {{deviceId}}
    {{connectionLabel}}: {{connection}}
