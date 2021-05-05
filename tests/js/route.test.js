import route from 'ziggy-js';
import { strictEqual as same } from 'assert';
import { Ziggy } from './routes'

const defaultWindow = {
  location: {
    host: 'ziggy.dev',
  },
};

const defaultZiggy = {
    url: 'https://ziggy.dev',
    port: null,
    defaults: { locale: 'en' },
    routes: {
        'home': {
            uri: '/',
            methods: ['GET', 'HEAD'],
        },
        'posts.index': {
            uri: 'posts',
            methods: ['GET', 'HEAD'],
        },
    },
};

beforeAll(() => {
  delete window.location;
  window.location = {};
});

beforeEach(() => {
  window.location = { ...defaultWindow.location };
  global.window.location = { ...defaultWindow.location };
  // global.Ziggy = { ...defaultZiggy };
  global.Ziggy = { ...Ziggy };
});

describe('route()', () => {
  test('can generate a URL with no parameters', () => {
    same(route('welcome'), 'https://ziggy.dev/');
  })
});
