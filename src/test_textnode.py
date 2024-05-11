import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold", "/f/f/f/f")
        node2 = TextNode("This is a text node", "bold", "/f/f/f/f")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", 'Dog')
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
