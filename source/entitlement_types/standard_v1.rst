#########################
Standard Entitlement (V1)
#########################

A Standard Entitlement Server in Version 1 provides an HTTP REST interface with 3 methods to login, retrieve a list of issues and logout.
It is configured with the URL and cache validity.

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

======== ===================
Name     Description
======== ===================
username urlencoded username
password urlencoded password
======== ===================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/user/login' -H 'content-type: application/x-www-form-urlencoded' -d 'username=testuser%40example.com&password=1234'

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

2. List issues
==============

With the help of the session token, the system asks for a list of unique identifiers of issues.
The implementation can deliver either Purple DS issue IDs or external issue numbers, which are configured as "Issue No." in the Purple DS | Manager.

The special case of returning an array of exactly one empty string (:code:`[""]` in JSON) is interpreted as "all issues" and can be used
to grant access to all app content, if this is the intended use case.

Request
*******

GET :code:`/issues/list`

Parameters (URL)
----------------

===== =============================
Name     Description
===== =============================
token the token received from login
===== =============================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/issues/list?token=2ef9f161-46e1-90a1-7ed6-658256124b4c'

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

3. Logout
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

===== ========================
Name  Description
===== ========================
token the authentication token
===== ========================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/user/logout' -H 'content-type: application/x-www-form-urlencoded' -d 'token=2ef9f161-46e1-90a1-7ed6-658256124b4c'

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
Cache Validity in Minutes Number of Minutes a retrieved issue list should be cached 1
========================= ========================================================= ============================
