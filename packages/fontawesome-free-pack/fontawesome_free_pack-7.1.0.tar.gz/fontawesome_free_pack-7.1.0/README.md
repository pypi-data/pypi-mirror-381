# fontawesome-free-pack

[![Crates.io Version][fa-cargo-badge]][fa-cargo-link]
![MSRV][msrv-badge]
[![PyPI - Version][fa-pip-badge]][fa-pip-link]
![Min Py][min-py]

A redistribution of SVG assets and some metadata from the
[`@fortawesome/fontawesome-free` npm package](https://www.npmjs.com/package/@fortawesome/fontawesome-free).

## Optimized SVG data

The SVG data is embedded as strings after it is optimized with SVGO. This
package is intended to easily inject SVG data into HTML documents. Thus, we have
stripped any `width` and `height` fields from the `<svg>` element, while
retaining any `viewBox` field in the `<svg>` element.

## Usage

All icons are instantiated as constants using the `Icon` data structure.
There is a convenient `get_icon()` function to fetch an icon using it's slug name.

Note the family of icon is expected to prefix the slug like a relative path:
`<family>/<slug>`

### In Python

```python
from fontawesome_free_pack import get_icon, BRANDS_GITHUB

fetched = get_icon("brands/github")
assert fetched is not None
assert BRANDS_GITHUB.svg == fetched.svg
```

### In Rust

```rust
use fontawesome_free_pack::{get_icon, BRANDS_GITHUB};

assert_eq!(BRANDS_GITHUB.svg, get_icon("brands/github").unwrap().svg);
```

## Rust Features

This crate has the following features:

- `brands`: Includes all icons under the fontawesome brands family.
- `solid`: Includes all icons under the fontawesome solid family.
- `regular`: Includes all icons under the fontawesome regular family.

All the above features are enabled by default.

The python binding does not support conditionally compiling certain icon
families.

[fa-cargo-badge]: https://img.shields.io/crates/v/fontawesome-free-pack
[fa-cargo-link]: https://crates.io/crates/fontawesome-free-pack
[fa-pip-badge]: https://img.shields.io/pypi/v/fontawesome-free-pack
[fa-pip-link]: https://pypi.org/project/fontawesome-free-pack/

[msrv-badge]: https://img.shields.io/badge/MSRV-1.85.0-blue
[min-py]: https://img.shields.io/badge/Python-v3.9+-blue
