##########
Deep Links
##########

.. toctree::

.. container:: custom-text

  The deep links can be used inside the app and from outside.

  For internal use the link starts with :code:`purple: //` and for external starts with :code:`purple-<PACKAGE_NAME>://`.

  The package name of the app can be found on the app overview page in the Purple DS Manager.

  The :code:`<PACKAGE_NAME>` in the deep link has to be used in lower case even though the app's actual package name can contain capital letters.

.. toggle-box:: Example
  :color: transparent

  .. container:: custom-text

    Internal link :code:`purple://app/info/open`

    External link :code:`purple-com.sprylab.purple.apps.developertest://app/info/open`

|

App
###

.. versioned-toggle-box:: Open app information
  :color: blue
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0

  Opens the app information view.

  |

  **URL**

  purple://app/info/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Open app settings
  :color: blue
  :versionadded-android: 2.7.0
  :versionadded-iOS: 3.10.0

  Opens the app settings view. In this view it is possible to adjust the settings for the app, e.g. toggle tracking services.

  |

  .. hint::

    On iOS this will open the device settings app.

  |

  **URL**

  purple://app/settings/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Open app menu
  :color: blue
  :versionadded-android: 2.3.3
  :versionadded-iOS: 2.3.3
  :versionadded-web-kiosk: 3.10.0

  Opens the app menu. The menu remains open, if it is already open.

  |

  **URL**

  purple://app/menu/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Close app menu
  :color: blue
  :versionadded-android: 2.3.3
  :versionadded-iOS: 2.3.3
  :versionadded-web-kiosk: 3.10.0

  Closes the app menu. The menu remains closed, if it is already closed.

  |

  **URL**

  purple://app/menu/close

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Toggle app menu
  :color: blue
  :versionadded-android: 2.3.3
  :versionadded-ios: 2.3.3
  :versionadded-web-kiosk: 3.10.0

  Closes the app menu, if it was opened and opens the app menu if it was closed.

  |

  **URL**

  purple://app/menu/toggle

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Open bookmarks view
  :color: blue
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0

  Opens the bookmarks view.

  |

  **URL**

  purple://app/bookmarks/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Open composer connect
  :color: blue
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0
  :deprecated: 5.0 Composer Connect has been removed.

  Opens the **Composer Connect** view. Only works if the feature *Composer Connect* has been enabled in the Purple DS Manager.

  |

  **URL**

  purple://app/composer/connect/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Open feedback mail
  :color: blue
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0
  :versionadded-web-kiosk: 3.5.0

  Opens a pre-filled email for feedback as configured in the :ref:`dynamic resources <dyn-res-feedback-mail>`.

  |

  **URL**

  purple://app/feedback/mail/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. _deeplink-show-dynamic-html-content:

.. versioned-toggle-box:: Show dynamic html content
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-kiosk: 3.10.0
  :versionchanged: 3.10.0 added :code:`force_status_bar`, 3.11.0 added :code:`app_logo`, 3.14.0: added :code:`bounces` (iOS only), 5.1: added storefront variant

  Opens an html file from :doc:`dynamic resources </dynamic_resources>`.
  The app variant opens the html file on top of the current context while the storefront variant navigates to a kiosk context before opening the html.

  |

  **URL**

  purple://app/resource/dynamic/:code:`<PATH>`

  purple://storefront/resource/dynamic/:code:`<PATH>`

  purple://app/resource/dynamic/:code:`<PATH>`?display_mode= :code:`<VALUE>` &title_bar= :code:`<VALUE>` &controls= :code:`<VALUE>` &force_status_bar= :code:`<VALUE>` &app_logo= :code:`<VALUE>`

  purple://storefront/resource/dynamic/:code:`<PATH>`?display_mode= :code:`<VALUE>` &title_bar= :code:`<VALUE>` &controls= :code:`<VALUE>` &force_status_bar= :code:`<VALUE>` &app_logo= :code:`<VALUE>`

  .. role:: fg-red

  +------------------------+-----------------+
  | Parameter              | Optional        |
  +========================+=================+
  | PATH                   | :fg-red:`NO`    |
  +------------------------+-----------------+

  +------------------------+-----------------+-----------------------------------------------------------+
  | Query-Parameter        | Optional        | Values                                                    |
  +========================+=================+===========================================================+
  | display_mode           | :fg-green:`YES` | - :code:`embedded` app menu available (default)           |
  |                        |                 | - :code:`modal` no app menu available                     |
  +------------------------+-----------------+-----------------------------------------------------------+
  | title_bar              | :fg-green:`YES` | - :code:`true` show title bar (default)                   |
  |                        |                 | - :code:`false` no title bar                              |
  +------------------------+-----------------+-----------------------------------------------------------+
  | controls               | :fg-green:`YES` | - :code:`true` show navigation controls                   |
  |                        |                 | - :code:`false` no navigation controls (default)          |
  +------------------------+-----------------+-----------------------------------------------------------+
  | force_status_bar       | :fg-green:`YES` | - :code:`true` show status bar                            |
  |                        |                 | - :code:`false` no status bar (default)                   |
  +------------------------+-----------------+-----------------------------------------------------------+
  | app_logo               | :fg-green:`YES` | - :code:`true` show app logo in title bar instead of text |
  |                        |                 | - :code:`false` no app logo (default)                     |
  +------------------------+-----------------+-----------------------------------------------------------+
  | bounces                | :fg-green:`YES` | - :code:`true` allow bouncing when scrolling (default)    |
  |                        |                 | - :code:`false` no bouncing                               |
  |                        |                 |                                                           |
  |                        |                 | Note: only available for iOS                              |
  +------------------------+-----------------+-----------------------------------------------------------+

  .. hint::

    | The :code:`force_status_bar` parameter is ignored if the :code:`title_bar` parameter is :code:`true`. The title bar is always presented with a status bar.
    | The :code:`app_logo` parameter is ignored if the :code:`title_bar` parameter is :code:`false`. The app logo can only be shown if a title bar is shown.

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Share app or issue
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionchanged: 2.7.0 iOS Storytelling content is now supported.

  Shares the current issue if one is open. Otherwise the app is shared.

  |

  **URL**

  purple://app/share_app_or_issue

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Share app or issue or page
  :color: blue
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0

  Shares the current page if an issue is open and the property *Content Sharing* has been enabled in the Purple DS Manager.
  Otherwise the issue is shared if this is open.

  Shares the app if the kiosk is open.

  |

  **URL**

  purple://app/share_app_or_issue_or_page

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Open home
  :color: blue
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-kiosk: 3.4.0

  Opens the area of the app defined by the :code:`app_initial_screen_url` property such as Kiosk, Channel or some
  Website in the dynamic resources. Due to Channel and Websites in the dynamic resources not being implemented in web newsstand,
  the newsstand will always be referred to as `home` in that context.

  |

  **URL**

  purple://app/home/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Register push service
  :color: blue
  :versionadded-ios: 3.8.0

  .. warning::

    This action url is not supported on Android.

  Triggers the push registration for the application. This will display a system dialog asking for permission to receive push notifications.

  |

  **URL**

  purple://app/push/register

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Open external URL
  :color: blue
  :versionadded-android: 3.9.0
  :versionadded-ios: 3.9.0
  :versionadded-web-kiosk: 3.9.0

  Open the given URL by handing it over to the underlying OS.
  The URL has to be URL-encoded.

  |

  **URL**

  purple://app/open/external/url/:code:`URLEncodedURL`

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Open HTML onboarding
  :color: blue
  :versionadded-android: 3.10.1
  :versionadded-ios: 3.10.1

  Open HTML onboarding screen which is shown on first app start.
  This only works if HTML onboarding is enabled.

  |

  **URL**

  purple://app/onboarding/app_start/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

Kiosk
#####

.. versioned-toggle-box:: Open kiosk (newsstand)
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-kiosk: 3.2.0

  Opens the kiosk.

  |

  **URL**

  purple://kiosk/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Open channel (newsfeed)
  :color: purple
  :versionadded-android: 2.2.0
  :versionadded-ios: 2.1.0

  Opens the channel.

  |

  **URL**

  purple://kiosk/feed/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Open category chooser
  :color: purple
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.3.3
  :versionadded-web-kiosk: 3.2.0

  Opens the category chooser view.

  |

  **URL**

  purple://kiosk/category/chooser/open


  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Show issue preview
  :color: purple
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0

  Opens the preview view of an issue in the kiosk via its ID or its alias.

  |

  **URL**

  purple://kiosk/issue/``<ISSUE_ID>``/preview

  purple://kiosk/issue/alias/``<ISSUE_ALIAS>``/preview

  .. role:: fg-red

  +------------------------+-----------------+
  | Parameter              | Optional        |
  +========================+=================+
  | ISSUE_ID               | :fg-red:`NO`    |
  +------------------------+-----------------+
  | ISSUE_ALIAS            | :fg-red:`NO`    |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Entitlement login
  :color: purple
  :versionadded-android: 2.6.0
  :versionadded-ios: 2.6.0
  :versionadded-web-kiosk: 3.2.0

  Opens the entitlement login view.

  |

  **URL**

  purple://kiosk/entitlement/login/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Perform entitlement login
  :color: purple
  :versionadded-android: 2.6.0
  :versionadded-ios: 2.6.0
  :versionadded-web-kiosk: 3.2.0

  Performs the entitlement login using the provided **login_name**, **access_token** and **roles**.
  If the login was performed for an OAuth entitlement server, the **refresh_token** is
  used for refreshing the **access_token**.
  If the login was successful, the **url_encoded_action_url** will be opened.

  |

  **URL**

  purple://kiosk/entitlement/login/perform?login_name= ``<LOGIN_NAME>`` &token= ``<ACCESS_TOKEN>`` &roles= ``<ROLES>`` &refresh_token= ``<REFRESH_TOKEN>`` &success_url= ``<URL_ENCODED_ACTION_URL>``

  .. role:: fg-red

  +------------------------+-----------------+
  | Query-Parameter        | Optional        |
  +========================+=================+
  | login_name             | :fg-green:`YES` |
  +------------------------+-----------------+
  | token                  | :fg-red:`NO`    |
  +------------------------+-----------------+
  | roles                  | :fg-red:`NO`    |
  +------------------------+-----------------+
  | refresh_token          | :fg-green:`YES` |
  +------------------------+-----------------+
  | success_url            | :fg-green:`YES` |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Perform entitlement logout
  :color: purple
  :versionadded-android: 2.6.0
  :versionadded-ios: 2.6.0
  :versionadded-web-kiosk: 3.2.0

  Performs the entitlement logout. If the logout was successful, the **url_encoded_action_url** will be opened.

  |

  **URL**

  purple://kiosk/entitlement/logout/perform?success_url= ``<URL_ENCODED_ACTION_URL>``

  .. role:: fg-red

  +------------------------+-----------------+
  | Query-Parameter        | Optional        |
  +========================+=================+
  | success_url            | :fg-green:`YES` |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. _deeplink-oauth-login:

.. versioned-toggle-box:: Start OAuth login flow
  :color: purple
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0

  Starts the entitlement OAuth login flow.
  If the login flow was successful completed, the **url_encoded_action_url** will be opened.

  |

  **URL**

  purple://kiosk/entitlement/login/oauth/start?success_url= ``<URL_ENCODED_ACTION_URL>``

  .. role:: fg-red

  +------------------------+-----------------+
  | Query-Parameter        | Optional        |
  +========================+=================+
  | success_url            | :fg-green:`YES` |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Cancel OAuth login flow
  :color: purple
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0

  Cancels the entitlement OAuth login flow.

  |

  **URL**

  purple://kiosk/entitlement/login/oauth/cancel

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Open subscription administration view
  :color: purple
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0

  Opens the subscription administration view with all activated subscription variants and depending on configuration including entitlements.

  .. TODO outsource declaration of subscription administration view in a feature docu

  |

  **URL**

  purple://kiosk/subscriptions/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Start In-App purchase
  :color: purple
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0

  Starts an In-App purchase of a product (issue/subscription) via its **product_id** property.

  |

  **URL**

  purple://kiosk/products/``<PRODUCT_ID>``/purchase

  .. role:: fg-red

  +------------------------+-----------------+
  | Parameter              | Optional        |
  +========================+=================+
  | PRODUCT_ID             | :fg-red:`NO`    |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-------------------------------------------+
  | Context                               | Usable                                    |
  +=======================================+===========================================+
  | App menu                              | :fg-green:`YES`                           |
  +---------------------------------------+-------------------------------------------+
  | Kiosk promotion area                  | :fg-green:`YES`                           |
  +---------------------------------------+-------------------------------------------+
  | Storytelling content                  | :fg-red:`NO` Android, :fg-green:`YES` ios |
  +---------------------------------------+-------------------------------------------+
  | Purple webview                        | :fg-green:`YES`                           |
  +---------------------------------------+-------------------------------------------+
  | Push notification Manager             | :fg-red:`NO`                              |
  +---------------------------------------+-------------------------------------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES`                           |
  +---------------------------------------+-------------------------------------------+
  | In-App Messages Braze                 | :fg-green:`YES`                           |
  +---------------------------------------+-------------------------------------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Restore purchases
  :color: purple
  :versionadded-ios: 2.7.0

  .. warning::

    This action url is not supported on Android.

  Restores all the purchases of the user.

  |

  **URL**

  purple://kiosk/products/restore

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Open issue
  :color: purple
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0
  :versionadded-web-kiosk: 3.2.0
  :versionadded-web-player: 3.0.0
  :versionchanged: 3.2.0 Add alias, add current page, 3.11.0 added open by index

  Opens an issue via its **issue_id**. If the action url is called with the **page_id** the page of the issue will be opened.
  It is also possible to provide the **issue_alias**, **page_alias** and **page_index** instead of their respective ids.

  |

  **URL**

  purple://kiosk/issue/:code:`<ISSUE>`/open

  +---------------------------------------------+-----------------------------------------------------------------------------------------------+
  | <ISSUE>                                     | Expected result                                                                               |
  +=============================================+===============================================================================================+
  | :code:`<ISSUE_ID>`                          | Opens the issue in the soft-bookmark state.                                                   |
  +---------------------------------------------+                                                                                               |
  | alias/:code:`<ISSUE_ALIAS>`                 |                                                                                               |
  +---------------------------------------------+-----------------------------------------------------------------------------------------------+
  | current                                     | Remains in the current state.                                                                 |
  |                                             |                                                                                               |
  | (or issue ID or alias of the current issue) |                                                                                               |
  +---------------------------------------------+-----------------------------------------------------------------------------------------------+

  |

  **URL**

  purple://kiosk/issue/:code:`<ISSUE>`/page/:code:`<PAGE>`/open

  +-----------------------------+-----------------------------+-----------------------------------------------------------------------------------------------+
  | <ISSUE>                     | <PAGE>                      | Expected result                                                                               |
  +=============================+=============================+===============================================================================================+
  | :code:`<ISSUE_ID>`          | :code:`<PAGE_ID>`           | Opens an issue via its issue ID on the specified page (page ID, page alias or page index).    |
  |                             +-----------------------------+                                                                                               |
  |                             | alias/:code:`<PAGE_ALIAS>`  |                                                                                               |
  |                             +-----------------------------+                                                                                               |
  |                             | index/:code:`<PAGE_INDEX>`  |                                                                                               |
  +-----------------------------+-----------------------------+-----------------------------------------------------------------------------------------------+
  | alias/:code:`<ISSUE_ALIAS>` | :code:`<PAGE_ID>`           | Opens an issue via its alias  on the specified page (page ID, page alias or page index).      |
  |                             +-----------------------------+                                                                                               |
  |                             | alias/:code:`<PAGE_ALIAS>`  |                                                                                               |
  |                             +-----------------------------+                                                                                               |
  |                             | index/:code:`<PAGE_INDEX>`  |                                                                                               |
  +-----------------------------+-----------------------------+-----------------------------------------------------------------------------------------------+
  | current                     | :code:`<PAGE_ID>`           | Opens the specified page of the current issue.                                                |
  |                             +-----------------------------+                                                                                               |
  | (or issue ID or alias       | alias/:code:`<PAGE_ALIAS>`  |                                                                                               |
  | of the current issue)       +-----------------------------+                                                                                               |
  |                             | index/:code:`<PAGE_INDEX>`  |                                                                                               |
  +-----------------------------+-----------------------------+-----------------------------------------------------------------------------------------------+
  | :code:`<ISSUE_ID>`          | current                     | Opens the issue on the first page.                                                            |
  +-----------------------------+                             |                                                                                               |
  | alias/:code:`<ISSUE_ALIAS>` |                             |                                                                                               |
  +-----------------------------+-----------------------------+-----------------------------------------------------------------------------------------------+
  | current                     | current                     | Remains in the current state.                                                                 |
  |                             |                             |                                                                                               |
  | (or issue ID or alias       | (or page ID, alias or index |                                                                                               |
  | of the current issue)       | of the current issue)       |                                                                                               |
  +-----------------------------+-----------------------------+-----------------------------------------------------------------------------------------------+

  |

  **Jump to element**

  |

  This is a special case of *open an issue*. It jumps to an issue, a page or an element.
  To jump to an element, the **element_id** or the **element_alias** must be specified as the fragment component of the url.

  The alignment of the element on the screen can be set with the parameter **align** by stating one of the following alignments:
  :code:`top_left`, :code:`top_center`, :code:`top_right`, :code:`center_left`, :code:`center_center`, :code:`center_right`, :code:`bottom_left`, :code:`bottom_center`, :code:`bottom_right`

  The alignment is a optional query parameter.

  |

  **URL**

  purple://kiosk/issue/:code:`<ISSUE>`/open# :code:`<ELEMENT>`

  purple://kiosk/issue/:code:`<ISSUE>`/open?align= :code:`<ALIGNMENT>` # :code:`<ELEMENT>`

  +-----------------------------+-------------------------+-----------------------------------------------------------------------------------------------+
  | <ISSUE>                     | <ELEMENT>               | Expected result                                                                               |
  +=============================+=========================+===============================================================================================+
  | :code:`<ISSUE_ID>`          | :code:`<ELEMENT_ID>`    | Opens the issue on the first page and jumps to the specified element if possible.             |
  +-----------------------------+-------------------------+                                                                                               |
  | alias/:code:`<ISSUE_ALIAS>` | :code:`<ELEMENT_ALIAS>` |                                                                                               |
  +-----------------------------+-------------------------+-----------------------------------------------------------------------------------------------+
  | current                     | :code:`<ELEMENT_ID>`    | Remains in the current state.                                                                 |
  |                             +-------------------------+                                                                                               |
  | (or issue ID or alias       | :code:`<ELEMENT_ALIAS>` |                                                                                               |
  | of the current issue)       |                         |                                                                                               |
  +-----------------------------+-------------------------+-----------------------------------------------------------------------------------------------+

  |

  **URL**

  purple://kiosk/issue/:code:`<ISSUE>`/page/:code:`<PAGE>`/open# :code:`<ELEMENT>`

  purple://kiosk/issue/:code:`<ISSUE>`/page/:code:`<PAGE>`/open?align= :code:`<ALIGNMENT>` # :code:`<ELEMENT>`

  +-----------------------------+----------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
  | <ISSUE>                     | <PAGE>                     | <ELEMENT>               | Expected result                                                                                    |
  +=============================+============================+=========================+====================================================================================================+
  | :code:`<ISSUE_ID>`          | :code:`<PAGE_ID>`          | :code:`<ELEMENT_ID>`    | Opens the issue on the specified page and jumps to the specified element if possible.              |
  +-----------------------------+----------------------------+-------------------------+                                                                                                    |
  | alias/:code:`<ISSUE_ALIAS>` | alias/:code:`<PAGE_ALIAS>` | :code:`<ELEMENT_ALIAS>` |                                                                                                    |
  +-----------------------------+----------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
  | current                     | :code:`<PAGE_ID>`          | :code:`<ELEMENT_ID>`    | Opens the specified page of the current issue and jumps to the specified element if possible.      |
  |                             +----------------------------+-------------------------+                                                                                                    |
  | (or issue ID or alias       | alias/:code:`<PAGE_ALIAS>` | :code:`<ELEMENT_ALIAS>` |                                                                                                    |
  | of the current issue)       |                            |                         |                                                                                                    |
  +-----------------------------+----------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
  | :code:`<ISSUE_ID>`          | current                    | :code:`<ELEMENT_ID>`    | Opens the issue on the first page and jumps to the specified element if possible.                  |
  +-----------------------------+                            +-------------------------+                                                                                                    |
  | alias/:code:`<ISSUE_ALIAS>` |                            | :code:`<ELEMENT_ALIAS>` |                                                                                                    |
  +-----------------------------+----------------------------+-------------------------+----------------------------------------------------------------------------------------------------+
  | current                     | current                    | :code:`<ELEMENT_ID>`    | Jumps to the specified element on the current page of the current issue.                           |
  |                             |                            +-------------------------+                                                                                                    |
  | (or issue ID or alias       | (or page ID or alias       | :code:`<ELEMENT_ALIAS>` |                                                                                                    |
  | of the current issue)       | of the current issue)      |                         |                                                                                                    |
  +-----------------------------+----------------------------+-------------------------+----------------------------------------------------------------------------------------------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+


.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Open issue via its external identifier
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0
  :versionadded-web-kiosk: 3.2.0
  :versionadded-web-player: 3.0.0

  It is possible to open an issue via its **external_issue_id** property. If the issue cannot be found in the current local kiosk, the optional **fallback_url**
  can be used to provide an alternative web link for the issue, e.g. the website of an article in the CMS.

  |

  **URL**

  purple://kiosk/issue/by_external_id/``<EXTERNAL_ISSUE_ID>``/open?fallback_url= ``<URL_ENCODED_URL>`` &target= ``<TARGET>``

  .. role:: fg-red
  .. role:: fg-green

  +------------------------+-----------------+
  | Parameter              | Optional        |
  +========================+=================+
  | EXTERNAL_ISSUE_ID      | :fg-red:`NO`    |
  +------------------------+-----------------+

  |

  +-----------------+---------------+-------------------------------------------------------------------------------------------------------------+
  | Query Parameter | Optional      | Description                                                                                                 |
  +=================+===============+=============================================================================================================+
  | fallback_url    | :fg-red:`YES` | The url which should be opened if no issue with the external issue ID can be found.                         |
  +-----------------+---------------+-------------------------------------------------------------------------------------------------------------+
  | target          | :fg-red:`YES` | The target for the fallback_url. Can be "_blank" for external window, or empty / omitted for inapp browser. |
  +-----------------+---------------+-------------------------------------------------------------------------------------------------------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Open publication
  :color: purple
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-kiosk: 3.4.0

  Opens the given publication. A kiosk-publication will be opened in the kiosk and a channel-publication in the channel
  view. If the target view is disabled, e.g. channel disabled, or if there is no publication with the given
  **publication_id** then no navigation will be performed.

  |

  **URL**

  purple://kiosk/publication/:code:`<PUBLICATION_ID>`/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

Presenter
#########

.. versioned-toggle-box:: Navigate between articles
  :color: dark-purple
  :versionadded-android: 3.15.0
  :versionadded-ios: 3.15.0
  :versionchanged: 5.2.0 now accepts an issue ID instead of the :code:`previous` and :code:`next` keywords.

  Navigates to the given issue within the current article pager.
  Instead of using an issue ID it is possible to use :code:`previous` and :code:`next` to navigate to the previous or next issue.

  |

  **URL**

  purple://presenter/issue/:code:`<ISSUE_ID>|previous|next`

  |

  .. note:: These deep links only work within an article pager that was opened via the JavaScript-API. And only articles within this pager can be accessed.

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

Content
#######

.. versioned-toggle-box:: Open table of contents
  :color: green
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0
  :versionadded-web-player: 3.0.0

  Opens the table of contents of an issue.

  |

  **URL**

  purple://content/toc/open

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Navigate inside an issue via alias
  :color: green
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0
  :versionadded-web-player: 3.0.0

  Navigates inside an issue to the corresponding page via **alias**.

  |

  **URL**

  purple://content/page/alias/``<ALIAS>``/open

  .. role:: fg-red

  +------------------------+-----------------+
  | Parameter              | Optional        |
  +========================+=================+
  | ALIAS                  | :fg-red:`NO`    |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Navigate inside an issue via index
  :color: green
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0
  :versionadded-web-player: 3.0.0

  Navigates inside an issue to the corresponding page via **index**.

  |

  **URL**

  purple://content/page/index/``<INDEX>``/open

  .. role:: fg-red

  +------------------------+-----------------+
  | Parameter              | Optional        |
  +========================+=================+
  | INDEX                  | :fg-red:`NO`    |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Navigate inside an issue via page ID
  :color: green
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :versionadded-web-player: 3.11.0

  Navigates inside an issue to the corresponding page via its **ID**.

  |

  **URL**

  purple://content/page/``<PAGE_ID>``/open

  .. role:: fg-red

  +------------------------+-----------------+
  | Parameter              | Optional        |
  +========================+=================+
  | PAGE_ID                | :fg-red:`NO`    |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Share content page
  :color: green
  :versionadded-android: 2.7.0
  :versionadded-ios: 2.7.0

  Shares a content page of an issue via its **alias**.

  |

  **URL**

  purple://content/page/alias/``<ALIAS>``/share

  .. role:: fg-red

  +------------------------+-----------------+
  | Parameter              | Optional        |
  +========================+=================+
  | ALIAS                  | :fg-red:`NO`    |
  +------------------------+-----------------+

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

.. raw:: pdf

   PageBreak

.. versioned-toggle-box:: Add bookmark
  :color: green
  :versionadded-android: 3.3.0
  :versionadded-ios: 3.3.0
  :not-available-for: web

  Adds a bookmark of the current state of the storytelling content.
  If there is already a bookmark for the exact same state then no new bookmark will added.

  |

  **URL**

  purple://content/bookmark/add

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-red:`NO`    |
  +---------------------------------------+-----------------+

|

.. raw:: pdf

   PageBreak

Old action urls
###############

.. container:: custom-table

  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Title                                 | Action url                                                                              | Version Android  | Version iOS      | Version Web                   |
  +=======================================+=========================================================================================+==================+==================+===============================+
  | Open app information                  | pkapp://action/openAppInformation                                                       | - 1.6.0          | 2.1.0            | not supported                 |
  |                                       |                                                                                         | - 2.1.0 (Braze)  |                  |                               |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open app settings                     | pkapp://action/openSettings                                                             | 2.1.0            | n/a              | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open bookmarks view                   | pkapp://action/openBookmarks                                                            | 2.1.0            | 2.1.0            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open composer connect                 | pkapp://action/openComposerConnect                                                      | 2.1.0            | 2.1.0            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open manager connect                  | pkapp://action/openPurpleManagerConnect                                                 | 2.1.0            | n/a              | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open feedback mail                    | pkapp://action/openFeedback                                                             | 2.1.0            | 1.7.x            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Show dynamic html content             | pkapp://action/showDynamicContent/``<PATH>``                                            | 2.7.0            | 1.7.x            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Share app or issue or page            | purple://app/share_app_or_issue_or_content                                              | 2.2.0            | 2.7.0            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open kiosk (newsstand)                | pkapp://action/openKiosk                                                                | - 1.6.x          | - 1.x            | not supported                 |
  |                                       |                                                                                         | - 2.1.0 (Braze)  | - 2.1.0 (Braze)  |                               |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open channel (newsfeed)               | pkapp://action/openChannelFeed                                                          | 2.2.x            | 2.1.0            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open category chooser                 | pkapp://action/changeKioskCategory                                                      | 2.1.0            | 2.3.3            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Show issue preview                    | pkapp://action/openIssueDetailByID/``<ISSUE_ID>``                                       | - 1.6.x          | 2.7.0            | not supported                 |
  |                                       |                                                                                         | - 2.1.0 (Braze)  |                  |                               |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open subscription administration view | pkapp://action/openSubscriptions                                                        | - 1.6.x          | - 1.x            | not supported                 |
  |                                       |                                                                                         | - 2.1.0 (Braze)  | - 2.1.0 (Braze)  |                               |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Start In-App purchase                 | pkapp://action/purchase/``<PRODUCT_ID>``                                                | 2.1.0            | 2.1.0            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Restore purchases                     | pkapp://action/restorePurchases                                                         | not supported    | 1.x              | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open issue                            | pkapp://action/openIssueByID/``<ISSUE_ID>``                                             | - 1.6.x          | - 2.7.0          | not supported                 |
  |                                       |                                                                                         | - 2.1.0 (Braze)  | - 2.1.0 (Braze)  |                               |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | ( Open current issue )                | pkapp://action/presentCurrentIssue                                                      | 2.1.0            | 2.1.0            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | ( Jump to element )                   | pkitem://purple/``<ISSUE_ID>``/``<PAGE_ID>``?align\= ``<ALIGNMENT>`` # ``<ELEMENT_ID>`` | 2.1.0            | 2.7.0            | 2.0.0                         |
  |                                       |                                                                                         |                  |                  | (inside current issue only)   |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Open table of contents                | pkapp://action/openTOC                                                                  | 1.6.x            | 1.x              | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Navigate inside an issue via alias    | pkapp://navigate/alias/``<ALIAS>``                                                      | 1.6.x            | 2.7.0            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Navigate inside an issue via index    | pkapp://navigate/index/``<INDEX>``                                                      | 1.6.x            | 2.7.0            | not supported                 |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+
  | Share content page                    | pkapp://action/shareContentPage/``<ALIAS>``                                             | 2.2.0            | 2.1.0            | not supported                 |
  |                                       | pkapp://action/shareContentPage/``.``                                                   |                  |                  |                               |
  +---------------------------------------+-----------------------------------------------------------------------------------------+------------------+------------------+-------------------------------+

|

|

.. raw:: pdf

   PageBreak

Web Player specifics
####################
External links do not work out of the box in Web Player because Safari, Edge, and Internet Explorer do not support the needed function ( http://caniuse.com/#feat=registerprotocolhandler ).

Due to WebViews being implemented using iframes in Web Player, Action URLs from inside Storytelling WebViews
only work if :code:`purpleInterface.js` is included in the embedded page.
When the WebView is loaded, all links with Purple Action URLs as href will be given ActionHandlers, so they can be handled by Web Player.

From V 3.0.0 :code:`purpleInterface.js` is included in the Web Player repository.
The latest version is delivered via Purple DS | Web Newsstand.
It is recommended to include the script from one of the following URLs to assure to always use the latest version:
https://kiosk.purplemanager.com/scripts/purpleInterface.js
https://kiosk.purplemanager.com/scripts/purpleInterface.min.js

.. note::

  Please be aware that only sites can be displayed which have the :code:`X-FRAME-OPTIONS` header set correctly.
  Read here for details: https://developer.mozilla.org/en/docs/Web/HTTP/Headers/X-Frame-Options

.. toggle-box:: purpleInterface.js (excerpt)

  .. code-block:: javascript

    window.purpleInterface = {
    callbacks: {},
    util: {
        postMessage: function (type, key, value, callback) {

            if (window !== window.parent) {

                // create requestData
                var requestData = {
                    type: type,
                    key: key
                };
                if (value) {
                    requestData.value = value;
                }

                // call postMessage
                window.parent.postMessage(JSON.stringify(requestData), '*');
            }

        }
      }
    };

    document.addEventListener('DOMContentLoaded', function () {
        window.addEventListener('message', window.purpleInterface.util.receiveMessage);

        window.purpleInterface.util.postMessage('LOAD', 'LOAD', null, function () {

            if (!window.purple) {
                var links = document.querySelectorAll('a[href^="purple://"], a[ ^="pkapp://"], a[href^="pkitem://"]');
                for (var i = 0; i < links.length; i++) {
                    links[i].addEventListener('click', function (e) {
                        window.purpleInterface.util.postMessage('ACTION_URL', 1, this.href);
                        e.preventDefault();
                    });
                }
            }

        });
    });


|

|

Standard Protocols
##################

.. versioned-toggle-box:: Mailto
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-player: 3.1.0

  Starts the default email client for sending an email.

  |

  **URL**

  mailto::code:`<EMAIL_ADDRESS>`

  mailto:?to= :code:`<EMAIL_ADDRESS>` &bcc= :code:`<EMAIL_ADDRESS>` &subject= :code:`<SUBJECT>` &body= :code:`<BODY>`

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+

.. versioned-toggle-box:: Tel
  :color: blue
  :versionadded-android: 3.2.0
  :versionadded-ios: 3.2.0
  :versionadded-web-player: 3.1.0

  Starts the default phone app for a call.

  |

  **URL**

  tel::code:`<PHONE_NUMBER>`

  |

  **Usable Contexts**

  .. role:: fg-green
  .. role:: fg-red

  +---------------------------------------+-----------------+
  | Context                               | Usable          |
  +=======================================+=================+
  | App menu                              | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Kiosk promotion area                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Storytelling content                  | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Purple webview                        | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | Push notification Manager             | :fg-red:`NO`    |
  +---------------------------------------+-----------------+
  | Push notifications Braze / Pinpoint   | :fg-green:`YES` |
  +---------------------------------------+-----------------+
  | In-App Messages Braze                 | :fg-green:`YES` |
  +---------------------------------------+-----------------+
