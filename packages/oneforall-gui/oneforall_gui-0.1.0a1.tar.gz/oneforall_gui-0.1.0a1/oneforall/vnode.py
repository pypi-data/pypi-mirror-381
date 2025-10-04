from typing import Any, Dict, List, Optional, Union


class VNode:
    def __init__(
        self,
        tag: str,
        props: Optional[Dict[str, Any]] = None,
        children: Optional[List[Union["VNode", str]]] = None,
    ):
        self.tag: str = tag
        self.props: Dict[str, Any] = props or {}
        self.children: List[Union["VNode", str]] = children or []

    def __eq__(self, other):
        if not isinstance(other, VNode):
            return False
        return (
            self.tag == other.tag
            and self.props == other.props
            and self.children == other.children
        )

    def to_html(self) -> str:
        props_str = " ".join(f'{k}="{v}"' for k, v in self.props.items())
        children_html = "".join(
            c.to_html() if isinstance(c, VNode) else str(c) for c in self.children
        )
        return f"<{self.tag} {props_str}>{children_html}</{self.tag}>"
