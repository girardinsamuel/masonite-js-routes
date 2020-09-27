# Masonite JS Routes

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="130px">
</p>

<p align="center">
  <a href="https://docs.masoniteproject.com">
    <img alt="Masonite Package" src="https://img.shields.io/static/v1?label=Masonite&message=package&labelColor=grey&color=blue&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAAA6gAwAEAAAAAQAAAA4AAAAATspU+QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAnxJREFUKBVNUl1IVEEUPjPObdd1VdxWM0rMIl3bzbVWLSofVm3th0AhMakHHyqRiNSHEAq5b2HSVvoQRUiEECQUQkkPbRslRGigG8auoon2oPSjpev+3PWeZq7eaC5nDt93vplz5txDQJYpNxX4st4JFiwj9aCqmswUFQNS/A2YskrZJPYefkECC2GhQwAqvLYybwXrwBvq8HSNOXRO92+aH7nW8vc/wS2Z9TqneYt2KHjlf9Iv+43wFJMExzO0YE5OKe60N+AOW6OmE+WJTBrg23jjzWxMBauOlfyycsV24F+cH+zAXYUOGl+DaiDxfl245/W9OnVrSY+O2eqPkyz4sVvHoKp9gOihf5KoAVv3hkQgbj/ihG9fI3RixKcUVx7lJVaEc0vnyf2FFll+ny80ZHZiGhIKowWJBCEAKr+FSuNDLt+lxybSF51lo74arqs113dOZqwsptxNs5bwi7Q3q8npSC2AWmvjTncZf1l61e5DEizNn5mtufpsqk5+CZTuq00sP1wkNPv8jeEikVVlJso+GEwRtNs3QeBt2YP2V2ZI3Tx0e+7T89zK5tNASOLEytJAryGtkLc2PcBM5byyUWYkMQpMioYcDcchC6xN220Iv36Ot8pV0454RHLEwmmD7UWfIdX0zq3GjMPG5NKBtv5qiPEPekK2U51j1451BZoc3i+1ohSQ/UzzG5uYFFn2mwVUnO4O3JblXA91T51l3pB3QweDl7sNXMyEjbguSjrPcQNmwDkNc8CbCvDd0+xCC7RFi9wFulD3mJeXqxQevB4prrqgc0TmQ85NG/K43e2UwnMVAJIEBNfWRYR3HfnvivrIzMyo4Hgy+hfscvLo53jItAAAAABJRU5ErkJggg==">
  </a>
  <img alt="GitHub Workflow Status (branch)" src="https://img.shields.io/github/workflow/status/girardinsamuel/masonite-js-routes/Test%20Application/master">
  <img alt="Coveralls github branch" src="https://img.shields.io/coveralls/github/girardinsamuel/masonite-js-routes/master">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-js-routes">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/girardinsamuel/masonite-js-routes">
  <img alt="License" src="https://img.shields.io/github/license/girardinsamuel/masonite-js-routes">
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Introduction

Use your Masonite named routes in Javascript !

This package creates a helper that you can include in your views. It will export a JavaScript object of your application's named routes, keyed by their names (aliases).

You can combine it with [ziggy-js](https://github.com/tighten/ziggy) library as to get a global `route()` helper function which you can use to access your routes in your JavaScript.

## Features

- _Add your package main features here_
- _and here_

## Official Masonite Documentation

New to Masonite ? Please first read the [Official Documentation](https://docs.masoniteproject.com/).
Masonite strives to have extremely comprehensive documentation 😃. It would be wise to go through the tutorials there.
If you find any discrepencies or anything that doesn't make sense, be sure to comment directly on the documentation to start a discussion!

Also be sure to join the [Slack channel](http://slack.masoniteproject.com/)!

## Installation

```bash
pip install masonite-js-routes
```

## Configuration

Add JSRoutesProvider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from masonite.js_routes import JSRoutesProvider

# ...
PROVIDERS = [
    # ...

    # Third Party Providers
    JSRoutesProvider,

    # ...
]
```

You can skip this step if you don't want to filters routes included by the helper.
Else you must publish the config file by running the command:

```bash
python craft js_routes:install
```

Then you should have a new `js_routes.py` config file in `config/`.

```bash
python craft js_routes:install
```

## Usage

In your views, just add this helper where you want to get `Ziggy` routes as a Javascript object:

```html
{{ js_routes() }}
```

### Basic filtering

Only the routes matching a list of name patterns will be included:

```python
FILTERS = {
    "only": ["welcome.*"],
}
```

Only the routes which does not match a list of name patterns will be included:

```python
FILTERS = {
    "except": ["admin.*"],
}
```

**Note: You have to choose one or the other. Setting both `only` and `except` will disable filtering altogether and simply return the default list of routes.**

### Filtering using Groups

Only the routes matching a group or a list of groups will be included if
groups are passed to the helpers

```python
FILTERS = {
    "groups": {
        "app": ["app.*"],
        "api": ["api.*"],
    }
}
```

and in your view :

```html
{{ js_routes('app') }}
```

or a list of group names

```html
{{ js_routes(['app', 'api']) }}
```

**Note: Passing group names to the `routes` helper will always take precedence over your other only or except settings.**

## Content Security Policy

A Content Security Policy may block unsafe inline scripts which Ziggy uses to pass the routes to JavaScript. By adding a nonce to your CSP you can allow certain inlined scripts. To add this nonce to Ziggy you can pass it as the second argument to the helper:

```html
{{ routes(false, '[YOUR_NONCE]') }}
```

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## License

Masonite JS Routes is open-sourced software licensed under the [MIT license](LICENSE).

**Disclaimer**: this package is based on the Laravel package [Ziggy](https://github.com/tighten/ziggy).
