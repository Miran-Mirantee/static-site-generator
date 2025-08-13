import unittest

from util import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word `another code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word ", TextType.TEXT),
            TextNode("another code block", TextType.CODE)
        ]
        self.assertEqual(new_nodes, expected_nodes)
        
    def test_bold(self):
        node = TextNode("**how bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("how bold", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected_nodes)
        
    def test_italic(self):
        node = TextNode("_italic_ and italian is **not** the same", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" and italian is **not** the same", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)