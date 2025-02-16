import unittest

from htmlnode import HTMLNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", "I can't believe it's not butter!", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("<a>", "I can't believe it's not butter!", None, {"href": "https://www.google.com"})       
        print(node)

    def test_compat(self):
        node3 = TextNode("This is a text node", TextType.BOLD, "Kitty.com")
        node4 = TextNode("This is a text node", TextType.IMAGE, "Kitty.com")
        node5 = TextNode("This is a text node", TextType.BOLD)
        print("===========================")
        print(text_node_to_html_node(node3))
        print(text_node_to_html_node(node4))
        print(text_node_to_html_node(node5))

if __name__ == "__main__":
    unittest.main()
