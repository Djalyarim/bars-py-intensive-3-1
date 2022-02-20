import unittest

from implementation import (
    get_numbers,
)


class MyTestCase(unittest.TestCase):
    def test_get_numbers(self):
        numbers = [
            1001, 1008, 1022, 1029, 1036, 1043, 1057, 1064, 1071, 1078, 1092, 1099, 1106, 1113, 1127, 1134, 1141,
            1148, 1162, 1169, 1176, 1183, 1197, 1204, 1211, 1218, 1232, 1239, 1246, 1253, 1267, 1274, 1281, 1288, 1302,
            1309, 1316, 1323, 1337, 1344, 1351, 1358, 1372, 1379, 1386, 1393, 1407, 1414, 1421, 1428, 1442, 1449, 1456,
            1463, 1477, 1484, 1491, 1498, 1512, 1519, 1526, 1533, 1547, 1554, 1561, 1568, 1582, 1589, 1596, 1603, 1617,
            1624, 1631, 1638, 1652, 1659, 1666, 1673, 1687, 1694, 1701, 1708, 1722, 1729, 1736, 1743, 1757, 1764, 1771,
            1778, 1792, 1799, 1806, 1813, 1827, 1834, 1841, 1848, 1862, 1869, 1876, 1883, 1897, 1904, 1911, 1918, 1932,
            1939, 1946, 1953, 1967, 1974, 1981, 1988
        ]

        self.assertEqual(list(get_numbers()), numbers)


if __name__ == '__main__':
    unittest.main()
