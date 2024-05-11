class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    #space before string is intentional idk why
    def props_to_html(self):
        edited_str = ''
        for key, value in self.props.items():
            edited_str += f' {key}="{value}"'
        return edited_str
    
    def __repr__(self):
        return f"HTMLNode\nself.tag = {self.tag},\nself.value = {self.value},\nself.children = {self.children},\nself.props = {self.props}"
    
def main():
    sam = HTMLNode('1', '2', '3', {"href": "https://www.google.com", "target": "_blank"})
    print(sam.props_to_html())
    print(sam.__repr__())

main()