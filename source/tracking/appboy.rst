#####
Braze
#####

.. versionadded:: 2.1.0

.. warning:: Please note: Due to changed conditions for app developers on the part of Braze, we can no longer support this service free of charge. Therefore, we do not provide any general warranty for correct operation when activating this feature. Individual support inquiries are welcome via support@sprylab.com.

|Braze| (formerly known as Appboy) is a tracking service which supports tracking events (actions / purchases) and storing attributes.

.. |Braze| raw:: html

   <a href="https://www.braze.com/" target="_blank">Braze</a>

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


.. note:: Due to compatibility with older versions we keep the previous name as the identifier in the config.

Actions
*******

Braze supports tracking of action events. The actual value sent to Braze is configured through template with the key :code:`action`.

Views
*****

Braze does not support view events.

Purchases
*********

Braze supports tracking of purchase events. Purchase events cannot be configured (besides enabling/disabling the whole event) and
always the track the product id, currency code and price.

Attributes
**********

Braze supports storing attributes per user. The name of the attribute can be configured through the :code:`name` template.

Event parameters
****************

Braze does not support sending custom parameters.

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
