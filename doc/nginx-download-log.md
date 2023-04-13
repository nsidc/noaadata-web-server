
## Configuring the nginx download log

The nginx download logs are configured in `nginx/nginx.conf` and `nginx/default.conf`.

Ideally it would be possible to filter with 2 conditions so that the logs contain
only downloads that have success status (200).

Below is what was attempted in `default.conf`

```    
    set $log_sentinel 0;
    set $logme 0;
    if ( $status ~ ^[2].* ) {
          set $log_sentinel status_ok;
    }
    if ( $uri ~ ^(?:/favicon\.ico)$(*SKIP)(*F)|^.*[^/]$ ) {
          set $log_sentinel "${log_sentinel}_uri_ok";
    }
    if ( $log_sentinel = ok ) {
        set $logme 1;
    }
```
