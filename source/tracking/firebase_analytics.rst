##################
Firebase Analytics
##################

.. versionadded:: 3.10.0

|Firebase Analytics| is a tracking service which supports tracking events (actions, views and purchases)
and storing user attributes.

.. |Firebase Analytics| raw:: html

   <a href="https://firebase.google.com/docs/analytics/" target="_blank">Firebase Analytics</a>

Events
######

Overview
********

+-----------------------+------------------------+-----------------------+------------------------+-----------------------+
| Key-Name in Config    | Action Templates       | View Templates        | Purchase Templates     | Attribute Templates   |
+=======================+========================+=======================+========================+=======================+
|                       |                        |                       |                        |                       |
| firebase_analytics    | :code:`action`         | :code:`name`          | :fg-red:`unsupported`  | :code:`name`          |
|                       |                        |                       |                        |                       |
+-----------------------+------------------------+-----------------------+------------------------+-----------------------+

Actions
*******

Firebase Analytics supports tracking of action events. The actual value sent to
Firebase Analytics is configured through a template with the key :code:`action`.

.. hint::

  Event names must be under 40 characters and contain
  only alphanumeric characters or '_' and must start with an alphabetic character.

  The length of each parameter value can be no more than 100 characters.


Views
*****

Firebase Analytics supports tracking of view events. The view name send to
Firebase Analytics is configured through template with the key :code:`name`.


Purchases
*********

Firebase Analytics supports tracking of purchase events. Purchase events cannot
be configured (besides enabling/disabling the whole event) and always track the
product id, product name, currency an quantity.

Attributes
**********

Firebase Analytics supports storing attributes per user. The name of the attribute can be
configured through the :code:`name` template.

.. hint::

  Attribute names must be under 40 characters and contain only alphanumeric characters or '_' and must start with an alphabetic character.

  The length of each parameter value can be no more than 100 characters.

Event parameters
****************

Firebase Analytics supports sending custom parameters for actions.

.. hint::

  An event can have up to 25 parameters. This doesn't just mean for each call,
  but for all invocations that use that event name.

Configuration Example
#####################

.. code-block:: json
  :linenos:

  {
    "firebase_analytics": {
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
