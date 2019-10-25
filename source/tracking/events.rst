Actions
*******

.. versioned-toggle-box:: APP_BOOKMARK_ADDED
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A bookmark was added by the user.

  +--------------------------+--------------------------------------------------------------------------------------------+
  | Template placeholder     | Example values                                                                             |
  +==========================+============================================================================================+
  | :code:`CONTENT_ID`       | :code:`<PUBLICATION_ID>/<ISSUE_ID>`                                                        |
  +--------------------------+--------------------------------------------------------------------------------------------+
  | :code:`CONTENT_NAME`     | :code:`displayName` (Name) of the Issue                                                    |
  +--------------------------+--------------------------------------------------------------------------------------------+
  | :code:`BOOKMARK_TITLE`   | Issues: same as :code:`CONTENT_NAME`,  Articles: :code:`displayName` (Name) of Publication |
  +--------------------------+--------------------------------------------------------------------------------------------+
  | :code:`BOOKMARK_SECTION` | Issues: Section of the ToC, Articles: :code:`displayName` (Name) of Issue                  |
  +--------------------------+--------------------------------------------------------------------------------------------+

.. versioned-toggle-box:: APP_BOOKMARK_DELETED
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A bookmark was deleted by the user.

  +--------------------------+--------------------------------------------------------------------------------------------+
  | Template placeholder     | Example values                                                                             |
  +==========================+============================================================================================+
  | :code:`CONTENT_ID`       | :code:`<PUBLICATION_ID>/<ISSUE_ID>`                                                        |
  +--------------------------+--------------------------------------------------------------------------------------------+
  | :code:`CONTENT_NAME`     | :code:`displayName` (Name) of the Issue                                                    |
  +--------------------------+--------------------------------------------------------------------------------------------+
  | :code:`BOOKMARK_TITLE`   | Issues: same as :code:`CONTENT_NAME`,  Articles: :code:`displayName` (Name) of Publication |
  +--------------------------+--------------------------------------------------------------------------------------------+
  | :code:`BOOKMARK_SECTION` | Issues: Section of the ToC, Articles: :code:`displayName` (Name) of Issue                  |
  +--------------------------+--------------------------------------------------------------------------------------------+

.. versioned-toggle-box:: APP_START
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-kiosk: 3.2.2

  The app has been started.

  This event has no template placeholders.

.. versioned-toggle-box:: APP_STOP
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-kiosk: 3.2.2

  The app has been stopped.

  This event has no template placeholders.

.. versioned-toggle-box:: APP_FOREGROUND
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The app has been resumed, e.g. through the recent tasks.

  This event has no template placeholders.

.. versioned-toggle-box:: APP_BACKGROUND
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The app has been minimized, e.g. using the home button.

  This event has no template placeholders.

.. versioned-toggle-box:: APP_SHARED
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.5.0

  The app has been shared.

  This event has no template placeholders.

.. versioned-toggle-box:: APP_CONTENT_SHARED
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.5.0

  The user has shared the currently visible content.

  +---------------------------+------------------------------------------------------+
  | Template placeholder      | Example values                                       |
  +===========================+======================================================+
  | :code:`CONTENT_ID`        | The content id of the shared content.                |
  +---------------------------+------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the shared content, e.g. the issue name. |
  +---------------------------+------------------------------------------------------+

.. versioned-toggle-box:: KIOSK_PROMOTION_OPEN_ACTION
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  An url has been opened from the promotion area in the kiosk.

  +--------------------------+---------------------------------------------------+
  | Template placeholder     | Example values                                    |
  +==========================+===================================================+
  | :code:`ACTION_URL`       | The url which has been opened.                    |
  +--------------------------+---------------------------------------------------+

.. versioned-toggle-box:: KIOSK_PUBLICATION_OPENED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.5.0
  :versionadded-web-kiosk: 3.2.2

  A publication has been selected in the publication filter menu in the kiosk.

  +--------------------------+---------------------------------------------------+
  | Template placeholder     | Example values                                    |
  +==========================+===================================================+
  | :code:`PUBLICATION_ID`   | The id of the publication.                        |
  +--------------------------+---------------------------------------------------+
  | :code:`PUBLICATION_NAME` | The name of the publication.                      |
  +--------------------------+---------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_CHANNEL_OPENED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A channel has been selected in the channel pager.

  +--------------------------+---------------------------------------------------+
  | Template placeholder     | Example values                                    |
  +==========================+===================================================+
  | :code:`PUBLICATION_ID`   | The id of the publication.                        |
  +--------------------------+---------------------------------------------------+
  | :code:`PUBLICATION_NAME` | The name of the publication.                      |
  +--------------------------+---------------------------------------------------+


.. versioned-toggle-box:: KIOSK_COUPON_ACTIVATED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A coupon code has been activated.

  +--------------------------+---------------------------------------------------+
  | Template placeholder     | Example values                                    |
  +==========================+===================================================+
  | :code:`COUPON_CODE`      | The coupon code which has been activated.         |
  +--------------------------+---------------------------------------------------+

  .. warning::

    This event has been renamed to :code:`KIOSK_SUBSCRIPTION_CODE_ACTIVATED`
    in version 2.3.
    All configurations have to be manually adjusted to use the new event name.

.. versioned-toggle-box:: KIOSK_COUPON_DEACTIVATED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A coupon code has been deactivated.

  +--------------------------+---------------------------------------------------+
  | Template placeholder     | Example values                                    |
  +==========================+===================================================+
  | :code:`COUPON_CODE`      | The coupon code which has been deactivated.       |
  +--------------------------+---------------------------------------------------+

  .. warning::

    This event has been renamed to :code:`KIOSK_SUBSCRIPTION_CODE_DEACTIVATED`
    in version 2.3.
    All configurations have to be manually adjusted to use the new event name.

.. versioned-toggle-box:: KIOSK_SUBSCRIPTION_CODE_ACTIVATED
  :color: purple
  :versionadded-android: 2.3.0
  :versionadded-ios: 2.3.0
  :versionadded-web-kiosk: 3.2.2

  A subscription code has been activated.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`SUBSCRIPTION_CODE` | The coupon code which has been activated.       |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_SUBSCRIPTION_CODE_DEACTIVATED
  :color: purple
  :versionadded-android: 2.3.0
  :versionadded-ios: 2.3.0
  :versionadded-web-kiosk: 3.2.2

  A subscription code has been deactivated.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`SUBSCRIPTION_CODE` | The coupon code which has been deactivated.     |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_ISSUE_DELETED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  An issue has been deleted.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_DOWNLOAD_STARTED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0

  An issue download has been started.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_DOWNLOAD_CANCELLED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0

  An issue download has been cancelled.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_DOWNLOAD_FAILED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0

  An issue download has failed.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_DOWNLOADED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  An issue has been downloaded.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_PREVIEW_DOWNLOADED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A preview issue has been downloaded.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_OPENED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-kiosk: 3.2.2

  An issue has been opened.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.


.. versioned-toggle-box:: KIOSK_ISSUE_OPEN_FAILED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: ?.?.?
  :versionadded-web-kiosk: 3.2.2

  An issue could not be opened. This can happen if the user tried to open an issue
  though a deep-link / action-url which is not available in the kiosk.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_ISSUE_PREVIEW_OPENED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A preview issue has been opened.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_PURCHASE_CANCELLED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  An issue purchase has been cancelled/aborted.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`PRODUCT_ID`        | The product id of the issue.                    |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_PURCHASED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  An issue has been purchase.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`PRODUCT_ID`        | The product id of the issue.                    |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_TOC_OPENED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The table of contents of an issue have been opened in the issue preview screen.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_ISSUE_PREVIEW_TOC_OPENED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The table of contents of a preview issue have been opened in the issue preview screen.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_PURCHASES_RESTORED
  :color: purple
  :versionadded-ios: 2.1.0

  The in-app purchases have been manually restored.

  This event has no template placeholders.

  .. warning:: This events is not available on Android as purchases are restored automatically after each kiosk sync.

.. versioned-toggle-box:: KIOSK_PURCHASE_RESTORATION_FAILED
  :color: purple
  :versionadded-ios: 2.1.0

  The in-app purchases could not be restored.

  This event has no template placeholders.

  .. warning:: This events is not available on Android as purchases are restored automatically after each kiosk sync.

.. versioned-toggle-box:: KIOSK_SUBSCRIPTION_PURCHASE_CANCELLED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A subscription purchase has been cancelled/aborted.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`SUBSCRIPTION_ID`   | The id of the subscription.                     |
  +---------------------------+-------------------------------------------------+
  | :code:`SUBSCRIPTION_NAME` | The name of the subscription.                   |
  +---------------------------+-------------------------------------------------+
  | :code:`PRODUCT_ID`        | The product id of the subscription.             |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the subscription.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_SUBSCRIPTION_PURCHASED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A subscription has been purchased.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`SUBSCRIPTION_ID`   | The id of the subscription.                     |
  +---------------------------+-------------------------------------------------+
  | :code:`SUBSCRIPTION_NAME` | The name of the subscription.                   |
  +---------------------------+-------------------------------------------------+
  | :code:`PRODUCT_ID`        | The product id of the subscription.             |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the subscription.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_MENU_ENTITLEMENT_LOGIN_SUCCEEDED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0
  :versionadded-web-kiosk: 3.2.2

  This event will be tracked if the entitlement login was successful.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`USERNAME`          | The username used to login.                     |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_MENU_ENTITLEMENT_LOGIN_FAILED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0
  :versionadded-web-kiosk: 3.2.2

  This event will be tracked if the entitlement login has failed.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`USERNAME`          | The username used to login.                     |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_ENTITLEMENT_LINK1_OPENED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0

  This event will be tracked if the first entitlement link was opened.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`LABEL`             | The displayed text of the link.                 |
  +---------------------------+-------------------------------------------------+
  | :code:`URL`               | The actual url of the link.                     |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_ENTITLEMENT_LINK2_OPENED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0

  This event will be tracked if the second entitlement link was opened.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`LABEL`             | The displayed text of the link.                 |
  +---------------------------+-------------------------------------------------+
  | :code:`URL`               | The actual url of the link.                     |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_ENTITLEMENT_LINK3_OPENED
  :color: purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0

  This event will be tracked if the third entitlement link was opened.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`LABEL`             | The displayed text of the link.                 |
  +---------------------------+-------------------------------------------------+
  | :code:`URL`               | The actual url of the link.                     |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: PRESENTER_CONTENT_TOC_OPENED
  :color: dark-purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-player: 3.1.0

  The user has opened the table of contents of the currently visible content.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+

.. versioned-toggle-box:: PRESENTER_CONTENT_PREVIEW_TOC_OPENED
  :color: dark-purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-player: 3.1.0

  The user has opened the table of contents of the currently visible preview content.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+

.. versioned-toggle-box:: PRESENTER_CHANNEL_CONTENT_OPENED
  :color: dark-purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.5.0

  The user has opened an article. This event will be triggered after 3 seconds of viewing the content.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+

.. versioned-toggle-box:: PRESENTER_ISSUE_CONTENT_OPENED
  :color: dark-purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.5.0
  :versionadded-web-player: 3.1.0

  The user has opened an issue.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+

  Additionally you can use all custom properties which are configured for the issue.
  The name of the property is used as the placeholder key.


.. versioned-toggle-box:: PRESENTER_CONTENT_PAGE_OPENED
  :color: dark-purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.5.0
  :versionadded-web-player: 3.1.0

  The user has opened a page in the currently visible content.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_ID`           | The id of the page.                                   |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_ALIAS`        | The alias of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_LABEL`        | The label of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_INDEX`        | The index of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_NUMBER`       | The number of the page.                               |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_TITLE`        | The title of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_SECTION`      | The section of the page.                              |
  +---------------------------+-------------------------------------------------------+

.. versioned-toggle-box:: PRESENTER_CONTENT_OPEN_FAILED
  :color: dark-purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0
  :versionadded-web-player: 3.1.0

  This event will be tracked if an issue can not be opened, e.g. when its contents are corrupt / invalid.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+

.. versioned-toggle-box:: PRESENTER_CONTENT_URL_OPENED
  :color: dark-purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0
  :versionadded-web-player: 3.1.0

  This event will be tracked if a link has been opened from within an issue.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`URL`               | The opened url.                                       |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_ID`           | The id of the page.                                   |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_ALIAS`        | The alias of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_LABEL`        | The label of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_INDEX`        | The index of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_NUMBER`       | The number of the page.                               |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_TITLE`        | The title of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_SECTION`      | The section of the page.                              |
  +---------------------------+-------------------------------------------------------+

|

Views
*****

.. versioned-toggle-box:: APP_BOOKMARKS
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The bookmarks screen is currently visible.

  This event has no template placeholders.

.. versioned-toggle-box:: APP_SHARING
  :color: blue
  :versionadded-ios: 2.1.0

  The bookmarks screen is currently visible.

  This event has no template placeholders.

  .. warning:: This event is not available on Android.

.. versioned-toggle-box:: APP_MENU
  :color: blue
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The app menu is currently visible.

  This event has no template placeholders.

.. versioned-toggle-box:: KIOSK
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-kiosk: 3.2.2

  The kiosk is currently visible.

  This event has no template placeholders.

.. versioned-toggle-box:: KIOSK_CHANNEL_FEED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A channel in the channel feed is currently visible.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`PUBLICATION_ID`    | The id of the channel.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the channel.                        |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_MY_ISSUES
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The my issues filter in the kiosk filter is active.

  This event has no template placeholders.

.. versioned-toggle-box:: KIOSK_PUBLICATION_ALL
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The all issues filter in the kiosk filter is active.

  This event has no template placeholders.

.. versioned-toggle-box:: KIOSK_PUBLICATION
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0
  :versionadded-web-kiosk: 3.2.2

  A specific publication in the kiosk filter is active.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`PUBLICATION_ID`    | The id of the channel.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the channel.                        |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_MANAGE_SUBSCRIPTIONS
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The subscription management screen is visible.

  This event has no template placeholders.

.. versioned-toggle-box:: KIOSK_ISSUE_PURCHASE
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The purchase screen of an issue is visible.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: KIOSK_ISSUE_PREVIEW
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  The preview screen of an issue is visible.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+

.. versioned-toggle-box:: PRESENTER_PAGE
  :color: dark-purple
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0
  :versionadded-web-player: 3.1.0

  This event tracks the currently visible page in the content. Only real pages can be tracked
  using this event. Large pages which are scrollable and have the paging enabled are still only
  tracked as one page.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_ID`           | The id of the page.                                   |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_ALIAS`        | The alias of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_LABEL`        | The label of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_INDEX`        | The index of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_NUMBER`       | The number of the page.                               |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_TITLE`        | The title of the page.                                |
  +---------------------------+-------------------------------------------------------+
  | :code:`PAGE_SECTION`      | The section of the page.                              |
  +---------------------------+-------------------------------------------------------+

.. versioned-toggle-box:: PRESENTER_CONTENT
  :color: dark-purple
  :versionadded-android: 2.2.0
  :versionadded-ios: 2.1.0
  :versionadded-web-player: 3.1.0

  An issue is visible.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: PRESENTER_CONTENT_TOC
  :color: dark-purple
  :versionadded-android: 2.2.0
  :versionadded-ios: 2.1.0
  :versionadded-web-player: 3.1.0

  The table of contents of an issue is visible.

  +---------------------------+-------------------------------------------------------+
  | Template placeholder      | Example values                                        |
  +===========================+=======================================================+
  | :code:`CONTENT_ID`        | The content id of the current content.                |
  +---------------------------+-------------------------------------------------------+
  | :code:`CONTENT_NAME`      | The name of the current content, e.g. the issue name. |
  +---------------------------+-------------------------------------------------------+

|

Purchases
*********

.. versioned-toggle-box:: KIOSK_ISSUE_PURCHASED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  An issue has been purchase.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`PRODUCT_ID`        | The product id of the issue.                    |
  +---------------------------+-------------------------------------------------+
  | :code:`PRICE`             | The price of the purchase.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`CURRENCY_CODE`     | The currency code of the price.                 |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_ID`          | The id of the issue.                            |
  +---------------------------+-------------------------------------------------+
  | :code:`ISSUE_NAME`        | The name of the issue.                          |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_ID`    | The id of the publication.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`PUBLICATION_NAME`  | The name of the publication.                    |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the publication and issue.
  The name of the property is used as the placeholder key.

.. versioned-toggle-box:: KIOSK_SUBSCRIPTION_PURCHASED
  :color: purple
  :versionadded-android: 2.1.0
  :versionadded-ios: 2.1.0

  A subscription has been purchased.

  +---------------------------+-------------------------------------------------+
  | Template placeholder      | Example values                                  |
  +===========================+=================================================+
  | :code:`PRODUCT_ID`        | The product id of the issue.                    |
  +---------------------------+-------------------------------------------------+
  | :code:`PRICE`             | The price of the purchase.                      |
  +---------------------------+-------------------------------------------------+
  | :code:`CURRENCY_CODE`     | The currency code of the price.                 |
  +---------------------------+-------------------------------------------------+
  | :code:`SUBSCRIPTION_ID`   | The id of the subscription.                     |
  +---------------------------+-------------------------------------------------+
  | :code:`SUBSCRIPTION_NAME` | The name of the subscription.                   |
  +---------------------------+-------------------------------------------------+

  Additionally you can use all custom properties which are configured for the subscription.
  The name of the property is used as the placeholder key.

|

Attributes
**********

.. versioned-toggle-box:: HAS_ACTIVE_SUBSCRIPTION
  :color: green
  :versionadded-android: 2.0.0
  :versionadded-ios: 2.0.0

  This attribute has a value of :code:`true` if the user has an active subscription, otherwise it has the value :code:`false`.

  This event has no template placeholders.

.. versioned-toggle-box:: HAS_ACTIVE_COUPON_CODE
  :color: green
  :versionadded-android: 2.0.0
  :versionadded-ios: 2.0.0

  This attribute has a value of :code:`true` if the user has an active coupon code, otherwise it has the value :code:`false`.

  This event has no template placeholders.

  |

  .. warning::

    This attribute has been renamed to :code:`HAS_ACTIVE_SUBSCRIPTION_CODE`
    in version 2.3.
    All configurations have to be manually adjusted to use the new event name.

.. versioned-toggle-box:: HAS_ACTIVE_SUBSCRIPTION_CODE
  :color: green
  :versionadded-android: 2.3.0
  :versionadded-ios: 2.3.0

  This attribute has a value of :code:`true` if the user has an active subscription code, otherwise it has the value :code:`false`.

  This event has no template placeholders.

.. versioned-toggle-box:: HAS_ACTIVE_TRIAL
  :color: green
  :versionadded-android: 2.0.0
  :versionadded-ios: 2.0.0

  This attribute has a value of :code:`true` if the user has an active trial, otherwise it has the value :code:`false`.

  This event has no template placeholders.

.. versioned-toggle-box:: HAS_PURCHASED_ISSUE
  :color: green
  :versionadded-android: 2.0.0
  :versionadded-ios: 2.0.0

  This attribute has a value of :code:`true` if the user has purchased at least one issue, otherwise it has the value :code:`false`.

  This event has no template placeholders.

.. versioned-toggle-box:: HAS_BOOKMARKS
  :color: green
  :versionadded-android: 2.0.0
  :versionadded-ios: 2.0.0

  This attribute has a value of :code:`true` if the user has at least one bookmark, otherwise it has the value :code:`false`.

  This event has no template placeholders.

.. versioned-toggle-box:: HAS_ENTITLEMENT_LOGIN
  :color: green
  :versionadded-android: 2.5.0
  :versionadded-ios: 2.5.0

  Is :code:`true` if the user has logged in via entitlement.
  While the user is logged in the attribute value remains :code:`true`.
  If the user logs out the attribute value is reset to :code:`false`.

  This event has no template placeholders.
