tree-sitter-javascript
===========================

[![CI Status](https://github.com/tree-sitter/tree-sitter-javascript/actions/workflows/ci.yml/badge.svg)](https://github.com/tree-sitter/tree-sitter-javascript/actions/workflows/ci.yml)

JavaScript and JSX grammar for [tree-sitter][]. For TypeScript, see [tree-sitter-typescript][].

[tree-sitter]: https://github.com/tree-sitter/tree-sitter
[tree-sitter-typescript]: https://github.com/tree-sitter/tree-sitter-typescript

References

* [The ESTree Spec](https://github.com/estree/estree)
* [The ECMAScript 2015 Spec](http://www.ecma-international.org/ecma-262/6.0/)

## Modification (By Bo)

Make those visible in parse tree:
```
$.template_chars
```

## Modification of grammar file

Install tree-sitter-cli
```
npm install -g tree-sitter-cli
npm install -g node-gyp
```

Generate and compile:
```
tree-sitter generate && node-gyp build
```