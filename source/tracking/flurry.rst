######
Flurry
######

.. versionadded:: 2.1.0

|Flurry| is a tracking service which supports tracking events (actions).

.. |Flurry| raw:: html

   <a href="https://developer.yahoo.com/analytics/" target="_blank">Flurry</a>

Events
######

Overview
********

+-----------------------+------------------------+-----------------------+------------------------+-----------------------+
| Key-Name in Config    | Action Templates       | View Templates        | Purchase Templates     | Attribute Templates   |
+=======================+========================+=======================+========================+=======================+
|                       |                        |                       |                        |                       |
| flurry                | :code:`action`         | :fg-red:`unsupported` | :fg-red:`unsupported`  | :fg-red:`unsupported` |
|                       |                        |                       |                        |                       |
+-----------------------+------------------------+-----------------------+------------------------+-----------------------+

Actions
*******

Flurry supports tracking of action events. The actual value sent to Flurry is configured through template with the key :code:`action`.

Views
*****

Flurry does not support view events.

Purchases
*********

Flurry does not support purchase events.

Attributes
**********

Flurry does not support storing attributes per user.

Event parameters
****************

Flurry does not support sending custom parameters.

Configuration Example
#####################

.. code-block:: json

  {
    "flurry": {
      "eventsEnabledByDefault": false,
      "events": {
        "APP_BOOKMARK_ADDED": {
          "enabled": true,
          "templates": {
            "action": "Bookmark added"
          }
        }
      }
    }
  }
