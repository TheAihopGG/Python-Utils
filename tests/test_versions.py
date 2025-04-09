import unittest
from python_utils import versions  # type: ignore


class TestVersions(unittest.TestCase):
    """docstring for TestVersions."""

    def test_init(self):
        self.assertTrue(versions.Version(1, 0, 0, versions.StringParts.BETA))

    def test_operators(self):
        version1 = versions.Version(1, 0, 0, versions.StringParts.BETA)
        version2 = versions.Version(2, 0, 0, versions.StringParts.BETA)
        self.assertTrue(version1 < version2)
        self.assertFalse(version1 > version2)

        version3 = versions.Version(3, 0, 0, versions.StringParts.BETA)
        version4 = versions.Version(3, 0, 0, versions.StringParts.BETA)
        self.assertTrue(version3 <= version4)
        self.assertTrue(version3 >= version4)

        self.assertEqual(version3, version4)
        self.assertNotEqual(version1, version4)

    def test_parsing(self):
        version1 = versions.Version(1, 0, 0, versions.StringParts.BETA)
        self.assertEqual(str(version1), "1.0.0beta")
        self.assertEqual(versions.Version.from_string("1.0.0beta"), version1)


if __name__ == "__main__":
    unittest.main()
