######
Appboy
######

.. versionadded:: 2.1.0

|Appboy| is a tracking service which supports tracking events (actions / purchases) and storing attributes.

.. |Appboy| raw:: html

   <a href="https://www.appboy.com/" target="_blank">Appboy</a>

Events
######

Overview
********

+-----------------------+------------------------+-----------------------+------------------------+-----------------------+
| Key-Name in Config    | Action Templates       | View Templates        | Purchase Templates     | Attribute Templates   |
+=======================+========================+=======================+========================+=======================+
|                       |                        |                       |                        |                       |
| appboy                | :code:`action`         | :fg-red:`unsupported` | :fg-red:`unsupported`  | :code:`name`          |
|                       |                        |                       |                        |                       |
+-----------------------+------------------------+-----------------------+------------------------+-----------------------+

Actions
*******

Appboy supports tracking of action events. The actual value sent to Appboy is configured through template with the key :code:`action`.

Views
*****

Appboy does not support view events.

Purchases
*********

Appboy supports tracking of purchase events. Purchase events cannot be configured (besides enabling/disabling the whole event) and
always the track the product id, currency code and price.

Attributes
**********

Appboy supports storing attributes per user. The name of the attribute can be configured through the :code:`name` template.

Event parameters
****************

Appboy does not support sending custom parameters.

Configuration Example
#####################

.. code-block:: json

  {
    "appboy": {
      "eventsEnabledByDefault": false,
      "purchasesEnabledByDefault": false,
      "attributesEnabledByDefault": false,
      "events": {
        "APP_BOOKMARK_ADDED": {
          "enabled": true,
          "templates": {
            "action": "Bookmark added"
          }
        }
      },
      "purchases": {
        "KIOSK_ISSUE_PURCHASED": {
          "enabled": true
        }
      },
      "attributes": {
        "HAS_ACTIVE_SUBSCRIPTION": {
          "enabled": true,
          "templates": {
            "name": "Has an active subscription"
          }
        }
      }
    }
  }
