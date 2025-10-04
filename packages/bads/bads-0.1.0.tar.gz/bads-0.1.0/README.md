# bads

Simple threaded path scanner. Usage:

```py
from bads import h0rn3t

sites_file = "v.txt"
paths = ["robots.txt", "login.php", "admin/"]
check_texts = ["admin", "login", "sql error"]
threads = 5
output_file = "results.txt"

scanner = h0rn3t(sites_file, paths, check_texts, threads, output_file)
scanner.run()
```
