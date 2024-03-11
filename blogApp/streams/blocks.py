from wagtail import blocks

class HeadingBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="Add your heading text")
    date = blocks.DateBlock(required=True, help_text="Add the date")
    total_blogs = blocks.IntegerBlock(required=True, help_text="Add the total")

    class Meta:
        template = "streams/heading_block.html"
        icon = "title"
        label = "Heading"

class BlogsBlock(blocks.StructBlock):
    blogs = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("type", blocks.CharBlock(required=True, max_length=20)),
                ("title", blocks.CharBlock(required=True, max_length=100)),
                ("body", blocks.TextBlock(required=True, max_length=250)),
                ("date", blocks.DateBlock(required=True)),  
            ]
        )
    )

    class Meta:
        template = "streams/blogs_block.html"
        icon = "edit"
        label = "Blogs" 