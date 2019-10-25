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
***********************

Apps support the :code:`window.open` JavaScript-API. Starting with 3.11 links
opened via this API will be opened in the internal App Browser (with title bar, status bar and navigation, as a "new window")
or the same webview, according to the standard browser specifications.

Starting with version 3.10 Action URLs can also be opened via this API on all platforms.

Cookies
*******

Starting with version 3.13.0 cookies are enabled for all webviews in the Android and iOS apps.

Accessing dynamic resources
***************************

Starting with version 5.1 it is possible to access files inside the dynamic resources by using the :code:`resource` scheme.
These urls must have the following structure:

resource://dynamic/``<path>``

The path should point towards a file inside the dynamic resources.
These paths are resolved based on device's preferred languages. The same goes for all relative paths if the html itself was loaded using this scheme.
This allows reducing the total size of the dynamic resources bundle by putting common files in the default folder and localization related files in their respective folders (e.g. de, en, ...).
For further information on dynamic resources and how files are resolved based on the device's preferred languages see the corresponding :ref:`page <dyn-res-localization>`.

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
      },
      tracking: {
          ...
      },
      media: {
          ...
      }
  }

Due to the asynchronous nature of the javascript bridge all api calls that return values require a callback function as a parameter.
This function is then called by the native implementation with the value as its parameter. A common usage would look like this:

.. code-block:: javascript
  :linenos:
  :caption: Sample usage of callback functions

  function callbackFunctionForSomething(valueOfSomething) {
      console.log(valueOfSomething);
  }

  window.purple.getSomething(callbackFunctionForSomething);

  // or inline:

  window.purple.getSomething(function(valueOfSomething) {
      console.log(valueOfSomething)
  });

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
        /**
         * Get the display mode for the current webview.
         */
        getDisplayMode: function (callback) {
            // Implementation
        },
        /**
         * Get the titlebar configuration for the current webview.
         */
        isTitleBarEnabled: function (callback) {
            // Implementation
        },
        /**
         * Get the controls configuration for the current webview.
         */
        isControlsEnabled: function (callback) {
            // Implementation
        },
        /**
         * Get the statusbar configuration for the current webview.
         */
        isStatusBarEnabled: function (callback) {
            // Implementation
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
           * Get metadata values by key. A callback function with a single parameter is required that will be called
           * with the value for the given key.
           *
           * @param {string} key          the metadata key
           * @param {Function} callback   the callback for the value
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

  .. versioned-toggle-box:: entitlement_mode
    :color: blue
    :versionadded-android: 3.11.0
    :versionadded-ios: 3.11.0

    Can be either ``entitlement``, ``oauth`` or ``none`` indicating the mode of the first entitlement server that is configured for the app.

    |

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: entitlement_refresh_token
    :color: blue
    :versionadded-android: 3.11.0
    :versionadded-ios: 3.11.0

    The refresh token that is being used to request a new access token for the entitlement api calls. This value is only available if oauth is being used as entitlement server.

    |

    **Available contexts**

    * Entitlement HTML Login
    * Dynamic HTML-Content
    * In-App-Browser
    * Storytelling Content

  .. versioned-toggle-box:: issue_id
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0
    :versionchanged: Android/iOS 3.17: Property now available in dynamic HTML and In-App-Browser (see below)

    The id of the currently viewed issue.

    **Available contexts**

    * Storytelling Content
    * Dynamic HTML-Content (when opened via an ST-Action)
    * In-App-Browser (when opened via an ST-Action)

  .. versioned-toggle-box:: issue_name
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0

    The name of the currently viewed issue.

    |

    In the Composer Preview on macOS this always returns "Preview Publication".

    |

    **Available contexts**

    * Storytelling Content
    * Dynamic HTML-Content (when opened via an ST-Action)
    * In-App-Browser (when opened via an ST-Action)

  .. versioned-toggle-box:: issue_alias
    :color: blue
    :versionadded-android: 3.17.0
    :versionadded-ios: 3.17.0

    The alias of the currently viewed issue.

    |

    **Available contexts**

    * Storytelling Content
    * Dynamic HTML-Content (when opened via an ST-Action)
    * In-App-Browser (when opened via an ST-Action)

  .. versioned-toggle-box:: publication_id
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0
    :versionchanged: Android/iOS 3.17: Property now available in dynamic HTML and In-App-Browser (see below)

    The id of the publication of the currently viewed issue.

    |

    In the Composer Preview on macOS this always returns "Preview Publication".

    |

    **Available contexts**

    * Storytelling Content
    * Dynamic HTML-Content (when opened via an ST-Action)
    * In-App-Browser (when opened via an ST-Action)

  .. versioned-toggle-box:: publication_name
    :color: blue
    :versionadded-android: 2.4.0
    :versionadded-ios: 2.4.0
    :versionadded-composer: 3.1.0
    :versionadded-web-player: 2.6.0
    :versionchanged: Android/iOS 3.17: Property now available in dynamic HTML and In-App-Browser (see below)

    The name of the publication of the currently viewed issue.

    On macOS this always returns "Preview Publication".

    **Available contexts**

    * Storytelling Content
    * Dynamic HTML-Content (when opened via an ST-Action)
    * In-App-Browser (when opened via an ST-Action)

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

.. _webviews_storefront:

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
           * JSONArray of Publication objects.
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
           * Gets the issue object for the given issueId. The callback function
           * will be called with the corresponding Issue object. If the issueId
           * is the id of a preview issue, then the corresponding parent issue
           * will be returned.
           */
          getIssueById: function (issueId, callback) {
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
          /**
           * Returns the base url for the files of the given issueId.
           */
          getIssueBaseUrl: function (issueId, callback) {
              // Implementation
          },
          /**
           * Returns the pages information for the given issueId.
           */
          getIssuePages: function (issueId, callback) {
              // Implementation
          },
          /**
           * Returns the toc information for the given issueId.
           */
          getIssueToc: function (issueId, callback) {
              // Implementation
          },
          /**
           * Open a list of articles in a pager.
           */
          openArticles: function (articleIds, initialArticleId, callback) {
              // Implementation
          },
          /**
           * Get a list of all categories. The callback will be called with a
           * JSONArray of Category objects.
           */
          getCategories: function (callback) {
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
  :versionchanged: Android/iOS 3.15: The issue alias is now also available, 4.0: :code:`LOCKED` issues are not returned anymore, 5.1: Added :code:`publicationId`
  :color: purple

  This method needs to be called to obtain a list of issues for a specific publication.
  It takes two parameters: A :code:`publicationId` and a callback function which then will be called with an array of issues.
  The :code:`publicationId` can be acquired from a publication model that is obtained through the getPublications method.

  |

  .. code-block:: javascript
    :caption: Issue model

    {
      "issueId": "aabbcc",
      "publicationId": "ddeeff",
      "alias": "alias2",
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
      },
      "productId": "com.sprylab.issue1",
      "thumbnails": {
        "default": "url",
        "kind1": "url"
      },
      "tags": ["tag1", "tag2", "tag3"],
      "categories": ["categoryId1", "categoryId2"]
    }

  The :code:`pubDate` is a UNIX timestamp in ms.
  If the issue has a preview issue then :code:`previewIssue` is a jsonObject with the preview issue's id, its content size and the number of pages otherwise it is :code:`null`.
  The :code:`productId` can be used to purchase the issue through the :code:`store` api. It can be :code:`null` if the issue is not purchasable through in app payments.

.. versioned-toggle-box:: getIssueStates
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-kiosk: 3.7.0
  :versionchanged: 4.0: removed :code:`LOCKED` and :code:`UPDATE` states, added updateAvailable to the state model and states for progressive loading, 5.0: removed :code:`INSTALLING` state
  :color: purple

  To obtain the state of specific issues this method can be used.
  It takes two parameters. The first is an array of issue ids and the second a callback function which returns an array of issue state objects for the requested issue ids.

  |

  .. code-block:: javascript
    :caption: Issue state model

    {
      "issueId": "aabbcc",
      "state": "<STATE>",
      "updateAvailable": <true|false>
    }

  Certain states are only available depending whether progressive loading is enabled or not.
  Note that issues that are hidden through entitlement are not returned by getIssues anymore until they are unlocked.
  The following table describes the possible issue states.

    .. role:: fg-gray

    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | State                           | Description                                                                         | PL               | PK      |
    +=================================+=====================================================================================+==================+=========+
    | LOCKED                          | locked through entitlement -> not visible for the user                              | :fg-green:`off`  | <4.0    |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | COMING_SOON                     | coming soon enabled -> visible, but not downloadable                                | :fg-gray:`any`   | >=3.4.0 |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | PURCHASABLE                     | not purchased                                                                       | :fg-gray:`any`   | >=3.4.0 |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | AVAILABLE                       | download possible -> purchased, or no paid content                                  | :fg-gray:`any`   | >=3.4.0 |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | INDEXING                        | minimal required                                                                    | :fg-green:`on`   | >=4.0   |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | PARTIALLY_INSTALLED_DOWNLOADING | ready to be displayed, still loading and not finished yet                           | :fg-green:`on`   | >=4.0   |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | PARTIALLY_INSTALLED_PAUSED      | ready to be displayed, not loading and not finished yet                             | :fg-green:`on`   | >=4.0   |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | DOWNLOAD_PAUSED                 | download started and paused                                                         | :fg-red:`off`    | >=3.4.0 |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | DOWNLOADING                     | downloading (and extracting on >= PK 5.0)                                           | :fg-red:`off`    | >=3.4.0 |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | INSTALLING                      | extracting, post processing                                                         | :fg-red:`off`    | <5.0    |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | INSTALLED                       | downloaded, extracted, available for reading                                        | :fg-gray:`any`   | >=3.4.0 |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+
    | UPDATE                          | downloaded and new version available (=local version does not match remote version) | :fg-red:`off`    | <4.0    |
    +---------------------------------+-------------------------------------------------------------------------------------+------------------+---------+


.. versioned-toggle-box:: getIssueById
  :versionadded-android: 5.1
  :versionadded-ios: 5.1
  :color: purple

  This method can be used to request information for a single issue with a given issueId.
  The callback function will be called with the corresponding Issue Object. See getIssues for the structure of such an object.
  When the passed issueId is the id of a preview issue then the corresponding parent issue is returned instead.

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
  :versionchanged: 5.0 changed behavior of the progress in the :code:`DOWNLOADING` state
  :color: purple

  The :code:`addIssueStateListener` method allows the registration of a listener that will be called each time when the state of an issue changes.
  This method takes a single parameter which is a callback function. It will be called with issue state objects which contain an additional :code:`progress` value.
  This :code:`progress` can be a value between 0 and 100.

  For a description of the states see the table in :code:`getIssueStates`.

  |

  .. code-block:: javascript
    :caption: Issue state model (with progress, for possible states see getIssueStates)

    {
      "issueId": "aabbcc",
      "state": "<STATE>",
      "updateAvailable": <true|false>,
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
  :versionchanged: Android/iOS 3.15: Callback now has a parameter (see below)
  :color: purple

  The :code:`addUpdateListener` method allows the registration of a listener that will be called each time the kiosk has been changed due to a sync or login change.
  This method takes a single parameter which is a callback function which itself takes one parameter.

  This parameter will be a JSON object with the following format:

  .. code-block:: javascript
    :linenos:

    {
       type: "PARTIAL|FULL|LOGIN|LOGOUT",
       success: true
    }

  Or for errors:

  .. code-block:: javascript
    :linenos:

    {
       type: "PARTIAL|FULL|LOGIN|LOGOUT",
       success: false,
       error_code: "OFFLINE|UNKNOWN"
    }


.. versioned-toggle-box:: removeUpdateListener
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: purple

  This method removes a listener that was previously added with :code:`addUpdateListener` to stop receiving kiosk updates.

.. versioned-toggle-box:: getIssueBaseUrl
  :versionadded-android: 3.13.0
  :versionadded-ios: 3.13.0
  :color: purple

  This method can be used to retrieve the base url for the given issueId. If the issue is not downloaded yet, the callback is called with :code:`null`.
  With this base url it is possible to request files of an issue. Requests to the :code:`pages.xml` and :code:`TOC.xml` will return :code:`404 Not Found`.
  To request the contents of these files, the :code:`storefront.getIssuePages()` and :code:`storefront.getIssueToc()` methods should be used.

.. versioned-toggle-box:: getIssuePages
  :versionadded-android: 3.13.0
  :versionadded-ios: 3.13.0
  :color: purple

  This method works the same as issue.getPages() except that it takes an issueId as parameter and returns the data for that issue.
  See :ref:`issue.getPages() <webviews_issue_getpages>` for details regarding the page model.

.. versioned-toggle-box:: getIssueToc
  :versionadded-android: 3.13.0
  :versionadded-ios: 3.13.0
  :color: purple

  This method works the same as issue.getToc() except that it takes an issueId as parameter and returns the data for that issue.
  See :ref:`issue.getToc() <webviews_issue_gettoc>` for details regarding the toc model.

.. versioned-toggle-box:: openArticles
  :versionadded-android: 3.14.0
  :versionadded-ios: 3.14.0
  :color: purple

  Opens a list of articles by their issue ID in a native pager.
  Invalid issues, e.g. paid issues, non-channel issues, will be filtered. If no
  issues remain to be opened, the callback will be called with the `error_code`
  `NO_ISSUES_FOUND`.

  The second parameter may be an issue ID from the list of issue IDs which will
  be the initially opened issue. If the issue ID is invalid, the first valid issue
  will be shown.

  When the articles have been successfully opened the callback function will be
  called with a simple json object:

  .. code-block:: javascript
    :linenos:

    {
      "success": true
    }

  For failures it will be a json object which may contain an error code:

  .. code-block:: javascript
    :linenos:

    {
      "success": false,
      "error_code": "[NO_ISSUES_FOUND|UNKNOWN]"
    }

.. versioned-toggle-box:: getCategories
  :versionadded-android: 3.15.0
  :versionadded-ios: 3.15.0
  :color: purple

  Gets a list of all categories. The callback will be called with a JSONArray like the following example:

  .. code-block:: javascript
    :linenos:

    [
      {
        "id": "categoryId1",
        "name": "Category name",
        "thumbnailURL": "http://",
        "properties": { "name": "value" },
        "categories": [
          {
            "id": "categoryId2",
            "name": "Category name 2",
            "thumbnailURL": "http://",
            "properties": { "name": "value" },
            "categories": []
          }
        ]
      },
      {
        "id": "categoryId3",
        "name": "Category name",
        "thumbnailURL": "http://",
        "properties": { "name": "value" },
        "categories": []
      }
    ]

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

  For failures it will be a json object which may contain an error code:

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

  For failures it will be a json object which may contain an error code:

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

.. _webviews_issue_getpages:

.. versioned-toggle-box:: getPages
  :versionadded-android: 3.3.0
  :versionadded-ios: 3.3.0
  :versionadded-web-player: 3.2.0
  :versionadded-composer: 3.1.0
  :versionchanged: 3.13 :code:`targetURL` has been added to the response. :code:`targetURL` and :code:`thumbnailURL` do not have a scheme such as :code:`pkmedia://` anymore and are now relative to the content root.
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
      "targetURL": "page-id.stxml",
      "thumbnailURL": "thumbs/thumb-page123.jpg",
      "sharingEnabled": true,
      "sharingText": "Text",
      "sharingURL": "http://example.com",
      "customData": "tag1,tag2"
    }

.. _webviews_issue_gettoc:

.. versioned-toggle-box:: getToc
  :versionadded-android: 3.4.0
  :versionadded-ios: 3.4.0
  :versionadded-web-player: 3.3.0
  :versionadded-composer: TODO
  :versionchanged: 3.13 :code:`thumbnailURL` does not have a scheme such as :code:`pkmedia://` anymore and is now relative to the content root.
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
      "thumbnailURL": "thumbs/thumb-page123.jpg"
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

Tracking
********

This API can be used to track custom events in web views (e.g. purchase over an external entitlement or custom view like read mode).
There are three different types of events:

#. Actions
#. Views
#. Purchases

The events are forwarded to the app's enabled :doc:`tracking services<tracking>`. The same :doc:`configuration mechanism<tracking>` like in the apps is used.

.. note::

  User Attributes are currently not supported.

.. code-block:: javascript
  :linenos:
  :caption: Tracking JavaScript-Interface

  window.purple = {
      tracking: {
      /**
      * Track an action, e.g. a tap on a button.
      *
      * @param {string} key the event name
      * @param {Object} [optionalParams] can be sent with each event if the tracking service supports this.
      * Every key will be included in the event. The values can contain all placeholders supported for the event
      * and will be evaluated (see app tracking) when sending the event to the service.
      * @param {Function} [callback] is called when the event has been tracked
      */
      trackAction: function (key, optionalParams, callback) {
          },
      /**
      * Track a view, e.g. a currently shown screen.
      *
      * @param {string} key the key of the screen event
      * @param {Object} [optionalParams] can be sent with each event if the tracking service supports this.
      * Every key will be included in the event. The values can contain all placeholders supported for the event
      * and will be evaluated (see app tracking) when sending the event to the service.
      * @param {Function} [callback] is called when the event has been tracked
      */
      trackView: function (key, optionalParams, callback) {
          },
      /**
      * Track a purchase.
      *
      * @param {string} key the purchase event key
      * @param {string} productId
      * @param {number} price
      * @param {string} currencyCode
      * @param {string} transactionId
      * @param {Object} [optionalParams] can be sent with each event if the tracking service supports this.
      * Every key will be included in the event. The values can contain all placeholders supported for the event
      * and will be evaluated (see app tracking) when sending the event to the service.
      * @param {Function} [callback] is called when the event has been tracked
      */
      trackPurchase: function (key, productId, price, currencyCode, transactionId, optionalParams, callback) {
          }
      }
  }

.. note::

  The :code:`optionalParams` (key-value pairs) can be sent with each event if the tracking service supports this. Every key will be included in the event. The values can contain all placeholders supported for the event and will be evaluated (see :doc:`app tracking<tracking>`) when sending the event to the service.

.. versioned-toggle-box:: trackAction
  :versionadded-android: 3.10.3
  :versionadded-ios: 3.10.5
  :versionadded-web-player: 3.11.0
  :versionadded-web-kiosk: 3.11.0
  :versionchanged: 3.14.0 added callback
  :color: blue

  The :code:`trackAction` method can be used to track a custom action event.

  It takes two parameters: key and optionalParams.
  Starting with 3.14.0 the method takes a callback function which is called when
  the event has been tracked.

.. versioned-toggle-box:: trackView
  :versionadded-android: 3.10.3
  :versionadded-ios: 3.10.5
  :versionadded-web-player: 3.11.0
  :versionadded-web-kiosk: 3.11.0
  :versionchanged: 3.14.0 added callback
  :color: blue

  The :code:`trackView` method can be used to track a custom view event.

  It takes two parameters: key and optionalParams.
  Starting with 3.14.0 the method takes a callback function which is called when
  the event has been tracked.

.. versioned-toggle-box:: trackPurchase
  :versionadded-android: 3.10.3
  :versionadded-ios: 3.10.5
  :versionadded-web-player: 3.11.0
  :versionadded-web-kiosk: 3.11.0
  :versionchanged: 3.14.0 added callback
  :color: blue

  The :code:`trackPurchase` method can be used to track a custom purchase event.

  It takes six parameters: key, productId, price, currencyCode, transactionId and optionalParams.
  Starting with 3.14.0 the method takes a callback function which is called when
  the event has been tracked.

Media
*****

This API can be used to play remote audio streams and files. The audio will
continue playing even if the user puts the app to the background.

.. code-block:: javascript
  :linenos:
  :caption: Media JavaScript-Interface

  window.purple = {
    media: {
      startAudio: function (displayName, url) {
          // Implementation
      },
      pauseAudio: function () {
          // Implementation
      },
      resumeAudio: function () {
          // Implementation
      },
      stopAudio: function () {
          // Implementation
      },
      seekTo: function(time) {
          // Implementation
      },
      setPlaybackRate: function (rate) {
          // Implementation
      },
      getPlaybackRate: function (callback) {
          // Implementation
      },
      addStatusListener: function (statusListener) {
          // Implementation
      },
      removeStatusListener: function (statusListener) {
          // Implementation
      },
      addProgressListener: function (progressListener) {
         // Implementation
      },
      removeProgressListener: function (progressListener) {
          // Implementation
      }
    }
  };

.. versioned-toggle-box:: startAudio
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Starts a remote audio stream or file. This method takes two parameters:
  a display name used for notification and player UI and the URL to play.

.. versioned-toggle-box:: pauseAudio
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Pauses the current audio playback.

.. versioned-toggle-box:: resumeAudio
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Resumes the current audio playback.

.. versioned-toggle-box:: stopAudio
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Stops the current audio playback.

.. versioned-toggle-box:: seekTo
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Seeks to the given time in the current audio playback. This method takes the
  desired time in milliseconds.

.. versioned-toggle-box:: setPlaybackRate
  :versionadded-android: 4.0
  :versionadded-ios: 4.0
  :color: blue

  Sets the playback rate to the specified value.
  Only values between 0.5 and 2.0 are allowed. Values outside these bounds will be clipped to their respective limits.
  The playback rate gets reset to the default rate of 1.0 on app restarts.

.. versioned-toggle-box:: getPlaybackRate
  :versionadded-android: 4.0
  :versionadded-ios: 4.0
  :color: blue

  Requests the current playback rate which will be the single parameter of the callback function.

.. versioned-toggle-box:: addStatusListener
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Adds a listener for playback state changes.

.. versioned-toggle-box:: removeStatusListener
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Removes a listener for playback state changes.

.. versioned-toggle-box:: addProgressListener
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Adds a listener for playback progress changes.

.. versioned-toggle-box:: removeProgressListener
  :versionadded-android: 3.11.0
  :versionadded-ios: 3.11.0
  :color: blue

  Removes listener for playback progress changes.

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

