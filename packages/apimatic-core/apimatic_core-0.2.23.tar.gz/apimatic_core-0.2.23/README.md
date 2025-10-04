# apimatic-core

[![PyPI][pypi-version]][apimatic-core-pypi-url]
[![Tests][test-badge]][test-url]
[![Test Coverage][coverage-badge]][coverage-url]
[![Maintainability Rating][maintainability-badge]][maintainability-url]
[![Vulnerabilities][vulnerabilities-badge]][vulnerabilities-url]
[![Licence][license-badge]][license-url]

## Introduction

The APIMatic Core libraries provide a stable runtime that powers all the functionality of SDKs.
This includes functionality like the ability to create HTTP requests, handle responses, apply authentication schemes, convert API responses back to object instances, validate user and server data, and more advanced features like templating and secure signature verification.

---

## Installation

You will need Python 3.7+ to support this package.

```bash
pip install apimatic-core
```

---

## API Call Classes

| Name                                                   | Description                                        |
| ------------------------------------------------------ | -------------------------------------------------- |
| [`RequestBuilder`](apimatic_core/request_builder.py)   | A builder class used to build an API Request       |
| [`APICall`](apimatic_core/api_call.py)                 | A class used to create an API Call object          |
| [`ResponseHandler`](apimatic_core/response_handler.py) | Used to handle the response returned by the server |

---

## Authentication

| Name                                                               | Description                                             |
| ------------------------------------------------------------------ | ------------------------------------------------------- |
| [`HeaderAuth`](apimatic_core/authentication/header_auth.py)        | HTTP authentication via headers                         |
| [`QueryAuth`](apimatic_core/authentication/query_auth.py)          | HTTP authentication via query parameters                |
| [`AuthGroup`](apimatic_core/authentication/multiple/auth_group.py) | Supports grouping of multiple authentication operations |
| [`And`](apimatic_core/authentication/multiple/and_auth_group.py)   | Logical AND grouping for multiple authentication types  |
| [`Or`](apimatic_core/authentication/multiple/or_auth_group.py)     | Logical OR grouping for multiple authentication types   |
| [`Single`](apimatic_core/authentication/multiple/single_auth.py)   | Represents a single authentication type                 |

---

## Configurations

| Name                                                                              | Description                                                         |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [`EndpointConfiguration`](apimatic_core/configurations/endpoint_configuration.py) | Holds configurations specific to an endpoint                        |
| [`GlobalConfiguration`](apimatic_core/configurations/global_configuration.py)     | Holds global configuration properties to make a successful API call |

---

## Decorators

| Name                                                        | Description                      |
| ----------------------------------------------------------- | -------------------------------- |
| [`LazyProperty`](apimatic_core/decorators/lazy_property.py) | Decorator for lazy instantiation |

---

## Exceptions

| Name                                                                                     | Description                                             |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [`OneOfValidationException`](apimatic_core/exceptions/oneof_validation_exception.py)     | Thrown on failed validation of oneOf union-type cases   |
| [`AnyOfValidationException`](apimatic_core/exceptions/anyof_validation_exception.py)     | Thrown on failed validation of anyOf union-type cases   |
| [`AuthValidationException`](apimatic_core/exceptions/auth_validation_exception.py)       | Thrown when authentication scheme validation fails      |

---

## Factories

| Name                                                                      | Description                      |
| ------------------------------------------------------------------------- | -------------------------------- |
| [`HttpResponseFactory`](apimatic_core/factories/http_response_factory.py) | Factory to create HTTP responses |

---

## HTTP Configurations
| Name                                                                                        | Description                                                                                                                               |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [`HttpClientConfiguration`](apimatic_core/http/configurations/http_client_configuration.py) | A class used for configuring the SDK by a user                                                                                            |
| [`ProxySettings`](apimatic_core/http/configurations/proxy_settings.py)                      | ProxySettings encapsulates HTTP proxy configuration for Requests, e.g. address, port and optional basic authentication for HTTP and HTTPS |

---

## HTTP

| Name                                                                                        | Description                                |
| ------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [`HttpCallBack`](apimatic_core/factories/http_response_factory.py)                          | Callback handler for HTTP lifecycle events |
| [`HttpRequest`](apimatic_core/http/request/http_request.py)                                 | Represents an HTTP request                 |
| [`ApiResponse`](apimatic_core/http/response/api_response.py)                                | Wraps an API response                      |
| [`HttpResponse`](apimatic_core/http/response/http_response.py)                              | Represents an HTTP response                |

---

## Logging Configuration

| Name                                                                                                 | Description                                |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [`ApiLoggingConfiguration`](apimatic_core/logger/configuration/api_logging_configuration.py)         | Global logging configuration for API calls |
| [`ApiRequestLoggingConfiguration`](apimatic_core/logger/configuration/api_logging_configuration.py)  | Request logging configuration              |
| [`ApiResponseLoggingConfiguration`](apimatic_core/logger/configuration/api_logging_configuration.py) | Response logging configuration             |

---

## Logger

| Name                                                      | Description                                                        |
| --------------------------------------------------------- | ------------------------------------------------------------------ |
| [`SdkLogger`](apimatic_core/logger/sdk_logger.py)         | Logs requests and responses when logging configuration is provided |
| [`NoneSdkLogger`](apimatic_core/logger/sdk_logger.py)     | No-op logger used when logging is disabled                         |
| [`ConsoleLogger`](apimatic_core/logger/default_logger.py) | Simple console logger implementation                               |
| [`LoggerFactory`](apimatic_core/logger/sdk_logger.py)     | Provides appropriate logger instances based on configuration       |

---

## Types

| Name                                                                        | Description                                       |
| --------------------------------------------------------------------------- | ------------------------------------------------- |
| [`SerializationFormats`](apimatic_core/types/array_serialization_format.py) | Enumeration of array serialization formats        |
| [`DateTimeFormat`](apimatic_core/types/datetime_format.py)                  | Enumeration of DateTime formats                   |
| [`ErrorCase`](apimatic_core/types/error_case.py)                            | Represents exception types                        |
| [`FileWrapper`](apimatic_core/types/file_wrapper.py)                        | Wraps files for upload with content-type          |
| [`Parameter`](apimatic_core/types/parameter.py)                             | Represents an API parameter                       |
| [`XmlAttributes`](apimatic_core/types/xml_attributes.py)                    | Represents XML parameter metadata                 |
| [`OneOf`](apimatic_core/types/union_types/one_of.py)                        | Represents OneOf union types                      |
| [`AnyOf`](apimatic_core/types/union_types/any_of.py)                        | Represents AnyOf union types                      |
| [`LeafType`](apimatic_core/types/union_types/leaf_type.py)                  | Represents a specific case in a OneOf/AnyOf union |

---

## Pagination

| Name                                                                           | Description                                                       |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| [`CursorPagination`](apimatic_core/pagination/strategies/cursor_pagination.py) | Cursor-based pagination helper                                    |
| [`LinkPagination`](apimatic_core/pagination/strategies/link_pagination.py)     | Link-based pagination helper                                      |
| [`OffsetPagination`](apimatic_core/pagination/strategies/offset_pagination.py) | Offset-based pagination helper                                    |
| [`PagePagination`](apimatic_core/pagination/strategies/page_pagination.py)     | Page-number-based pagination helper                               |
| [`PaginatedData`](apimatic_core/pagination/paginated_data.py)                  | Iterable interface to traverse items and pages in a paginated API |

---

## Utilities

| Name                                                               | Description                                                |
| ------------------------------------------------------------------ | ---------------------------------------------------------- |
| [`ApiHelper`](apimatic_core/utilities/api_helper.py)               | Helper functions for API calls                             |
| [`AuthHelper`](apimatic_core/utilities/auth_helper.py)             | Helper functions for authentication                        |
| [`ComparisonHelper`](apimatic_core/utilities/comparison_helper.py) | Utilities for response comparison                          |
| [`FileHelper`](apimatic_core/utilities/file_helper.py)             | File handling utilities                                    |
| [`XmlHelper`](apimatic_core/utilities/xml_helper.py)               | XML serialization/deserialization helpers                  |
| [`DateTimeHelper`](apimatic_core/utilities/datetime_helper.py)     | Date/time parsing and validation helpers                   |
| [`UnionTypeHelper`](apimatic_core/utilities/union_type_helper.py)  | Deserialization and validation for OneOf/AnyOf union types |

---

## **Signature Verification**

| Name                                                                                                 | Description                                                                          |
|------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------ |
| [`HmacSignatureVerifier`](apimatic_core/security/signature_verifiers/hmac_signature_verifier.py)  | Verifies HMAC signatures using configurable templates, hash algorithms, and encoders |
| [`HexEncoder`](apimatic_core/security/signature_verifiers/hmac_signature_verifier.py)             | Encodes digest as lowercase hex                                                      |
| [`Base64Encoder`](apimatic_core/security/signature_verifiers/hmac_signature_verifier.py)          | Encodes digest as Base64                                                             |
| [`Base64UrlEncoder`](apimatic_core/security/signature_verifiers/hmac_signature_verifier.py)       | Encodes digest as URL-safe Base64 without padding                                    |

This layer enables secure handling of webhooks, callbacks, and API integrations that rely on HMAC or other signing strategies.

---

| Name                                                                    | Description                                                                                                                                                                                        |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`to_unified_request`](apimatic_core/adapters/request_adapter.py)       | **Sync** wrapper for Flask/Django (WSGI). Unwraps Flask `LocalProxy` when present and bridges to the async converter using an event loop.                                                          |
| [`to_unified_request_async`](apimatic_core/adapters/request_adapter.py) | **Async** adapter that converts Starlette/FastAPI, Flask/Werkzeug, or Django requests into a framework-agnostic `Request` snapshot (method, path, url, headers, raw body, query, form, cookies).   |

---

## Links

* [apimatic-core-interfaces](https://pypi.org/project/apimatic-core-interfaces/)

[pypi-version]: https://img.shields.io/pypi/v/apimatic-core
[apimatic-core-pypi-url]: https://pypi.org/project/apimatic-core/
[test-badge]: https://github.com/apimatic/core-lib-python/actions/workflows/test-runner.yml/badge.svg
[test-url]: https://github.com/apimatic/core-lib-python/actions/workflows/test-runner.yml
[coverage-badge]: https://sonarcloud.io/api/project_badges/measure?project=apimatic_core-lib-python&metric=coverage
[coverage-url]: https://sonarcloud.io/summary/new_code?id=apimatic_core-lib-python
[maintainability-badge]: https://sonarcloud.io/api/project_badges/measure?project=apimatic_core-lib-python&metric=sqale_rating
[maintainability-url]: https://sonarcloud.io/summary/new_code?id=apimatic_core-lib-python
[vulnerabilities-badge]: https://sonarcloud.io/api/project_badges/measure?project=apimatic_core-lib-python&metric=vulnerabilities
[vulnerabilities-url]: https://sonarcloud.io/summary/new_code?id=apimatic_core-lib-python
[license-badge]: https://img.shields.io/badge/licence-MIT-blue
[license-url]: LICENSE
