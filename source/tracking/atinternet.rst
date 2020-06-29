###########
AT Internet
###########

.. versionadded:: 5.2

|AT Internet| is a tracking service which supports tracking events (actions and views).

.. |AT Internet| raw:: html

   <a href="https://www.atinternet.com/" target="_blank">AT Internet</a>

Events
######

Overview
********

+-----------------------+------------------------+-----------------------+------------------------+-----------------------+
| Key-Name in Config    | Action Templates       | View Templates        | Purchase Templates     | Attribute Templates   |
+=======================+========================+=======================+========================+=======================+
| atinternet            | - :code:`name`         | - :code:`name`        |                        |                       |
|                       | - :code:`chapter1`     | - :code:`chapter1`    | :fg-red:`unsupported`  | :fg-red:`unsupported` |
|                       | - :code:`chapter2`     | - :code:`chapter2`    |                        |                       |
|                       | - :code:`chapter3`     | - :code:`chapter3`    |                        |                       |
|                       | - :code:`level2`       | - :code:`level2`      |                        |                       |
|                       | - :code:`action`       |                       |                        |                       |
+-----------------------+------------------------+-----------------------+------------------------+-----------------------+

Actions
*******

AT Internet supports tracking of action events. With AT Internet, each action is
tracked as a |Gesture event|.

.. |Gesture event| raw:: html

   <a href="https://developers.atinternet-solutions.com/android-en/content-android-en/gestures-android-en-2-3-0/" target="_blank">Gesture event</a>

For each event, the properties of the Gesture event can be configured via separate
templates: :code:`name`, :code:`chapter1`, :code:`chapter2`, :code:`chapter3`
and :code:`level2`.

.. note::

  The :code:`level2` template must evaluate to a valid integer value.

Each Gesture event can have a different :code:`action`. This is configured with
the corresponding :code:`action` template.
The values need to be one of:

- :code:`touch`
- :code:`navigation`
- :code:`download`
- :code:`exit`
- :code:`search`

If no :code:`action` or an invalid value was provided, the event will be sent
as a :code:`touch` event.

On the web platform, gestures are always sent as :code:`click` events.

Views
*****

AT Internet supports tracking of view events. With AT Internet, each view is
tracked as a |Screen event|.

.. |Screen event| raw:: html

   <a href="https://developers.atinternet-solutions.com/android-en/content-android-en/screens-android-en-2-3-0/" target="_blank">Gesture event</a>

For each event, the properties of the Screen event can be configured via separate
templates: :code:`name`, :code:`chapter1`, :code:`chapter2`, :code:`chapter3`
and :code:`level2`.

.. note::

  The :code:`level2` template must evaluate to a valid integer value.

Purchases
*********

AT Internet does not support tracking of purchases.

Attributes
**********

AT Internet does not support storing attributes per user.

Event parameters
****************

AT Internet does support sending custom parameters for actions.

Configuration Example
#####################

.. code-block:: json

  {
    "atinternet": {
      "events": {
        "APP_BOOKMARK_ADDED": {
          "enabled": true,
          "templates": {
            "name": "Bookmark added",
            "chapter1": "{{BOOKMARK_TITLE}}",
            "chapter2": "Chapter 2",
            "chapter3": "Chapter 3",
            "level2": "2",
            "action": "touch"
          }
        }
      },
      "views": {
        "PRESENTER_PAGE": {
          "enabled": true,
          "templates": {
            "name": "{{CONTENT_NAME}}",
            "chapter1": "{{PAGE_LABEL}}",
            "chapter2": "Chapter 2",
            "chapter3": "Chapter 3",
            "level2": "3"
          }
        }
      },
      "attributes": {
      }
    }
  }
