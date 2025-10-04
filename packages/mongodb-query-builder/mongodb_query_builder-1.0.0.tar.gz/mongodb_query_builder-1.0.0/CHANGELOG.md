# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive documentation system with Sphinx and Markdown formats
- Getting Started guide with installation instructions
- Complete API reference documentation for all builders
- Tutorial: Basic Queries with exercises
- Migration guide for converting raw MongoDB queries
- Performance optimization guide
- Documentation build system with `make docs` commands
- Multiple installation methods documented (PyPI, source, GitHub)

## [1.0.0] - 2025-10-03

### Added

#### QueryFilter
- Fluent interface for building MongoDB queries
- Comparison operators: equals, not_equals, greater_than, less_than, between
- String operations: contains, starts_with, ends_with, regex
- Array operations: array_contains, array_contains_all, array_size, elem_match
- Logical operators: any_of, all_of, none_of, not_filter
- Existence checks: exists, is_null, is_not_null
- Text search support with language and sensitivity options
- Automatic ObjectId string conversion
- Comprehensive error handling with QueryFilterError

#### AggregateBuilder
- Fluent interface for building MongoDB aggregation pipelines
- Pipeline stages: match, project, group, sort, limit, skip
- Join operations: lookup, lookup_pipeline, graph_lookup
- Array operations: unwind with preserve_null and include_array_index
- Field manipulation: add_fields, set, unset, replace_root, replace_with
- Faceting: facet, bucket, bucket_auto
- Output stages: count, sort_by_count, sample, out, merge
- Union operations: union_with
- Advanced features: redact, custom_stage
- Comprehensive error handling with AggregateBuilderError

#### AtlasSearchBuilder
- Fluent interface for building MongoDB Atlas Search queries
- Search operators: text, phrase, autocomplete, wildcard, regex, range
- Compound queries with CompoundBuilder
- Clause types: must, should, must_not, filter
- Minimum should match configuration
- Faceting support with string, number, and date types
- Facet operator mode for advanced aggregations
- Score boosting and scoring functions
- Count configuration (lowerBound/total)
- More like this search
- Build as $search or $searchMeta stages
- Comprehensive error handling with AtlasSearchError

#### Testing
- Comprehensive test suite with 90%+ coverage
- Tests for QueryFilter (50+ test cases)
- Tests for AggregateBuilder (40+ test cases)
- Tests for AtlasSearchBuilder and CompoundBuilder (30+ test cases)
- Unit tests for all operators and methods
- Error handling tests

#### Documentation
- Comprehensive README with examples
- API documentation with type hints
- Real-world usage examples
- Contributing guidelines
- Development setup instructions

#### Project Infrastructure
- Modern Python packaging with pyproject.toml
- Setup.py for backward compatibility
- GitHub Actions CI/CD workflow
- Code quality tools: black, isort, flake8, mypy, pylint
- Makefile for common development tasks
- Requirements files for dependencies
- MIT License
- .gitignore for Python projects

### Features Highlights

- **Type Safety**: Full type hints throughout the codebase
- **Validation**: Built-in validation for all operations
- **Error Messages**: Clear, helpful error messages
- **Chainable API**: Fluent, chainable method calls
- **Python 3.8+**: Support for Python 3.8 through 3.12
- **Zero Breaking Changes**: Stable API from v1.0.0
- **Well Tested**: Comprehensive test coverage
- **Documentation**: Extensive documentation and examples

### Planned Features
- Additional aggregation operators ($densify, $fill, etc.)
- Enhanced Atlas Search features (geoWithin, geoShape)
- Async/await support with motor
- Performance optimizations for large pipelines
- Additional tutorials (Aggregation, Atlas Search, Advanced Patterns)
- Cookbook with real-world examples
- Type stub files for better IDE support

---

[1.0.0]: https://github.com/ch-dev401/mongodb-query-builder/releases/tag/v1.0.0
