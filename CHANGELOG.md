# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2021-02-07

### Bug fixes

- Fix format of routes payload with latest version of `ziggy-js`

### Features

- Improve documentation in README
- Add a CHANGELOG

### Build system

- Switch coverage to codecov.io
- Add dependabot

### BREAKING CHANGES

- The format of the payload included client-side won't be compatible with oldest `ziggy-js` versions,
  so it is advised to upgrade `npm install -U ziggy-js` (and regenerate your routes if needed).

## [0.3.0] - 2020-09-28

### Bug fixes

- Fix installation command to publish config file

### Features

- Add generate command to dump routes in file as Ziggy object
- Update documentation for routes generation

## [0.2.0] - 2020-09-27

### Features

- Add README as description on PyPi

## [0.1.0] - 2020-09-27

- First alpha release of the package
