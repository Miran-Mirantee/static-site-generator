import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        
    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node_1 = LeafNode("b", "child_1")
        child_node_2 = LeafNode("b", "child_2")
        child_node_3 = LeafNode("b", "child_3")
        parent_node = ParentNode("div", [child_node_1, child_node_2, child_node_3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child_1</b><b>child_2</b><b>child_3</b></div>",
        )
    
if __name__ == "__main__":
    unittest.main()