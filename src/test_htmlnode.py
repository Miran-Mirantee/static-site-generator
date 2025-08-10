import unittest

from htmlnode import HTMLNode, LeafNode

class TextHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode('img', "", props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node.props_to_html(), ' src="image.png" alt="An image"')
    
    def test_props_to_html_2(self):
        node = HTMLNode('p', "hello boys", props={"style": "color: red", "class": "text"})
        self.assertEqual(node.props_to_html(), ' style="color: red" class="text"')
    
    def test_props_to_html_3(self):
        node = HTMLNode('a', "link", props={"href": "www.idiot.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.idiot.com" target="_blank"')
        
    def test_leaf_to_html_p_1(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_p_2(self):
        node = LeafNode("p", "MapleStoryM sucks Ass", props={"class": "text", "style": "background-color: red"})
        self.assertEqual(node.to_html(), '<p class="text" style="background-color: red">MapleStoryM sucks Ass</p>')
    
if __name__ == "__main__":
    unittest.main()