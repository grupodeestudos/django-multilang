
from django.template import Library, Node

register = Library()


class EchoNode(Node):
    def __init__(self, parser):
        self.parser = parser

    def render(self, context):
        return 'bla {0}, {1}'.format(context, self.parser)

@register.tag
def echotag(parser, token):
    return EchoNode(parser)
