class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('Not implemented')
    

    def props_to_html(self):
        if self.props is None:
            return ""
        edited_str = ''
        for key, value in self.props.items():
            edited_str += f' {key}="{value}"'
        return edited_str
    
    
    def __repr__(self):
        return f"HTMLNode\nself.tag = {self.tag},\nself.value = {self.value},\nself.children = {self.children},\nself.props = {self.props}"
    
# children node inside a parent node, representing nesting HTML tags
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"\nLeafNode\nself.tag = {self.tag},\nself.value = {self.value},\nself.props = {self.props}"

# highest level <tag>
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag provided")
        if self.children == None:
            raise ValueError("No children provided")
        html_str = ""
        for i in range(len(self.children)):
            html_str += f"{self.children[i].to_html()}"
        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode\nself.tag = {self.tag},\nself.children =\n{self.children}\nself.props = {self.props}"
