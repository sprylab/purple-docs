###
IVW
###

.. versionadded:: 2.2.0

|IVW| is a tracking service which supports tracking actions (views).

.. |IVW| raw:: html

   <a href="http://www.ivw.de/" target="_blank">IVW</a>

Events
######

Overview
********

+-----------------------+------------------------+-----------------------+------------------------+-----------------------+
| Key-Name in Config    | Action Templates       | View Templates        | Purchase Templates     | Attribute Templates   |
+=======================+========================+=======================+========================+=======================+
|                       |                        | - :code:`category`    |                        |                       |
| ivw                   | :fg-red:`unsupported`  | - :code:`comment`     | :fg-red:`unsupported`  | :fg-red:`unsupported` |
|                       |                        |                       |                        |                       |
+-----------------------+------------------------+-----------------------+------------------------+-----------------------+

Actions
*******

IVW does not support action events.

Views
*****

IVW supports tracking of view events. The actual values sent to IVW is
configured through :code:`category` and :code:`comment` templates.

Purchases
*********

IVW does not support purchase events.

Attributes
**********

IVW does not support storing attributes per user.

Event parameters
****************

IVW does not support sending custom parameters.

Configuration Example
#####################

.. code-block:: json

  {
    "ivw": {
      "viewsEnabledByDefault": false,
      "views": {
        "APP_BOOKMARKS": {
          "enabled": true,
          "templates": {
            "category": "<IVW Code>",
            "comment": "Bookmark added"
          }
        }
      }
    }
  }
