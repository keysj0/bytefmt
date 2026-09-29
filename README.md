# bytefmt

Convert an integer byte count to a short label, and parse that label back.

Uses 1024-based steps: `B`, `KB`, `MB`, `GB`, `TB`.

```python
from bytefmt import format_bytes, parse_bytes, is_bytes

format_bytes(1536)     # "1.5 KB"
parse_bytes("2MB")     # 2097152
is_bytes("2MB")        # True
```

```bash
python -m unittest test_bytefmt.py
```

MIT
