# Masonite JS Routes

Use your Masonite named routes in Javascript

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="160px">
</p>

This package creates a helper that you can include in your views. It will export a JavaScript object of your application's named routes, keyed by their names (aliases).

You can combine it with [ziggy-js](#) library as to get a global `route()` helper function which you can use to access your routes in your JavaScript.

## Learning Masonite

Masonite strives to have extremely comprehensive documentation. All documentation can be [Found Here](https://masoniteframework.gitbooks.io/docs/content/) and would be wise to go through the tutorials there. If you find any discrepencies or anything that doesn't make sense, be sure to comment directly on the documentation to start a discussion!

Also be sure to join the [Slack channel](https://masoniteframework.gitbooks.io/docs/content/)!

## Installation

```bash
pip install masonite-js-routes
```

Add `JsRoutesProvider` to your app

```python
# ...
from masonite.js_routes import
PROVIDERS = [
  # ...
  # Third Party Applications
  JsRoutesProvider,
  # ...
]
```

## Usage

In your views, just add this helper where you want to get `Ziggy` routes as a Javascript object:

```html
{{ js_routes() }}
```

## Configuration

You can skip this step if you don't want to filters routes included by the helper.
Else you must publish the config file by running the command:

```bash
python craft js_routes:install
```

Then you should have a new `js_routes.py` config file in `config/`.

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

## How to contribute

Disclaimer: this package is based on the legacy Laravel package [Ziggy](https://github.com/tighten/ziggy).
