# statute-utils

![Github CI](https://github.com/justmars/statute-utils/actions/workflows/ci.yml/badge.svg)

Enables manipulation of Philippine statutory law, including features such as:

1. Pattern matching
2. Unit retrieval
3. Database creation
4. Template creation, i.e. using the database representation to

This relies on [prelawsql](https://github.com/justmars/prelawsql) for dependency functions.

## Run

```sh
just --list # see recipes
just dumpenv # set .env variables
builder # list pyproject.toml cli scripts
mkdocs serve # show docs
```

## Note

> [!IMPORTANT]
> When modifying a database structure, consider four inter-related parts:
>
> 1. The pythonic object, e.g. `NamedTuple`
> 2. The representation of such in the prospective database
> 3. The documentation of the pythonic object found in `/docs`
> 4. The use of all of the above in downstream [decision-utils](https://github.com/justmars/decision-utils).
