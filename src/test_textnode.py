import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_w_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "Kitty.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "Kitty.com")
        self.assertEqual(node, node2) 

    def test_differing_markdown(self):
        node = TextNode("This is a text node", TextType.ITALIC,"KITTY")
        node2 = TextNode("This is a text node", TextType.BOLD,"KITTY")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
