########
Webviews
########

.. toctree::

.. _webviews-js-api:

General
#######

Support for window.print
************************

.. versionadded:: 3.7.0

Apps support the :code:`window.print` JavaScript-API.
The standard system print dialog is opened if :code:`window.print` is called.

Support for window.open
************************

Apps support the :code:`window.open` JavaScript-API. Starting with 3.11 links
opened via this API will be opened in the internal App Browser (with title bar, status bar and navigation, as a "new window")
or the same webview, according to the standard browser specifications.

Starting with version 3.10 Action URLs can also be opened via this API on all platforms.

JavaScript-Interfaces
#####################

Using the Purple JavaScript-API
*******************************

Web content can access special JavaScript-APIs to get information about
the app / issue and trigger actions.

There are two ways to access the JavaScript-APIs: **automatic** and **manual** inclusion.

Automatic inclusion (deprecated since 3.9)
==========================================

.. versionchanged:: 3.9.0 Deprecated, replaced with manual inclusion

With automatic inclusion you simply need to have a global :code:`onPurpleLoad`
function which will get called after the APIs have been made available.

**This however only works on Android and iOS and is not supported in the Web Kiosk.
This method is therefore considered deprecated since Purple Release 3.9 with the
support of manual inclusion.**

Manual inclusion
================

.. versionadded:: 3.9.0

To manually include the JS-APIs html consumers can add any source ending on :code:`scripts/purpleInterface.js` or :code:`scripts/purpleInterface.min.js`
to their head element.
The web view intercepts this request and returns the :code:`purpleInterface.js`.
It is recommended to use the following URL to assure the API works on all platforms
including web.

.. code-block:: html
  :linenos:
  :caption: Example HTML

  <html>
    <head>
        <script type="text/javascript" src="https://kiosk.purplemanager.com/scripts/purpleInterface.min.js"></script>
    </head>
    <body></body>
  </html>

.. note:: The old automatic injection mechanism is used as fallback strategy.

When manually embedding the purpleInterface.js source, the use of the :code:`onPurpleLoad` function is not mandatory.
The purple-Object is available instantly after loading the script.

.. hint:: If the onPurpleLoad function is used anyways, it needs to be defined prior to the above script tag.

.. code-block:: html
  :caption: Example HTML
  :name: index.html

  <html>
    <head>
        <script type="text/javascript">
            function onPurpleLoad() {
                // the global "purple" object is now available
            }
        </script>
        <script type="text/javascript" src="https://kiosk.purplemanager.com/scripts/purpleInterface.min.js"></script>
    </head>
    <body></body>
  </html>

.. code-block:: javascript
  :caption: Overview of the JavaScript-Interfaces

  window.purple = {
      app: {
          ...
      },
      metadata: {
          ...
      },
      storefront: {
          ...
      },
      store: {
          ...
      },
      issue: {
          ...
      },
      state: {
          ...
      }
  }

App
***

This interface is for app-wide information such as the device's connectivity state.

.. note:: This interface is not available in Web Kiosk.

.. code-block:: javascript
  :caption: App JavaScript-Interface

  window.purple = {
      /**
       * @public
       * @static
       * @namespace AppController
       */
      app: {
          /**
           * Adds a listener for connection state changes.
           * The listener will be called with a ConnectionState object.
           * This listener will also be called with the current state right after
           * calling this method.
           */
          addConnectionStateListener: function (listener) {
              // Implementation
          },
          /**
           * Removes a listener for connection state changes.
           */
          removeConnectionStateListener: function (listener) {
              // Implementation
          },
          /**
           * Adds a listener for lifecycle changes.
           * The listener will be called with a LifecycleEvent object.
           * This listener will also be called with the current state right after
           * calling this method.
           */
          addLifecycleListener: function (listener) {
              // Implementation
          },
          /**
           * Removes a listener for lifecycle changes.
           */
          removeLifecycleListener: function (listener) {
              // Implementation
          },
          /**
           * Close the onboarding screen. If true is passed as the first parameter
           * the onboarding will be shown again on the next app start.
           */
          closeOnboarding: function (showAgain) {
              // Implementation
          }
      }
  }

.. versioned-toggle-box:: addConnectionStateListener
  :color: blue
  :versionadded-android: 3.3.0
  :versionadded-ios: 3.4.0

  The :code:`addConnectionStateListener` method can be used to register a callback function that gets called when the device changes its connection state.
  The listener will also be called with the current state when this method is called.

  This method takes a single parameter: A callback function that gets called with one parameter, a json object.

  This json object will consist of a :code:`state` with the value :code:`ONLINE` and :code:`type` of either :code:`TYPE_3G` during mobile connectivity or :code:`TYPE_WLAN` when it is connected to wi-fi.

  .. code-block:: javascript

    {
      "state": "ONLINE",
      "type": "TYPE_3G|TYPE_WLAN"
    }

  If the device is offline then there will be only a :code:`state` with the value :code:`OFFLINE`.

  .. code-block:: javascript

    {
      "state": "OFFLINE"
    }

.. versioned-toggle-box:: removeConnectionStateListener
  :color: blue
  :versionadded-android: 3.3.0
  :versionadded-ios: 3.4.0

  This method removes the listener that was added with :code:`addConnectionStateListener` to stop receiving callbacks.

.. versioned-toggle-box:: addLifecycleListener
  :color: blue
  :versionadded-android: 3.10.2
  :versionadded-ios: 3.10.2

  The :code:`addLifecycleListener` method can be used to register a callback function that gets called when the webview or the device changes its lifecycle state.
  The listener will also be called with the current state when this method is called.

  This method takes a single parameter: A callback function that gets called with one parameter of type object.

  This object will consist of a :code:`type` with the following values

  * :code:`STARTED` if the webview appears
  * :code:`RESUMED` if the webview is visible and gets focus
  * :code:`PAUSED` if the webview is visible but loses focus
  * :code:`STOPPED` if the webview disappears

  When the app comes to foreground or background and the webview is presented, the callback will also be called with the specific :code:`type`.

  .. code-block:: javascript
    :linenos:

    {
      "type": "STARTED|RESUMED|PAUSED|STOPPED"
    }

.. versioned-toggle-box:: removeLifecycleListener
  :color: blue
  :versionadded-android: 3.10.2
  :versionadded-ios: 3.10.2

  This method removes the listener that was added with :code:`addLifecycleListener` to stop receiving callbacks.

.. _webviews_app_closeonboarding:

.. versioned-toggle-box:: closeOnboarding
  :color: blue
  :versionadded-android: 3.10.0
  :versionadded-ios: 3.10.0

  Close the onboarding screen. If true is passed as the first parameter the
  onboarding will be shown again on the next app start.

  This API method is only available on the onboarding screen.

  See the :doc:`onboarding documentation </apps/onboarding>` for more information about this feature.

App-Browser
***********

This interface can be used to retrieve information about the configuration of the
current webview, e.g. if it's displayed modally or embedded, has titlebar and controls.

.. code-block:: javascript
  :linenos:
  :caption: App-Browser JavaScript-Interface

  window.purple = {
     appBrowser: {
        getDisplayMode: function (callback) {
            // Impl
        },
        isTitleBarEnabled: function (callback) {
            // Impl
        },
        isControlsEnabled: function (callback) {
            // Impl
        },
        isStatusBarEnabled: function (callback) {
            // Impl
        }
     }
  }

.. versioned-toggle-box:: getDisplayMode
  :color: blue
  :versionadded-android: 3.5.0
  :versionadded-ios: 3.5.0
  :versionadded-web-player: 3.5.0
  :versionadded-web-kiosk: 3.7.0

  Get the display mode for the current webview.

  This method has one parameter, a callback function which will get the display
  mode value in as a single string parameter.

  Values can be :code:`embedded` or :code:`modal`.

.. versioned-toggle-box:: isTitleBarEnabled
  :color: blue
  :versionadded-android: 3.5.0
  :versionadded-ios: 3.5.0
  :versionadded-web-player: 3.5.0
  :versionadded-web-kiosk: 3.7.0

  Get the titlebar configuration for the current webview.

  This method has one parameter, a callback function which will get a boolean
  value in as a single parameter.

.. versioned-toggle-box:: isControlsEnabled
  :color: blue
  :versionadded-android: 3.5.0
  :versionadded-ios: 3.5.0
  :versionadded-web-player: 3.5.0
  :versionadded-web-kiosk: 3.7.0

  Get the controls configuration for the current webview.

  This method has one parameter, a callback function which will get a boolean
  value in as a single parameter.

.. versioned-toggle-box:: isStatusBarEnabled
  :color: blue
  :versionadded-android: 3.10.0
  :versionadded-ios: 3.10.0
  :versionadded-web-player: 3.10.0
  :versionadded-web-kiosk: 3.10.0

  Get the statusbar configuration for the current webview.

  This method has one parameter, a callback function which will get a boolean
  value in as a single parameter.

Metadata
********

Metadata / information about the app and issue can be accessed through this javascript interface.

.. code-block:: javascript
  :caption: Metadata JavaScript-Interface

  window.purple = {
      /**
       * @public
       * @static
       * @namespace MetaDataController
       */
      metadata: {
          /**
           * Get metadata values by key.
           *
           * @param {string} key          the metadata key
           * @param {string} callback     the callback for the value
           */
          getMetadata: function (key, callback) {
              // Implementation
          }
      }
  }

.. versioned-toggle-box:: getMetadata
  :color: blue
  :versionadded-android: 2.4.0
  :versionadded-ios: 2.6.0
  :versionadded-web-player: 2.6.0
  :versionadded-web-kiosk: 3.7.0

  This method returns the value for a given key. The value will be provided via the `callback` method.

  The following keys are available:

  |

  .. versioned-toggle-box:: app_id
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionchanged: 2.6.0 now globally available in all web views
    :versionadded-web-player: 2.6.0
    :versionadded-web-kiosk: 3.7.0

    The id of the app in the Purple Manager.

    On macOS this always returns "Preview Publication".

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: app_version
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0
    :versionadded-composer: 3.1.0

    The version of the app.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: preview_app
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0
    :versionadded-web-kiosk: 3.7.0

    Boolean value indicating if the app is a preview or release app.

    On macOS this always returns :code:`true`.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: device_id
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0

    The unique id of the device. Used for communication with the Purple Manager.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: device_model
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0
    :versionadded-composer: 3.1.0

    The model of the device.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: device_os
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0
    :versionadded-web-kiosk: 3.7.0

    The os version of the device.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: platform
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0
    :versionadded-web-kiosk: 3.7.0

    The platform (``android``, ``kindle``, ``ios``, ``web` or ``macOS``) on which this app is running on.

    |

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content


  .. versioned-toggle-box:: locale
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0
    :versionadded-web-kiosk: 3.7.0

    The current locale of the system.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: manager_base_url
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0
    :versionadded-web-player: 2.6.0
    :versionadded-web-kiosk: 3.7.0

    The base url for communicating with the delivery service of the Purple Manager.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: push_registration_token
    :color: blue
    :versionadded-android: 3.0.0
    :versionadded-ios: 3.0.0

    The push registration token. This can be used to send pushes to the app.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content


  .. versioned-toggle-box:: entitlement_login
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionchanged: 2.6.0 now globally available in all web views
    :versionadded-web-player: 2.6.0
    :versionadded-web-kiosk: 3.7.0

    |

    The entitlement username of the user if he is logged in.

    **Available contexts**

    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content


  .. versioned-toggle-box:: entitlement_token
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionchanged: 2.6.0 now globally available in all web views
    :versionadded-web-player: 2.6.0
    :versionadded-web-kiosk: 3.7.0

    The entitlement access token of the user if he is logged in.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: entitlement_forced_login_enabled
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0

    The configuration parameter for forced entitlement login on app start.

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: entitlement_login_mode
    :color: blue
    :versionadded-android: 2.6.0
    :versionadded-ios: 2.6.0

    Can be either ``login`` or ``relogin`` indicating the current mode / reason why the login screen has been opened. ``relogin`` will be returned
    if the server responded with an error that the access token is invalid during subscription validation.

    **Available contexts**

    * Html-Entitlement Login

  .. versioned-toggle-box:: issue_id
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The id of the currently viewed issue.

    **Available contexts**

    * Storytelling Content

  .. versioned-toggle-box:: issue_name
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The name of the currently viewed issue.

    On macOS this always returns "Preview Publication".

    **Available contexts**

    * Storytelling Content

  .. versioned-toggle-box:: publication_id
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The id of the publication of the currently viewed issue.

    On macOS this always returns "Preview Publication".

    **Available contexts**

    * Storytelling Content

  .. versioned-toggle-box:: publication_name
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The name of the publication of the currently viewed issue.

    On macOS this always returns "Preview Publication".

    **Available contexts**

    * Storytelling Content

  .. versioned-toggle-box:: page_id
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The id of the currently viewed content page.

    **Available contexts**

    * Storytelling Content

  .. versioned-toggle-box:: page_alias
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0

    The alias of the currently viewed content page.

    **Available contexts**

    * Storytelling Content


  .. versioned-toggle-box:: page_title
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The title of the currently viewed content page.

    **Available contexts**

    * Storytelling Content

  .. versioned-toggle-box:: page_index
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The index of the currently viewed content page.

    **Available contexts**

    * Storytelling Content

  .. versioned-toggle-box:: page_filename
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The filename of the current page (not the webview page, but the storytelling content page)

    **Available contexts**

    * Storytelling Content

  .. versioned-toggle-box:: onboarding_mode
    :color: blue
    :versionadded-android: 3.10.1
    :versionadded-ios: 3.10.1

    The mode for the onboarding screen. Can be :code:`appstart` when opened
    during app start or :code:`manual` when opened via action url.

    |

    **Available contexts**

    * HTML onboarding screen

Storefront
**********

Web content can access storefront data through a javascript interface.

.. note:: This interface is not available in Composer Native Preview.

.. code-block:: javascript
  :caption: Storefront JavaScript-Interface

  window.purple = {
      /**
       * @public
       * @static
       * @namespace StorefrontController
       */
      storefront: {
          /**
           * Get subscriptions.
           *
           * @param {Function} callback     the callback for the subscriptions
           */
          getSubscriptions: function (callback) {
              // Implementation
          },
          /**
           * Gets a list of all publications. Callback will be called with a
           *  JSONArray of Publication objects.
           */
          getPublications: function (callback) {
              // Implementation
          },
          /**
           * Gets a list of all issues for the publication with the given
           * publicationId. Callback will be called with a JSONArray of Issue
           * objects.
           */
          getIssues: function (publicationId, callback) {
              // Implementation
          },
          /**
           * Gets a list of all issue states for the given issueIds. Callback
           * will be called with a JSONArray of IssueState objects without a
           * progress value.
           */
          getIssueStates: function (issueIds, callback) {
              // Implementation
          },
          /**
           * Starts the download of the issue with the given issueId.
           * This can also be a preview issue.
           */
          startDownload: function (issueId) {
              // Implementation
          },
          /**
           * Pauses the download of the issue with the given issueId.
           * This can also be a preview issue.
           */
          pauseDownload: function (issueId) {
              // Implementation
          },
          /**
           * Deletes the content of the issue with the given issueId.
           * This includes the preview content and temporary downloaded data.
           * The callback will be called with the current IssueState object.
           */
          deleteIssue: function (issueId, callback) {
              // Implementation
          },
          /**
           * Adds a listener for issue state changes.
           * The listener will be called with an IssueState object with a
           * progress value.
           */
          addIssueStateListener: function (listener) {
              // Implementation
          },
          /**
           * Removes a listener for issue state changes.
           */
          removeIssueStateListener: function (listener) {
              // Implementation
          },
          /**
           * Loads the new storefront.
           * The callback will be called with the StorefrontUpdateResult object.
           */
          updateStorefront: function (callback) {
              // Implementation
          },
          /**
           * Adds a listener for newsstand and newsfeed changes.
           */
          addUpdateListener: function (listener) {
              // Implementation
          },
          /**
           * Removes a listener for newsstand and newsfeed changes.
           */
          removeUpdateListener: function (listener) {
              // Implementation
          }
      }
  }

.. versioned-toggle-box:: getSubscriptions
  :versionadded-android: 3.0.0
  :versionadded-ios: 3.0.0
  :versionchanged: 3.4.0 moved from :code:`kiosk` to :code:`storefront` API. The method in the :code:`kiosk` is still available but deprecated.
  :color: purple

  Subscriptions can be accessed through the :code:`getSubscriptions` method.
  It takes one parameter, a callback function, which is called with an array of
  subscriptions.

  |

  .. code-block:: javascript
    :caption: Subscription model

    {
      "name": "One Month Subscription",
      "productId": "com.sprylab.onemonth",
      "duration": "one_month",
      "hidden": false,
      "unlocksAllContentDuringPeriod": true,
      "index": 1,
      "publicationIds": ["aabbcc", "1233456"],
      "formattedPrice": "13.37€",
      "price": 13.37,
      "currency": "EUR",
      "properties": [
          {
              "name": "testproperty",
              "value": "testvalue"
          }
      ],
      "state": "NONE|PURCHASING|VALIDATING|PURCHASED"
    }

.. versioned-toggle-box:: getPublications
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-kiosk: 3.7.0
  :color: purple

  This method lists all publications in the storefront.
  It takes one parameter, a callback function, which is called with an array of publications.

  |

  .. code-block:: javascript
    :caption: Publications model

    {
      "publicationId": "aabbcc",
      "displayName": "Publication A",
      "displayDescription": "Fancy publication description",
      "properties": [
        {
          "name": "testproperty",
          "value": "testvalue"
        }
      ],
      "index": 0,
      "type": "KIOSK|CHANNEL",
      "thumbnails": {
        "default": "url",
        "kind1": "url"
      }
    }

.. versioned-toggle-box:: getIssues
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-kiosk: 3.7.0
  :color: purple

  This method needs to be called to obtain a list of issues for a specific publication.
  It takes two parameters: A :code:`publicationId` and a callback function which then will be called with an array of issues.
  The :code:`publicationId` can be acquired from a publication model that is obtained through the getPublications method.

  |

  .. code-block:: javascript
    :caption: Issue model

    {
      "issueId": "aabbcc",
      "displayName": "Issue A",
      "displayDescription": "Fancy issue description",
      "properties": [
        {
          "name": "testproperty",
          "value": "testvalue"
        }
      ],
      "index": 0,
      "pubDate": 123,
      "contentLength": 1337,
      "numberOfPages": 42,
      "comingSoon": true,
      "previewIssue": {
        "id": "ddeeff",
        "contentLength": 1337,
        "numberOfPages": 42
      }
      "productId": "com.sprylab.issue1",
      "thumbnails": {
        "default": "url",
        "kind1": "url"
      }
    }

  The :code:`pubDate` is a UNIX timestamp in ms.
  If the issue has a preview issue then :code:`previewIssue` is a jsonObject with the preview issue's id, its content size and the number of pages otherwise it is :code:`null`.
  The :code:`productId` can be used to purchase the issue through the :code:`store` api. It can be :code:`null` if the issue is not purchasable through in app payments.

.. versioned-toggle-box:: getIssueStates
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-kiosk: 3.7.0
  :color: purple

  To obtain the state of specific issues this method can be used.
  It takes two parameters. The first is an array of issue ids and the second a callback function which returns an array of issue state objects for the requested issue ids.

  |

  .. code-block:: javascript
    :caption: Issue state model

    {
      "issueId": "aabbcc",
      "state": "<STATE>"
    }

  The following table describes the possible issue states.

    +------------------+-------------------------------------------------------------------------------------+
    | State            | Description                                                                         |
    +==================+=====================================================================================+
    | LOCKED           | locked through entitlement -> not visible for the user                              |
    +------------------+-------------------------------------------------------------------------------------+
    | COMING_SOON      | coming soon enabled -> visible, but not downloadable                                |
    +------------------+-------------------------------------------------------------------------------------+
    | PURCHASABLE      | not purchased                                                                       |
    +------------------+-------------------------------------------------------------------------------------+
    | AVAILABLE        | download possible -> purchased, or no paid content                                  |
    +------------------+-------------------------------------------------------------------------------------+
    | DOWNLOAD_PAUSED  | download started and paused                                                         |
    +------------------+-------------------------------------------------------------------------------------+
    | DOWNLOADING      | downloading                                                                         |
    +------------------+-------------------------------------------------------------------------------------+
    | INSTALLING       | extracting, post processing                                                         |
    +------------------+-------------------------------------------------------------------------------------+
    | INSTALLED        | downloaded, extracted, available for reading                                        |
    +------------------+-------------------------------------------------------------------------------------+
    | UPDATE           | downloaded and new version available (=local version does not match remote version) |
    +------------------+-------------------------------------------------------------------------------------+


.. versioned-toggle-box:: startDownload
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :color: purple

  With this method it is possible to start the download of an issue with the given :code:`issueId`.


.. versioned-toggle-box:: pauseDownload
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :color: purple

  With this method it is possible to pause the download of the issue with the given :code:`issueId`.


.. versioned-toggle-box:: deleteIssue
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :color: purple

  This method allows the deletion of an issue. It takes two parameters. The first is the :code:`issueId` of the issue that will be removed and the other is a callback function that will be called with an issue state object after the delete process completed.


.. versioned-toggle-box:: addIssueStateListener
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :color: purple

  The :code:`addIssueStateListener` method allows the registration of a listener that will be called each time when the state of an issue changes.
  This method takes a single parameter which is a callback function. It will be called with issue state objects which contain an additional :code:`progress` value.
  This :code:`progress` can be a value between 0 and 100. It is always 0 except for the :code:`DOWNLOADING` and :code:`INSTALLING` state.
  The progress for the :code:`INSTALLING` state is currently only implemented in Android apps.
  For a description of the states see the table in :code:`getIssueStates`.

  |

  .. code-block:: javascript
    :caption: Issue state model (with progress, for possible states see getIssueStates)

    {
      "issueId": "aabbcc",
      "state": "<STATE>",
      "progress": 0
    }

.. versioned-toggle-box:: removeIssueStateListener
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :color: purple

  This method removes a listener that was set with :code:`addIssueStateListener` to stop receiving issue state updates.


.. versioned-toggle-box:: updateStorefront
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-kiosk: 3.7.0
  :color: purple

  This method starts a synchronization of the storefront with the Purple Manager. The result of this process will then be called on the given callback function.

  For a successful synchronization it will be a simple json object:

  .. code-block:: javascript

    {
      "success": true
    }

  For failures it will be json object which may contain an error code:

  .. code-block:: javascript

    {
      "success": false,
      "error_code": "[OFFLINE|UNKNOWN]"
    }

.. versioned-toggle-box:: addUpdateListener
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: purple

  The :code:`addUpdateListener` method allows the registration of a listener that will be called each time the kiosk has been updated.
  This method takes a single parameter which is a callback function which itself takes no parameters.

.. versioned-toggle-box:: removeUpdateListener
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: purple

  This method removes a listener that was previously added with :code:`addUpdateListener` to stop receiving kiosk updates.

Store
*****

It is also possible to start purchases and manage the subscription codes
through a javascript interface.

.. note:: This interface is not available in Web Kiosk and Composer Native Preview.

.. code-block:: javascript
  :caption: Store JavaScript-Interface

    window.purple = {
        /**
         * @public
         * @static
         * @namespace StoreController
         */
        store: {
            /**
             * Purchase a product
             *
             * @param {string} productId
             * @param {Function} callback
             */
            purchase: function (productId, callback) {
                // Implementation
            },
            /**
             * Subscribe to a subscription
             *
             * @param {string} productId
             * @param {Function} callback
             */
            subscribe: function (productId, callback) {
                // Implementation
            },
            /**
             * Restores purchases on device. Only available on iOS
             * (Android will call callback immediately).
             *
             * @param {Function} callback
             */
            restorePurchases: function (callback) {
                // Implementation
            },
            /**
             * Set a function as a listener which should be called when
             * the purchase state of a subscription product did change.
             * @param {Function} listener
             */
            setPurchaseStateListener: function (listener) {
                // Implementation
            },
            /**
             * Get the current subscription codes
             *
             * @param {Function} callback
             */
            getSubscriptionCodes: function (callback) {
                // Implementation
            },
            /**
             * Add subscription codes
             *
             * @param {String[]} codes
             * @param {Function} callback
             */
            addSubscriptionCodes: function (codes, callback) {
                // Implementation
            },
            /**
             * Remove the subscription codes
             *
             * @param {String[]} codes
             * @param {Function} callback
             */
            removeSubscriptionCodes: function (codes, callback) {
                // Implementation
            },
            /**
             * Gets the price information for the given productIds.
             * The callback will be called with a JSONArray of ProductInfo objects.
             */
            getPrices: function (productIds, callback) {
                // Implementation
            }
        }
    }

.. versioned-toggle-box:: purchase
  :versionadded-android: 3.0.0
  :versionadded-ios: 3.0.0
  :color: purple

  The :code:`purchase` method can be used to purchase a single product, e.g. an
  issue.

  It takes two parameters: the product id and a callback function.

  The callback function gets called with one parameter.

  For successful purchases it will be a simple json object:

  .. code-block:: javascript

    {
      "success": true
    }

  For failures it will be json object which may contain an error code:

  .. code-block:: javascript

    {
      "success": false,
      "error_code": "CANCELLED"
    }

.. versioned-toggle-box:: subscribe
  :versionadded-android: 3.0.0
  :versionadded-ios: 3.0.0
  :color: purple

  The :code:`subscribe` method can be used to purchase a subscription.

  It takes two parameters: the product id and a callback function.

  The callback function gets called with one parameter.

  For successful purchases it will be a simple json object:

  .. code-block:: javascript

    {
      "success": true
    }

  For failures it will be json object which may contain an error code:

  .. code-block:: javascript

    {
      "success": false,
      "error_code": "CANCELLED"
    }

.. versioned-toggle-box:: restorePurchases
  :versionadded-android: 3.0.0
  :versionadded-ios: 3.0.0
  :color: purple

  Previously purchased products and subscriptions can be restored using the
  :code:`restorePurchases` method.

  It takes one parameter, a callback function, which gets called when the restore
  has finished.

  The callback function gets called with one parameter: a success or failure
  result object. See purchase / subscribe for details about this object.

  .. note::

    This call is only available on iOS. It will do nothing on Android and call
    the callback function immediately with a success-object.

.. versioned-toggle-box:: setPurchaseStateListener
  :versionadded-android: 3.0.0
  :versionadded-ios: 3.0.0
  :color: purple

  Set a function as a listener which will be called when the purchase state of
  a subscription product changed.

  .. note::

    This call is only available on iOS. It will do nothing on Android.

.. versioned-toggle-box:: getSubscriptionCodes
  :versionadded-android: 3.0.0
  :versionadded-ios: 3.0.0
  :color: purple

  Get the current subscription codes.

  It takes one parameter, a callback function, which gets called with the
  subscription codes in a string array as the only parameter.

.. versioned-toggle-box:: addSubscriptionCodes
  :versionadded-android: 3.0.0
  :versionadded-ios: 3.0.0
  :color: purple

  Add and activate (multiple) subscription codes.

  It takes two parameters: the codes as a string array and a callback function,
  which gets called with a success or failure result object.
  See purchase / subscribe for details about this object.

.. versioned-toggle-box:: removeSubscriptionCodes
  :versionadded-android: 3.0.0
  :versionadded-ios: 3.0.0
  :color: purple

  Remove and deactivate (multiple) subscription codes.

  It takes two parameters: the codes as a string array and a callback function,
  which gets called with a success or failure result object.
  See purchase / subscribe for details about this object.

.. versioned-toggle-box:: getPrices
  :versionadded-android: 3.3.0
  :versionadded-ios: 3.4.0
  :color: purple

  This method requests the price information for given product ids. It takes two parameters: The first is an array of product ids and the second a callback method that will be called with an array of product info objects.

  .. code-block:: javascript

      {
        "productId": "some.product.id",
        "formattedPrice": "13.37€",
        "price": 13.37,
        "currency": "EUR"
      }

Issue
*****

This API can be used to retrieve information (e.g. pages and toc from the :code:`pages.xml` and :code:`TOC.xml`)
of the current issue.

.. code-block:: javascript
  :caption: Issue JavaScript-Interface

  window.purple = {
      issue: {
          getPages: function (callback) {
              // Implementation
          },
          getToc: function (callback) {
              // Implementation
          }
      }
  }

.. versioned-toggle-box:: getPages
  :versionadded-android: 3.3.0
  :versionadded-ios: 3.3.0
  :versionadded-web-player: 3.2.0
  :versionadded-composer: 3.1.0
  :color: green

  The :code:`getPages` method can be used to retrieve all pages.

  It takes one parameter: a callback function.

  The callback function gets called with one parameter: an array of page model objects.

  |

  .. code-block:: json
    :caption: Page model

    {
      "id": "",
      "pageIndex": 1,
      "pageNumber": 1,
      "pageLabel": "Seite 1",
      "title": "Seite 1",
      "shortTitle": "Seite 1",
      "alias": "Seite 1",
      "showPurchaseSuggestion": true,
      "placeholder": false,
      "excludeFromPaging": true,
      "thumbnailURL": "",
      "sharingEnabled": true,
      "sharingText": "Text",
      "sharingURL": "http://example.com",
      "customData": "tag1,tag2"
    }

.. versioned-toggle-box:: getToc
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-player: 3.3.0
  :versionadded-composer: TODO
  :color: green

  The :code:`getToc` method can be used to retrieve all toc pages.

  It takes one parameter: a callback function.

  The callback function gets called with one parameter: an array of toc page model objects.

  |

  .. code-block:: json
    :caption: Toc page model

    {
      "pageId": "<page-id>",
      "pageAlias": "Page Alias",
      "title": "Title 123",
      "section": "Section",
      "shortTitle": "Old Content Short-Title",
      "teaser": "Old Content Only",
      "thumbnailURL": "pkmedia://thumbs/thumb-page123.jpg"
    }

State
*****

This API can be used to store custom state for usage in different webviews.
It can only store string values.

.. code-block:: javascript
  :caption: State JavaScript-Interface

  window.purple = {
      state: {
          setState: function (key, value) {
              // Implementation
          },
          getState: function (key, callback) {
              // Implementation
          }
      }
  }

.. note::

  On macOS the state is stored on a per document bases inside the users defaults.
  This means that the state data is not part of the Purple-Project files.

.. versioned-toggle-box:: setState
  :versionadded-android: 3.3.0
  :versionadded-ios: 3.3.0
  :versionadded-web-player: 3.1.4
  :versionadded-web-kiosk: 3.7.0
  :versionadded-composer: 3.1.0
  :color: blue

  The :code:`setState` method can be used to store a string value for a string key.

  It takes two parameters: the key and a value.

  If the value is :code:`null` the key gets deleted.

  .. hint:: The key is case-sensitive.

.. versioned-toggle-box:: getState
  :versionadded-android: 3.3.0
  :versionadded-ios: 3.3.0
  :versionadded-web-player: 3.1.4
  :versionadded-web-kiosk: 3.7.0
  :versionadded-composer: 3.1.0
  :color: blue

  The :code:`getState` method can be used to retrieve a string value for a string key.

  It takes two parameters: the key and a callback function.

  The callback function gets called with two parameters: the key and the value.
  If there is no value for the given key, the value will be :code:`null`.

  .. hint:: The key is case-sensitive.

Web Player specifics
********************
Due to WebViews being implemented using iframes in Web Player and Web Newsstand, JavaScript
injection works different in this context.

The global purple object can be made available by including :code:`purpleInterface.js`
in the embedded page. An interface for the Purple Object is
re-implemented in the child page. When a function of the purple object is
called, a HTML5 PostMessage will be sent to the parent window (Web Player / Web Newsstand).
This will invoke the actual call on the Purple Object. The Web Player / Web Newsstand will then
respond with another HTML 5 PostMessage which the child window (iframe) will
process.

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
        receiveMessage: function (event) {
            try {
                // get response data
                var responseData = JSON.parse(event.data);
                var value = responseData.value;
                var callbackId = responseData.callbackId;
                var key = responseData.key;

                if (callbackId) {
                    // call callback function from callback map
                    if(key) {
                        window.purpleInterface.callbacks[callbackId](key, value);
                    } else {
                        window.purpleInterface.callbacks[callbackId](value);
                    }
                    // delete callback
                    window.purpleInterface.callbacks[callbackId] = null;
                } else if(key === 'RELOAD'){
                    window.document.location.reload();
                } else if(key === 'HISTORY_BACK') {
                    window.history.back();
                } else if(key === 'HISTORY_FORWARD') {
                    window.history.forward();
                } else if(key === 'DOCUMENT_TITLE') {
                    window.purpleInterface.util.postMessage('DOCUMENT_TITLE', 'DOCUMENT_TITLE', document.title);
                }

            } catch (e) {
            }
        },
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
                if (callback) {
                    // create id = index in callback array
                    var callbackId = window.purpleInterface.util.generateUUID();
                    requestData.callbackId = callbackId;
                    // add callback to callback array
                    window.purpleInterface.callbacks[callbackId] = callback;
                }

                // call postMessage
                window.parent.postMessage(JSON.stringify(requestData), '*');
            }

        },
        generateUUID: function () {
            var d = new Date().getTime();
            return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
                var r = (d + Math.random() * 16) % 16 | 0;
                d = Math.floor(d / 16);
                return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
            });
        }
      }
    };

    document.addEventListener('DOMContentLoaded', function () {
        window.addEventListener('message', window.purpleInterface.util.receiveMessage);

        window.purpleInterface.util.postMessage('LOAD', 'LOAD', null, function () {

            if (!window.purple) {

                window.purple = {};

                var links = document.querySelectorAll('a[href^="purple://"], a[ ^="pkapp://"], a[href^="pkitem://"]');
                for (var i = 0; i < links.length; i++) {
                    links[i].addEventListener('click', function (e) {
                        window.purpleInterface.util.postMessage('ACTION_URL', 1, this.href);
                        e.preventDefault();
                    });
                }

                // purple object
                window.purple.metadata = {
                    getMetadata: function (key, callback) {
                        window.purpleInterface.util.postMessage('META', key, null, callback);
                    }
                };

                window.purple.state = {
                    setState: function (key, value) {
                        window.purpleInterface.util.postMessage('STATE', key, value, null);
                    },
                    getState: function (key, callback) {
                        window.purpleInterface.util.postMessage('STATE', key, null, callback);
                    }

                };

                window.purple.issue = {
                    getPages: function (callback) {
                        window.purpleInterface.util.postMessage('PAGES', 'PAGES', null, callback);
                    },
                    getToc: function (callback) {
                        window.purpleInterface.util.postMessage('TOC', 'TOC', null, callback);
                    }
                };

                window.purple.closeView = function() {
                    window.purpleInterface.util.postMessage('CLOSE_VIEW', 'CLOSE_VIEW');
                };

                if ('onPurpleLoad' in window && typeof onPurpleLoad === 'function') {
                    onPurpleLoad();
                }

                var search = window.location.search;
                if (document.referrer){
                    if (search) {
                        search += '&' + document.referrer.split('?')[1];
                    } else {
                        search = '?' + document.referrer.split('?')[1];
                    }
                }
                history.replaceState({}, document.title, window.location.origin + window.location.pathname + search);
            }

        });
    });

