import unittest

from bytefmt import format_bytes, greater_than, is_bytes, parse_bytes, sum_bytes


class BytefmtTest(unittest.TestCase):
    def test_format(self) -> None:
        self.assertEqual(format_bytes(0), "0 B")
        self.assertEqual(format_bytes(1536), "1.5 KB")
        self.assertEqual(format_bytes(1024), "1 KB")

    def test_parse(self) -> None:
        self.assertEqual(parse_bytes("1.5 KB"), 1536)
        self.assertEqual(parse_bytes("2MB"), 2 * 1024 * 1024)
        self.assertTrue(is_bytes("2MB"))
        self.assertFalse(is_bytes("soon"))
        self.assertEqual(sum_bytes("1 KB", "512 B"), 1536)
        self.assertTrue(greater_than("2MB", "1 KB"))
        self.assertFalse(greater_than("1 KB", "2MB"))
        with self.assertRaises(ValueError):
            sum_bytes()


if __name__ == "__main__":
    unittest.main()
