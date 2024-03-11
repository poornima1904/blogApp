from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from streams import blocks as my_blocks

class BlogPage(Page):
    heading_block = StreamField(
        [
            ("heading_block", my_blocks.HeadingBlock())
        ],
        null=True,
        blank=True,
    )
    blogs_block = StreamField(
        [
            ("blogs_block", my_blocks.BlogsBlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("heading_block"),
        FieldPanel("blogs_block"),
    ]

class Blog(Page):
    template = "blog/blog.html"
    content = StreamField(
        [
            ('title', blocks.CharBlock(icon='title')),
            ('byline', blocks.StructBlock([
            ('date', blocks.DateTimeBlock(icon='date', classname='date')),
            ('time_to_read', blocks.CharBlock(icon='time', classname='time', required=False)),
            ])),
            
            ('section_heading', blocks.CharBlock(icon='title', classname='title')),
            ('subtitle', blocks.CharBlock(icon='title', classname='title')),
            ('body', blocks.RichTextBlock(icon='pilcrow', classname='full')),
            ('image', ImageChooserBlock(icon='image', classname='image')),

            ('author', blocks.StructBlock([
                ('name', blocks.CharBlock(icon='user', classname='user')),
                ('bio', blocks.RichTextBlock(icon='pilcrow', classname='full')),
                ('image', ImageChooserBlock(icon='image', classname='image')),
            ], icon='user', classname='user')),

        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]
