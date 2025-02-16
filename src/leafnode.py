from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, children=None, props=None):
        if(value == None):
            raise ValueError("Value mandatory on leftnode")
        super().__init__(tag, value, children, props)
    def to_html(self):
        if self.tag != None:
            if self.props == None:
                return  f"<{self.tag}>{self.value}</{self.tag}>"  
            else:
                pretty_props = " ".join(f"{key}=\"{self.props[key]}\"" for key in self.props.keys()) 
                return  f'<{self.tag}{' ' + pretty_props}>{self.value}</{self.tag}>' 
        else:
            return f"{self.value}"

