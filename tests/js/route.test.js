import route from 'ziggy-js';
import { strictEqual as same } from 'assert';
import { Ziggy } from './routes'

const defaultWindow = {
  location: {
    host: 'ziggy.dev',
  },
};


beforeAll(() => {
  delete window.location;
  window.location = {};
});

beforeEach(() => {
  window.location = { ...defaultWindow.location };
  global.window.location = { ...defaultWindow.location };
  global.Ziggy = { ...Ziggy };
});

describe('route()', () => {
  test('can return base URL if path is "/"', () => {
    same(route('home'), 'https://ziggy.dev');
  });
  test('can generate a URL with no parameters', () => {
    same(route('posts.index'), 'https://ziggy.dev/posts');
  });
  test('can generate a URL with one parameters', () => {
    same(route('posts.show', 1), 'https://ziggy.dev/posts/1');
  })
  test('can generate a URL with multiple named parameters', () => {
    same(route('posts.comments.show', {post_id: 1, id: 2}), 'https://ziggy.dev/posts/1/comments/2');
  })
});
