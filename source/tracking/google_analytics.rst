################
Google Analytics
################

.. versionadded:: 2.1.0

|GoogleAnalytics| is a tracking service which supports tracking events (actions, views, purchases).

.. |GoogleAnalytics| raw:: html

   <a href="https://www.google.com/analytics/" target="_blank">Google Analytics</a>

Campaign Tracking
#################

Google Analytics supports campaign tracking for both app installs and deep links (Purple Action-URLs).
For information on how to adjust your Play Store links you can consult the |GoogleAnalyticsCampaigns|.
For Purple Action-URLs you just have to append your campaign parameters to the URL.

.. |GoogleAnalyticsCampaigns| raw:: html

   <a href="https://support.google.com/analytics/answer/1033863?hl=en" target="_blank">official documentation</a>

Events
######

Overview
********

+-----------------------+------------------------+-----------------------+------------------------+-----------------------+
| Key-Name in Config    | Action Templates       | View Templates        | Purchase Templates     | Attribute Templates   |
+=======================+========================+=======================+========================+=======================+
|                       | - :code:`category`     |                       |                        |                       |
| google_analytics      | - :code:`action`       | :code:`name`          | :fg-red:`unsupported`  | :fg-red:`unsupported` |
|                       | - :code:`label`        |                       |                        |                       |
+-----------------------+------------------------+-----------------------+------------------------+-----------------------+

Actions
*******

Google Analytics supports tracking of action events. The actual values sent to
Google Analytics is configured through :code:`category`, :code:`action` and :code:`label` templates.

Views
*****

Google Analytics supports tracking of action events. The view name send to
Google Analytics is configured through template with the key :code:`name`.

Purchases
*********

Google Analytics supports tracking of purchase events. Purchase events cannot
be configured (besides enabling/disabling the whole event) and always the
track the product id, currency code and price.

Attributes
**********

Google Analytics does not support storing attributes per user.

Event parameters
****************

Google Analytics does not support sending custom parameters.

Configuration Example
#####################

.. code-block:: json

  {
    "google_analytics": {
      "eventsEnabledByDefault": false,
      "viewsEnabledByDefault": false,
      "purchasesEnabledByDefault": false,
      "events": {
        "APP_BOOKMARK_ADDED": {
          "enabled": true,
          "templates": {
            "category": "App",
            "action": "Bookmark added",
            "label": "{{CONTENT_NAME}}"
          }
        }
      },
      "views": {
        "APP_BOOKMARKS": {
          "enabled": true,
          "templates": {
            "name": "App bookmarks"
          }
        }
      },
      "purchases": {
        "KIOSK_ISSUE_PURCHASED": {
          "enabled": true
        }
      }
    }
  }
