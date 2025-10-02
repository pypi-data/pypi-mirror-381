"""
Statistical and numerical computation functions for JAX, focusing on tools
not available in the main JAX API.

## Overview

This package provides JAX-compatible implementations of specialized numerical
functions with full differentiability support. All functions are designed to
work seamlessly with JAX's transformations (JIT, grad, vmap, etc.) and follow
JAX's functional programming paradigms.

### Special Functions ([`numerax.special`](api/special))

Mathematical special functions with custom derivative implementations.
Functions provide exact gradients through custom JVP rules where standard
automatic differentiation would be inefficient or unstable.

### Statistical Methods ([`numerax.stats`](api/stats))

Advanced statistical computation tools for inference problems. Implements
complex statistical models that benefit from JAX's compilation and
differentiation capabilities.

### Utilities ([`numerax.utils`](api/utils))

Development utilities for creating JAX-compatible functions with proper
documentation support. Includes decorators and helpers for preserving
function metadata when using JAX's advanced features like custom derivatives.
"""

from . import special, stats, utils

__version__ = "1.1.0"

__all__ = ["special", "stats", "utils"]
