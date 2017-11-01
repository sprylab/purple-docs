###############
Amazon Pinpoint
###############

.. versionadded:: 3.6.0

|AmazonPinpoint| is a tracking service which supports tracking events (actions and purchases)
and storing user attributes.

.. |AmazonPinpoint| raw:: html

   <a href="https://aws.amazon.com/pinpoint/" target="_blank">Amazon Pinpoint</a>

Events
######

Overview
********

+-----------------------+------------------------+-----------------------+------------------------+-----------------------+
| Key-Name in Config    | Action Templates       | View Templates        | Purchase Templates     | Attribute Templates   |
+=======================+========================+=======================+========================+=======================+
|                       |                        |                       |                        |                       |
| pinpoint              | :code:`action`         | :fg-red:`unsupported` | :fg-red:`unsupported`  | :code:`name`          |
|                       |                        |                       |                        |                       |
+-----------------------+------------------------+-----------------------+------------------------+-----------------------+

Actions
*******

Amazon Pinpoint supports tracking of action events. The actual value sent to
Amazon Pinpoint is configured through a template with the key :code:`action`.

.. note::

  Event names can only be 50 characters long and will be truncated if they exceed
  this limit.

Views
*****

Amazon Pinpoint does not support view events.

Purchases
*********

Amazon Pinpoint supports tracking of purchase events. Purchase events cannot
be configured (besides enabling/disabling the whole event) and always track the
product id, currency code and price.

Attributes
**********

Amazon Pinpoint supports storing attributes per user. The name of the attribute can be
configured through the :code:`name` template.

Event parameters
****************

Amazon Pinpoint supports sending custom parameters for actions.

Configuration Example
#####################

.. code-block:: json
  :linenos:

  {
    "pinpoint": {
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
