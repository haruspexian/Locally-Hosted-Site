from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        if(tag == None):
            raise ValueError("Value mandatory on leftnode")
        if(children == None):
            raise ValueError("Children mandatory for ParentNode")

        super().__init__(tag, None, children, props)
    def to_html(self):
        ret_string = ""
        for child in self.children:
            ret_string = ret_string + f"{child.to_html()}"
        return f"<{self.tag}>{ret_string}</{self.tag}>"

