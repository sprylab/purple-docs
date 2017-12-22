########################
Adobe DPS Entitlement V1
########################

The Adobe DPS Entitlement description is spread over multiple documents and tutorials to be found here:
http://www.adobe.com/devnet/digitalpublishingsuite/entitlement.html and elsewhere.

Here is a brief aggregation of the information used when implementing the appropriate plugin.

API Description
###############

All calls described in the following are designed to return an XML response.
Though not all server implementations set the appropriate response content type, therefore our (universal client) implementation doesn't rely on that.
Furthermore, the XML response has an attribute named :code:`httpResponseCode` which is usually set to an appropriate HTTP status code,
while the actual HTTP status code of the response is :code:`200 Ok`. Our implementation accepts both the actual HTTP status code and the
:code:`httpResponseCode` attribute from the XML response and treats them synonymously.

1. Sign in with credentials
===========================

By signing in, users obtain an authentication token that is required for all subsequent API calls.

Request
*******

GET :code:`/SignInWithCredentials`

Parameters (URL)
----------------

============ =====================================================================
Name         Description
============ =====================================================================
emailAddress urlencoded username
password     urlencoded password
appId        the bundle identifier / package name of the app or a configured value
uuid         the unique device id of the calling device
============ =====================================================================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/SignInWithCredentials?emailAddress=testuser%40example.com&password=1234&appId=com.package.app&uuid=3944-1345-1145656-5645'

Response
********

In case of success, the answer is an XML object with an :code:`httpResponseCode` of 200 and an :code:`authToken`.

================ ============================
HTTP Status code Response body
================ ============================
200 OK           XML object, see sample below
================ ============================

Sample response body
--------------------

.. code-block:: xml

  <result httpResponseCode="200">
    <authToken>VFgrV1lKd09pL2s2NnlIKzE5R</authToken>
  </result>

Error response
--------------

================ ============================
HTTP Status code Response body
================ ============================
200 OK           XML object, see sample below
401 Unauthorized XML object, see sample below
================ ============================

Sample error response body
--------------------------

.. code-block:: xml

  <result httpResponseCode="401" errorCode=""/>

2. Renew authentication token
=============================

Using this call, an authentication token retrieved by SignInWithCredentials can be renewed.
The result is either the same or a new token which should be used instead in following API calls.

Request
*******

GET :code:`/renewAuthToken`

Parameters (URL)
----------------

============ ============================================================================================
Name         Description
============ ============================================================================================
authToken    an authentication token retrieved by SignInWithCredentials or a prior call to renewAuthToken
appId        the bundle identifier / package name of the app or a configured value
============ ============================================================================================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/renewAuthToken?authToken=VFgrV1lKd09pL2s2NnlIKzE5R&appId=com.package.app'

Response
********

In case of success, the answer is an XML object with an :code:`httpResponseCode` of 200 and a new :code:`authToken`.

================ ============================
HTTP Status code Response body
================ ============================
200 OK           XML object, see sample below
================ ============================

Sample response body
--------------------

.. code-block:: xml

  <result httpResponseCode="200">
    <authToken>VFgrV1lKd09pL2s2NnlIKzE5R</authToken>
  </result>

Error response
--------------

================ ============================
HTTP Status code Response body
================ ============================
200 OK           XML object, see sample below
401 Unauthorized XML object, see sample below
================ ============================

Sample error response body
--------------------------

.. code-block:: xml

  <result httpResponseCode="401" errorCode=""/>

3. Entitlements
===============

This calls delivers identifiers of the issues, the user is entitled to see.
While Purple DS issue ID's would be handled correctly, normally external issue identifiers are used,
which are configured as "Issue No." in the Purple DS | Manager.

Request
*******

GET :code:`/entitlements`

Parameters (URL)
----------------

============ ============================================================================================
Name         Description
============ ============================================================================================
authToken    an authentication token retrieved by SignInWithCredentials or a prior call to renewAuthToken
appId        the bundle identifier / package name of the app or a configured value
============ ============================================================================================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/entitlements?authToken=VFgrV1lKd09pL2s2NnlIKzE5R&appId=com.package.app'

Response
********

In case of success, the answer is an XML object with an :code:`httpResponseCode` of 200
and a list of :code:`productId` elements wrapped in an :code:`entitlements` element.

================ ============================
HTTP Status code Response body
================ ============================
200 OK           XML object, see sample below
================ ============================

Sample response body
--------------------

.. code-block:: xml

  <result httpResponseCode="200">
    <entitlements>
      <productId>com.package.app.07.2017</productId>
	  <productId>com.package.app.09.2017</productId>
	  <productId>com.package.app.thanksgiving.special</productId>
	  <productId>com.package.app.11.2017</productId>
    <entitlements>
  </result>

Error response
--------------

================ ============================
HTTP Status code Response body
================ ============================
200 OK           XML object, see sample below
401 Unauthorized XML object, see sample below
================ ============================

Sample error response body
--------------------------

.. code-block:: xml

  <result httpResponseCode="401" errorCode=""/>

4. Verify entitlement
=====================

After retrieving a list of issue identifiers, the app presents the identified issues to the user.
Right before the app opens a specific issue, it verifies again, that the user has still access to that issue.

Request
*******

GET :code:`/verifyEntitlement`

Parameters (URL)
----------------

============ ============================================================================================
Name         Description
============ ============================================================================================
authToken    an authentication token retrieved by SignInWithCredentials or a prior call to renewAuthToken
productId    the issue identifier as retrieved by the call to entitlements
appId        the bundle identifier / package name of the app or a configured value
============ ============================================================================================

Sample request
--------------

.. code-block:: bash

  curl '<Endpoint-Base-URL>/verifyEntitlement?authToken=VFgrV1lKd09pL2s2NnlIKzE5R&productId=com.package.app.07.2017&appId=com.package.app'

Response
********

In case of success, the answer is an XML object with an :code:`httpResponseCode` of 200
and a boolean value in an :code:`entitled` element.

================ ============================
HTTP Status code Response body
================ ============================
200 OK           XML object, see sample below
================ ============================

Sample response body
--------------------

.. code-block:: xml

  <result httpResponseCode="200">
    <entitled>true<entitled>
  </result>

Error response
--------------

================ ============================
HTTP Status code Response body
================ ============================
200 OK           XML object, see sample below
401 Unauthorized XML object, see sample below
================ ============================

Sample error response body
--------------------------

.. code-block:: xml

  <result httpResponseCode="401" errorCode=""/>

Configuration
#############

The following parameters can be set when this entitlement type is selected in the **Purple DS | Manager** for an app:

========================= ========================================================= ============================
Parameter                 Description                                               Example
========================= ========================================================= ============================
URL                       Server URL of the entitlement REST interface              https://example.com/rest/api
Cache Validity in Minutes Number of Minutes a retrieved issue list should be cached 1
appId                     The appId to be used to identify the app at the           my-app
                          entitlement server. Default is the package name.
========================= ========================================================= ============================
