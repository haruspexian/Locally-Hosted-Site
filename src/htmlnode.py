from textnode import TextType

def text_node_to_html_node(text_node):   
    from leafnode import LeafNode
    if isinstance(text_node.text_type, TextType):
        match(text_node.text_type):
            case TextType.NORMAL:
                return LeafNode(None, text_node.text)
            case TextType.BOLD: 
                return LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                return LeafNode("a", text_node.text, props={"href":link})
            case TextType.IMAGE:
                if text_node.url != None:
                    return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
                else:
                    raise ValueError("Image text node must have url to convert.")
            case _:
                raise TypeError("TextNode must have valid TextType to convert") 


class HTMLNode:
    
    '''
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}?
    '''
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
     
    def to_html(self):
        raise Error (NotImplementedError)
    
    def props_to_html(self):
        if self.props is not None:
            pretty_props = " ".join(f"{key}={self.props[key]}" for key in self.props.keys())
            return f"{pretty_props}"
        else:
            return None

    def __repr__(self):
        if self.props is not None:
            pretty_props = " ".join(f"{key}={self.props[key]}" for key in self.props.keys())
            return f"{self.tag}, {self.value}, {self.children}, {pretty_props}"
        else:
            return f"{self.tag}, {self.value}, {self.children}, None"
