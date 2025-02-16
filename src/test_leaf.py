import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "I can't believe it's not butter!", None, {"href": "https://www.google.com"})
        node2 = LeafNode("p", "Nunya BeezWax!", None, None)       
        print(node.to_html())
        print(node2.to_html())



if __name__ == "__main__":
    unittest.main()
