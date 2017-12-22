#########################
Standard Entitlement (V2)
#########################

A Standard Entitlement Server in Version 2 provides an HTTP REST interface with 5 methods to login, renew the session token,
retrieve a list of issues, verify access to a single issue and logout.
It is configured with the URL.

API Description
###############

1. Login
========

By logging in, users obtain a session token that is required for all subsequent API calls.

Request
*******

POST :code:`/user/login`

============== =================================
Request header Value
============== =================================
Content-Type   application/x-www-form-urlencoded
============== =================================

Parameters (Request body)
-------------------------

======== =====================================================================
Name     Description
======== =====================================================================
username urlencoded username
password urlencoded password
appId    the bundle identifier / package name of the app or a configured value
deviceId the unique device id of the calling device
======== =====================================================================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/user/login' -H 'content-type: application/x-www-form-urlencoded'\
   -d 'username=testuser%40example.com&password=1234&appId=com.domain.myapp&deviceId=6789-1234-1234-123-123456'

Response
********

In case of success, the answer is a string representing the session token that is to be used for all further API calls.

================ ========================
HTTP Status code Response body
================ ========================
200 OK           the authentication token
================ ========================

Sample response body
--------------------

.. code-block:: none

  2ef9f161-46e1-90a1-7ed6-658256124b4c

Error response
--------------

================ ================= ====================================
HTTP Status code Response body     Description
================ ================= ====================================
403 Forbidden    WRONG_CREDENTIALS username and/or password incorrect
403 Forbidden    USER_DEACTIVATED  user is deactivated
================ ================= ====================================

Sample error response body
--------------------------

.. code-block:: none

  WRONG_CREDENTIALS

2. Token renewal
================

By renewing the token, users obtain an updated session token required for all subsequent API calls.

Request
*******

POST :code:`/token/renew`

============== =================================
Request header Value
============== =================================
Content-Type   application/x-www-form-urlencoded
============== =================================

Parameters (Request body)
-------------------------

======== =====================================================================
Name     Description
======== =====================================================================
token    the token retrieved by login or a prior renew
appId    the bundle identifier / package name of the app or a configured value
deviceId the unique device id of the calling device
======== =====================================================================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/token/renew' -H 'content-type: application/x-www-form-urlencoded'\
   -d 'token=2ef9f161-46e1-90a1-7ed6-658256124b4c&appId=com.domain.myapp&deviceId=6789-1234-1234-123-123456'

Response
********

In case of success, the answer is a string representing the new session token that is to be used for all further API calls.
The prior session token is no longer used by the app.

================ ========================
HTTP Status code Response body
================ ========================
200 OK           the authentication token
================ ========================

Sample response body
--------------------

.. code-block:: none

  3ef9f161-46e1-90n1-7ed6-658256hl4bff

Error response
--------------

================ ====================================
HTTP Status code Description
================ ====================================
401 Unauthorized the transmitted token was incorrect
================ ====================================

3. List issues
==============

With the help of the session token, the system asks for a list of unique identifiers of issues.
The implementation can deliver either Purple DS issue IDs or external issue numbers, which are configured as "Issue No." in the Purple DS | Manager.

The special case of returning an array of exactly one empty string (:code:`[""]` in JSON) is interpreted as "all issues without an Issue No."
and can be used to grant access to all app content, if this is the intended use case.

Request
*******

GET :code:`/issues/list`

Parameters (URL)
----------------

======== =====================================================================
Name     Description
======== =====================================================================
token    the token retrieved by login or renew
appId    the bundle identifier / package name of the app or a configured value
deviceId the unique device id of the calling device
======== =====================================================================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/issues/list?token=2ef9f161-46e1-90a1-7ed6-658256124b4c&appId=com.domain.myapp&deviceId=6789-1234-1234-123-123456'

Response
********

On success, a JSON String Array containing the issue id's or issue numbers of the issues available for the user is returned.

=============== ==============================
Response header Value
=============== ==============================
Content-Type    application/json;charset=UTF-8
=============== ==============================

================ =============================
HTTP Status code Response body
================ =============================
200 OK           JSON-Encoded Array of Strings
================ =============================

Sample response body
--------------------

.. code-block:: json

  ["842a954728n7490118s0b8329ff","147b876348z9371540994872649dr","143a938211b058372659d737163ab"]

4. Verify access to an issue
============================

After retrieving a list of issue identifiers, the app presents the identified issues to the user.
Right before the app opens a specific issue, it verifies again, that the user has still access to that issue.

This verification is done with the external issue number, which is configured as "Issue No." in the **Purple DS | Manager**
and if this is not successful with the Purple DS issue ID as well.

In the aforementioned special case of granting access to all app content by returning an array of exactly one empty string (:code:`[""]` in JSON)
this call should simply return an HTTP status 200 OK on any request.

Request
*******

GET :code:`/issue/verify`

Parameters (URL)
----------------

======== =====================================================================
Name     Description
======== =====================================================================
token    the token retrieved by login or renew
issueId  the identifier of an issue
appId    the bundle identifier / package name of the app or a configured value
deviceId the unique device id of the calling device
======== =====================================================================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/issue/verify?token=2ef9f161-46e1-90a1-7ed6-658256124b4c&appId=com.domain.myapp&deviceId=6789-1234-1234-123-123456'

Response
********

No response body is expected to be returned by this call. The HTTP status code is interpreted as follows:

================ =============================
HTTP Status code Description
================ =============================
200 OK           the issue is accessible
401 Unauthorized the token is invalid,
                 the issue is not accessible
403 Forbidden    the issue is not accessible
================ =============================

5. Logout
=========

A call to logout should invalidate the token. Further calls to the API with the token are expected to fail.

Request
*******

POST :code:`/user/logout`

============== =================================
Request header Value
============== =================================
Content-Type   application/x-www-form-urlencoded
============== =================================

Parameters (Request body)
-------------------------

======== =====================================================================
Name     Description
======== =====================================================================
token    the token retrieved by login or renew
appId    the bundle identifier / package name of the app or a configured value
deviceId the unique device id of the calling device
======== =====================================================================


Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/user/logout' -H 'content-type: application/x-www-form-urlencoded' \
   -d 'token=2ef9f161-46e1-90a1-7ed6-658256124b4c&appId=com.domain.myapp&deviceId=6789-1234-1234-123-123456'

Response
********

No response body is expected to be returned by this call.

================ ========================
HTTP Status code Description
================ ========================
200 OK           the user is logged out
================ ========================

Configuration
#############

The following parameters can be set when this entitlement type is selected in the **Purple DS | Manager** for an app:

========================= ========================================================= ============================
Parameter                 Description                                               Example
========================= ========================================================= ============================
URL                       Server URL of the entitlement REST interface              https://example.com/rest/api
appId                     The appId to be used to identify the app at the           my-app
                          entitlement server. Default is the package name.
========================= ========================================================= ============================
