######
Search
######

.. toctree::
  :hidden:

Calls to search are used to retrieve the search results from issue content of an App.

URL
===

[POST] https://purplemanager.com/delivery/search

Request Parameters
==================

.. role:: fg-green
.. role:: fg-red

===================== ============================= ======================================================================= ====================================
Name                  Type                          Description                                                             Required
===================== ============================= ======================================================================= ====================================
appId                 String                        The id of the requesting app                                            :fg-green:`YES`
platform              String (android/ios/kindle)   Platform of the device                                                  :fg-green:`YES`
preview               Boolean (true/false)          Is the requesting app a test (true) or production (false) app           :fg-red:`NO`, defaults to false
locale                String                        Language locale like de_DE or en_US                                     :fg-green:`YES`
model                 String                        Model identifier like iPhone 4S, some kind of model number (iOS only)   :fg-red:`NO`
smallestScreenWidthDp Integer                       Density-Independent Pixels of the smallest screen width (Android only)  :fg-red:`NO`
===================== ============================= ======================================================================= ====================================

.. note:: The paramters :code:`model` and :code:`smallestScreenWidthDp` are used to filter the results by device class (phone / tablet). If they are omitted all
          results will be returned even if the containing issue is not shown on the requesting device.

Request Body
============

===================== ============================= ======================================================================================= ====================================
Name                  Type                          Description                                                                             Required
===================== ============================= ======================================================================================= ====================================
issueIds              List<String>                  when content search is active limit search to issues with given ids                     :fg-red:`NO`, defaults to no limit
publicationIds        List<String>                  when content search is active limit search to issues from publications with given ids   :fg-red:`NO`, defaults to no limit
phrase                String                        the search phrase                                                                       :fg-green:`YES`
fuzzy                 Boolean (true/false)          use a fuzzy search                                                                      :fg-red:`NO`, defaults to false
sortPages             Boolean (true/false)          sort the search hits by pages of the issues                                             :fg-red:`NO`, defaults to false
findAll               Boolean (true/false)          find all words of the search phrase (any word otherwise)                                :fg-red:`NO`, defaults to false
===================== ============================= ======================================================================================= ====================================

.. code-block:: json

  {
    "issueIds": ["xxx"],
    "publicationIds": ["xxx"],
    "phrase": "xxx",
    "fuzzy": true,
    "sortPages": true,
    "findAll": true
  }

Request Headers
===============

=============== ================= ========================================================================================================================= ==================
Name            Type                 Content                                                                                                                Required
=============== ================= ========================================================================================================================= ==================
Authorization   String            :code:`Token <authToken>` results from entitled issues are only returned if the authToken grants access to these issues   :fg-red:`NO`
Content-Type    String            :code:`application/json`                                                                                                  :fg-green:`YES`
=============== ================= ========================================================================================================================= ==================

Response Codes
==============

=========================== =========================
Http Status Code            Reason
=========================== =========================
200 - OK
=========================== =========================

Response Headers
================

=============== ========= ======================================
Name            Type      Content
=============== ========= ======================================
Content-Type    String    :code:`application/json;charset=UTF-8`
Content-Length  int       Length of json
=============== ========= ======================================

Response Body
=============

A JSON Response is returned.

.. code-block:: json

  {
    "numberOfIssueHits": 1,
    "numberOfPageHits": 2,
    "issues": [
        {
            "issueId": "xxx",
            "publicationId": "xxx",
            "pages": [
                {
                    "pageIndex": 0,
                    "pageNumber": 1,
                    "pageLabel": "1",
                    "pageTitle": "",
                    "excerpt": "... <strong>xxx/strong> ..."
                },
                {
                    "pageIndex": 5,
                    "pageNumber": 6,
                    "pageLabel": "10",
                    "pageTitle": "",
                    "excerpt": "... <strong>xxx/strong> ..."
                }
            ]
        }
    ]
  }
