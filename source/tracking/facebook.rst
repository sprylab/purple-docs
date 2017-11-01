########
Facebook
########

.. versionadded:: 2.1.0
.. versionchanged:: 3.5.0 Added support for action templates and parameters

|Facebook| is a tracking service which supports tracking events (actions and purchases).
It also supports tracking the installation of the app.

.. |Facebook| raw:: html

   <a href="https://developers.facebook.com/products/analytics" target="_blank">Facebook</a>

General
#######

For setting up the App in Facebook Analytics use the following information:

Android Class Name: :code:`com.sprylab.purple.android.app.purple.splash.SplashActivity`

Andriod Key Hash (Preview Apps): :code:`VnOtQRWs9tYehKQDf9SeALlqsxc=`

For Release Apps you need to create a hash from your release keystore. See the
|FacebookAndroidReleaseHash| for more information.

.. |FacebookAndroidReleaseHash| raw:: html

  <a href="https://developers.facebook.com/docs/android/getting-started/?locale=en_US#release-key-hash" target="_blank">official Facebook documentation</a>

Events
######

Overview
********

+-----------------------+------------------------+-----------------------+------------------------+-----------------------+
| Key-Name in Config    | Action Templates       | View Templates        | Purchase Templates     | Attribute Templates   |
+=======================+========================+=======================+========================+=======================+
|                       |                        |                       |                        |                       |
| facebook              | :code:`action`         | :fg-red:`unsupported` | :fg-red:`unsupported`  | :fg-red:`unsupported` |
|                       |                        |                       |                        |                       |
+-----------------------+------------------------+-----------------------+------------------------+-----------------------+

Actions
*******

Facebook supports tracking of action events. The actual value sent to Facebook is
configured through a template with the key :code:`action`.

.. hint::

  Event names and parameter names length must be under 40 characters and contain
  only alphanumeric characters, '_', '-' or spaces, and cannot start with a space
  or hyphen.

  For more information please see the |FacebookFAQAppEvents|.

  .. |FacebookFAQAppEvents| raw:: html

   <a href="https://developers.facebook.com/docs/app-events/faq/?locale=en_US#faq_1705672466316587" target="_blank">official Facebook documentation</a>

Views
*****

Facebook does not support view events.

Purchases
*********

Facebook supports tracking of purchase events. Purchase events only send the price
and currency for the purchase. The product id can be sent with custom parameters.

.. warning::

  "Log In-App Purchase Events Automatically on iOS" setting should be disabled
  otherwise in-app purchases logging will be duplicated.

  To disable the setting follow the steps below:

  1. Go to My Apps.
  2. Select your app.
  3. Click on the settings tab on the left nav.
  4. Find the section labeled iOS.
  5. Disable the switch called "Automatically Log In-App Purchase Events on iOS".

  For more information please see the |FacebookFAQAppEventsPurchases|.

  .. |FacebookFAQAppEventsPurchases| raw:: html

   <a href="https://developers.facebook.com/docs/app-events/faq/?locale=en_US#auto_in_app_purchase" target="_blank">official Facebook documentation</a>

Attributes
**********

Facebook does not support storing attributes per user.

Event parameters
****************

Facebook supports sending custom parameters for actions and purchases.

.. hint::

  An event can have up to 25 parameters. This doesn't just mean for each call,
  but for all invocations that use that event name.

  If you need to remove obsolete parameters - you can deactivate parameters by
  following the instructions in the Facebook help center.

  The length of each parameter value can be no more than 100 characters.

  For more information please see the |FacebookFAQAppEventsParameters|.

  .. |FacebookFAQAppEventsParameters| raw:: html

   <a href="https://developers.facebook.com/docs/app-events/faq/?locale=en_US#faq_1753207134925965" target="_blank">official Facebook documentation</a>


Configuration Example
#####################

.. code-block:: json
  :linenos:

  {
    "facebook": {
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
      "purchases": {
        "KIOSK_ISSUE_PURCHASED": {
          "templates": {
            "action": "Issue purchased {{ISSUE_ID}}"
          },
          "parameters": {
            "product": "{{PRODUCT_ID}}",
            "issue.id": "{{ISSUE_ID}}"
          }
        }
      }
    }
  }
