<p align="center">
    <img src="https://banners.beyondco.de/Masonite%20JS%20Routes.png?theme=light&packageManager=pip+install&packageName=masonite-js-routes&pattern=topography&style=style_1&description=Use%20your%20Masonite%20named%20routes%20in%20Javascript&md=1&showWatermark=1&fontSize=100px&images=https%3A%2F%2Fgblobscdn.gitbook.com%2Fspaces%2F-L9uc-9XAlqhXkBwrLMA%2Favatar.png">
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

Use your Masonite named routes in Javascript.

This package provides a helper that inject your Masonite application routes definition into your views. It will export a JavaScript object of your application's named routes, keyed by their names (aliases).

You can combine it with [ziggy-js](https://github.com/tighten/ziggy) library as to get a global `route()` helper function which you can use to access your routes in your JavaScript.

## Features

- Avoid hard-coding urls client-side
- Generate once your routes file
- Compatible with client-side route helper `ziggy-js`
- Possibility to filter routes to include client-side

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

Then you can publish the configuration file in your project if you need to change some parameters:

```bash
python craft package:publish js_routes
```

## Usage

1. [Using `routes` view helper](#1.-using-routes-view-helper): routes will be generated at each request and included client-side in the page.
2. [Generating routes as Javascript file](#2.-generating-routes-as-javascript-file): routes are generated once in a file and you load this file client-side. When you update your routes, you must regenerate the file.

### 1. Using `routes` view helper

1. In your views, just add this helper where you want to get `Ziggy` routes as a Javascript object (e.g. in `<head></head>` or at the end of body).

```html
{{ routes() }}
```

#### Basic filtering

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

#### Filtering using Groups

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
{{ routes('app') }}
```

or a list of group names

```html
{{ routes(['app', 'api']) }}
```

**Note: Passing group names to the `routes` helper will always take precedence over your other only or except settings.**

### 2. Generating routes as Javascript file

You can also generate once the routes as a Javascript file. For now it generates a file exporting
`Ziggy` object routes as it is made to use it with `ziggy-js`.

To generate the routes, run the craft command (it takes an optional `--path` argument to change the output path):

```bash
python craft js_routes:generate
```

(You could add this into a pipeline, to regenerate it whenever needed).

You will get a file like this:

```js
var Ziggy = {
  routes: {
    home: { uri: "", methods: ["GET", "HEAD"], domain: null },
    login: { uri: "login", methods: ["GET", "HEAD"], domain: null },
  },
  url: "http://ziggy.test",
  port: null,
  defaults: {},
};

export { Ziggy };
```

## Client-side usage

Then to be able to use it client-side you can refer to [ziggy-js documentation](https://github.com/tighten/ziggy#advanced-setup).
(Note that you don't have to use this library you can use the routes objects as you like.)

### Quick explanation with Vue.js

Install the library:

```bash
npm install ziggy-js
```

Then in your Vue.js entrypoint you could for example define a global `route()` mixin (using the `route()` method from `ziggy-js`).

- With the **option 1**, `Ziggy` will be available in the global javascript `window` scope

```javascript
// app.js
import { createApp, h } from "vue";
import route from "ziggy-js";

import App from "./App.vue";

const app = createApp(App).mixin({
  methods: {
    route(name, params = {}, absolute = true) {
      return route(name, params, absolute, window.Ziggy);
    },
  },
});

// App.vue
// ...
this.route("users", 2); // == http://ziggy.test/users/2
```

- With the **option 2**, the routes config must be imported from the generated file (instead of the `window` object)

```javascript
// app.js
import { createApp, h } from "vue";
import route from "ziggy-js";
import { Ziggy } from "./routes";

import App from "./App.vue";

const app = createApp(App).mixin({
  methods: {
    route(name, params = {}, absolute = true) {
      return route(name, params, absolute, Ziggy);
    },
  },
});

// App.vue
// ...
this.route("users", 2); // == http://ziggy.test/users/2
```

## Content Security Policy

A Content Security Policy may block unsafe inline scripts which Ziggy uses to pass the routes to JavaScript. By adding a nonce to your CSP you can allow certain inlined scripts. To add this nonce to Ziggy you can pass it as the second argument to the helper:

```html
{{ routes(false, '[YOUR_NONCE]') }}
```

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## Maintainers

- [Samuel Girardin](https://www.github.com/girardinsamuel)

## License

Masonite JS Routes is open-sourced software licensed under the [MIT license](LICENSE).
