########
Tracking
########

.. _apps-tracking:

Overview
########

Purple DS apps support tracking via several different tracking services. There are three different types of events:

#. Actions
#. Views
#. Purchases

Additionally, if the tracking service supports this, there are several attributes which describe the state of the app / usage by a user.

Tracking Services
#################

Currently Purple DS apps support several different tracking services.

.. warning::

  Not all tracking services support all event types. See the linked pages below for
  detailed information about the supported event types of each tracking service.


- :doc:`Adjust <tracking/adjust>`
- :doc:`Adobe Analytics <tracking/adobe>`
- :doc:`Amazon Pinpoint <tracking/pinpoint>`
- :doc:`AT Internet <tracking/atinternet>`
- :doc:`Braze (Appboy) <tracking/appboy>`
- :doc:`Facebook <tracking/facebook>`
- :doc:`Firebase Analytics <tracking/firebase_analytics>`
- :doc:`Flurry <tracking/flurry>`
- :doc:`Google Analytics <tracking/google_analytics>`
- :doc:`IVW <tracking/ivw>`

.. toctree::
  :hidden:

  tracking/adjust
  tracking/adobe
  tracking/atinternet
  tracking/appboy
  tracking/facebook
  tracking/firebase_analytics
  tracking/flurry
  tracking/google_analytics
  tracking/ivw
  tracking/pinpoint


Configuration
#############

There are two sets of configurations:

- the default/base configuration, included in the Purple Kit. See https://redmine.purplepublish.com/issues/5094 for the latest version.
- the app configuration, included in the dynamic resources

The app configuration is merged with the "default" configuration. This means
that every entry in the app configuration overrides the value in the default configuration.

This allows to have standard configurations for all events which can be overridden for each tracking service.

For this purpose a new JSON file `tracking_config.json` is used in the dynamic resources.
This configuration makes it possible to map internal event names to custom event names.

The JSON is structured as follows:

.. toggle-box:: tracking_config.json

  .. code-block:: json

    {
      "default": {
        "eventsEnabledByDefault": false,
        "viewsEnabledByDefault": false,
        "purchasesEnabledByDefault": false,
        "attributesEnabledByDefault": false,
        "events": {
          "<internal_event_key>": {
            "enabled": false,
            "templates": {
              "<template_name>": "<Text to send to tracking service>"
            },
            "parameters": {
              "paramKey1": "paramValue1"
            }
          }
        },
        "views": {
        },
        "purchases": {
        },
        "attributes": {
        }
      },
      "<tracking_service_name>": {
        "eventsEnabledByDefault": false,
        "viewsEnabledByDefault": false,
        "purchasesEnabledByDefault": false,
        "attributesEnabledByDefault": false,
        "events": {
          "<internal_event_key>": {
            "enabled": false,
            "templates": {
              "<template_name>": "<Text to send to tracking service>"
            }
          }
        },
        "views": {
        },
        "purchases": {
        },
        "attributes": {
        }
      },
    }

Each event has the following configuration options:

enabled
*******

Each event can be selectively enabled or disabled.

templates
*********

Each event has templates. They are used to configure the tracking services, e.g.
Google Analytics has three templates for action events: "category", "action" and "label".
The names map to the API of the tracking service. Each tracking service supports different
templates.

The templates can contain placeholders. They can be referenced in the config by
using the following syntax: :code:`{{PLACEHOLDER_NAME}}`, e.g. :code:`{{ISSUE_ID}}`.

A list of all available placeholders can be found :doc:`here <tracking/events>`.

parameters
**********

Additional parameters (key-value pairs) can be send with each event if the tracking
service supports this.
Every key will be included in the event. The values can contain all placeholders
supported for the event and will be evaluated (see above) when sending the event to the service.

Events
######

A current list of all available events, parameters and default values can be found :doc:`here <tracking/events>`.

.. toctree::
  :hidden:

  tracking/events
