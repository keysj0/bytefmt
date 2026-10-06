# bytefmt

Convert an integer byte count to a short label, and parse that label back.

Uses 1024-based steps: `B`, `KB`, `MB`, `GB`, `TB`.

```python
from bytefmt import format_bytes, parse_bytes, is_bytes, sum_bytes, greater_than, lesser

format_bytes(1536)     # "1.5 KB"
parse_bytes("2MB")     # 2097152
is_bytes("2MB")        # True
sum_bytes("1 KB", "512 B")  # 1536
greater_than("2MB", "1 KB")  # True
```

```bash
python -m unittest test_bytefmt.py
```

MIT
