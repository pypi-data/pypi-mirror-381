# SF3 Middleware - Currently transmissions are diabled

<!-- TODO - turn on thread transmissions -->

Middleware for Python (Django, Flask, and FastAPI) to intercept requests, print statements, logs, and exceptions while persisting tracing.

## Installation

Use Poetry to install:

```bash
poetry add sf-veritas
```

## Usage

### Django, etc

**Switch the following:**

```sh
python manage.py runserver 0.0.0.0:8000
```

**To:**

```sh
sf-veritas API-KEY python manage.py runserver 0.0.0.0:8000
```

## TODO - Rename all Sailfish artifacts to Sailfish.ai

## Network Hop Calculation Time

To evaluate the performance impact of this package, we benchmarked 1000 HTTP requests with and without the package enabled.

| Configuration     | Mean (ms) | Median (ms) | Std Dev (ms) |
|-------------------|-----------|-------------|--------------|
| ✅ With Package    | 79.12     | 54.00       | 111.18      |
| ❌ Without Package | 69.70     | 52.00       | 73.78       |

> ⚠️ Note: The package introduces a slight increase in mean response time and variance. This trade-off may be acceptable depending on the value the package provides (e.g., additional logging, monitoring, or security features).

---

## Optimized Entrypoint Capture (Post-Refactor)

After optimizing how the user-code entrypoint is captured (via faster stack inspection), we observed improved stability and performance across 1015 analyzed requests:

| Configuration     | Mean (ms) | Median (ms) | Std Dev (ms) |
|-------------------|-----------|-------------|--------------|
| ✅ With Package    | 142.45   | 138.50      | 80.78        |
| ❌ Without Package | 131.07   | 127.00      | 35.75        |

> ⚠️ The optimized implementation added a slight increase in mean latency (~8.7%), but this tradeoff is offset by improved accuracy of entrypoint capture.
---
