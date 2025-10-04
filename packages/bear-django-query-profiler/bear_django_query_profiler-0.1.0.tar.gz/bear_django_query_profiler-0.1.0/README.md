# Django Query Profiler

A simple Django middleware to log SQL queries executed during a request. This middleware is active only when `DEBUG = True`.

## Installation

```bash
pip install bear-django-query-profiler
```

## Usage

1.  Add the middleware to your `MIDDLEWARE` list in `settings.py`. It should be placed after any other middleware that might generate queries.

    ```python
    # settings.py
    MIDDLEWARE = [
        # ... other middleware
        'query_profiler.middleware.QueryProfilerMiddleware',
    ]
    ```

2.  (Optional) You can specify a list of string patterns to ignore in the logs. Any query containing one of these patterns will not be logged.

    ```python
    # settings.py
    QUERY_PROFILER_IGNORE_PATTERNS = ['global_system_logs', 'django_session']
    ```

3.  Ensure your logging is configured to display `DEBUG` level messages.