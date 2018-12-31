import unittest

from reference import polyval, s2i, i2s


class PolyvalTest(unittest.TestCase):
    def _test(self, s, h, x):
        assert s == i2s(polyval(s2i(h), map(s2i, x)))

    def test_1(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'00000000000000000000000000000000']
        s = b'00000000000000000000000000000000'
        self._test(s, h, x)

    def test_2(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'01000000000000000000000000000000',
             b'00000000000000004000000000000000']
        s = b'eb93b7740962c5e49d2a90a7dc5cec74'
        self._test(s, h, x)

    def test_3(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'01000000000000000000000000000000',
             b'00000000000000006000000000000000']
        s = b'48eb6c6c5a2dbe4a1dde508fee06361b'
        self._test(s, h, x)

    def test_4(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'01000000000000000000000000000000',
             b'00000000000000008000000000000000']
        s = b'20806c26e3c1de019e111255708031d6'
        self._test(s, h, x)

    def test_5(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'01000000000000000000000000000000',
             b'02000000000000000000000000000000',
             b'00000000000000000001000000000000']
        s = b'ce6edc9a50b36d9a98986bbf6a261c3b'
        self._test(s, h, x)

    def test_6(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'01000000000000000000000000000000',
             b'02000000000000000000000000000000',
             b'03000000000000000000000000000000',
             b'00000000000000008001000000000000']
        s = b'81388746bc22d26b2abc3dcb15754222'
        self._test(s, h, x)

    def test_7(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'01000000000000000000000000000000',
             b'02000000000000000000000000000000',
             b'03000000000000000000000000000000',
             b'04000000000000000000000000000000',
             b'00000000000000000002000000000000']
        s = b'1e39b6d3344d348f6044f89935d1cf78'
        self._test(s, h, x)

    def test_8(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'01000000000000000000000000000000',
             b'02000000000000000000000000000000',
             b'08000000000000004000000000000000']
        s = b'b26781e7e2c1376f96bec195f3709b2a'
        self._test(s, h, x)

    def test_9(self):
        h = b'd9b360279694941ac5dbc6987ada7377'
        x = [b'01000000000000000000000000000000',
             b'02000000000000000000000000000000',
             b'03000000000000000000000000000000',
             b'04000000000000000000000000000000',
             b'05000000000000000000000000000000',
             b'08000000000000000002000000000000']
        s = b'ffcd05d5770f34ad9267f0a59994b15a'
        self._test(s, h, x)

    def test_10(self):
        h = b'8a51df64d93eaf667c2c09bd454ce5c5'
        x = [b'046787f3ea22c127aaf195d189472800',
             b'1177441f195495860f00000000000000',
             b'78000000000000004800000000000000']
        s = b'63a3451c0b23345ad02bba59956517cf'
        self._test(s, h, x)


if __name__ == '__main__':
    unittest.main()
