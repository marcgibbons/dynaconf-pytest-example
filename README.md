# Dynaconf & pytest

This example demonstrates how to dynamically modify
[Dynaconf](https://www.dynaconf.com) setting values in
[pytest](https://docs.pytest.org) using an auto-use fixture.

It loads the "production" settings file, and merges a separate settings file
specific to the test suite (good for setting global, deterministic values).

See my [blog post](https://marcgibbons.com/posts/dynaconf-pytest) for context.
