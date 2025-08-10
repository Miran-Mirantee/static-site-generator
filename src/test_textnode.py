import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(TextType.PLAIN, "Hello")
        node2 = TextNode(TextType.PLAIN, "Hello")
        self.assertEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()