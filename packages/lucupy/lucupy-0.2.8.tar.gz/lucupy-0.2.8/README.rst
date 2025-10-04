Lucupy
#########

This package contains data structures and functions to support all the microservices that make up the Schedule app
for the Gemini Program Plataform (and other auxiliary services such as Env and Resource)

Content
-------

- Minimodel: A small version of GPP's data model. This allows for any services to use common data structures to model programs, observations, etc.
- Helpers: A collection of functions that helps with the handling of data.
- Observatory: An API that allows Observatory-specific behaviour to be added to a service (or sub-service: e.g Collector)
- Sky: A library that calculates night events for the use of visibility in Observations
- Time Utils: Time handling functions
- Types: A collection of variables to use with Python typing
- Decorators: A collection of decorators (Currently empty)

Copyright (c) 2016-2022 Association of Universities for Research in Astronomy, Inc. (AURA)
For license information see LICENSE or https://opensource.org/licenses/BSD-3-Clause
