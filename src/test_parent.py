import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ],)   
        print(node.to_html())




if __name__ == "__main__":
    unittest.main()
