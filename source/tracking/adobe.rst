###############
Adobe Analytics
###############

.. versionadded:: 3.4.0

|AdobeAnalytics| is a tracking service which supports tracking events (actions, views, purchases).

.. |AdobeAnalytics| raw:: html

   <a href="http://www.adobe.com/de/marketing-cloud/web-analytics.html" target="_blank">Adobe Analytics</a>

Events
######

Overview
********

+-----------------------+-------------------------+-----------------------+--------------------------+-----------------------+
| Key-Name in Config    | Action Templates        | View Templates        | Purchase Templates       | Attribute Templates   |
+=======================+=========================+=======================+==========================+=======================+
|                       |                         |                       |                          |                       |
| adobeanalytics        | :code:`action`          | :code:`name`          | :code:`action`           | :fg-red:`unsupported` |
|                       |                         |                       |                          |                       |
+-----------------------+-------------------------+-----------------------+--------------------------+-----------------------+

Actions
*******

Adobe Analytics supports tracking of action events. The actual value sent to Adobe is configured through template with the key :code:`action`.

Views
*****

Adobe Analytics supports tracking of view events. The actual value sent to Adobe is configured through template with the key :code:`name`.

Purchases
*********

Adobe Analytics supports tracking of purchase events.  The actual value sent to Adobe is configured through template with the key :code:`action`.

Attributes
**********

Adobe Analytics does not support storing attributes.

Event parameters
****************

Adobe Analytics supports sending custom parameters for actions, views and purchases.

Configuration Example
#####################

.. code-block:: json

  {
    "adobeanalytics": {
      "events": {
        "APP_BOOKMARK_ADDED": {
          "templates": {
            "action": "Bookmark added {{CONTENT_NAME}}"
          },
          "parameters": {
            "pageinfo.brand": "purple"
          }
        }
      },
      "views": {
        "KIOSK_CHANNEL_FEED": {
          "templates": {
            "name": "Kiosk channel {{PUBLICATION_NAME}}"
          },
          "parameters": {
            "pageinfo.brand": "purple"
          }
        }
      },
      "purchases": {
        "KIOSK_ISSUE_PURCHASED": {
          "templates": {
            "action": "Issue purchased {{ISSUE_ID}}"
          },
          "parameters": {
            "pageinfo.brand": "purple",
            "issue.id": "{{ISSUE_ID}}"
          }
        }
      }
    }
  }
