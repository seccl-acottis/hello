import { add } from '../src/hello.js';
import assert from 'assert';

assert(add(1, 2) === 3);
assert(add(1, 2) != 4);
