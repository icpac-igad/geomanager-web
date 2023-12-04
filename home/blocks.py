from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from geomanager.models import Category
from wagtail import blocks
from wagtail.blocks import StructValue
from wagtail.images.blocks import ImageChooserBlock
from wagtailiconchooser.blocks import IconChooserBlock


class InfoBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, label=_('Section Title'),
                             help_text=_("Section title"), )
    text = blocks.RichTextBlock(features=["bold", "li", "ul"], label=_('Section Text'),
                                help_text=_("Section description"))
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "streams/title_text_image.html"
        icon = "placeholder"
        label = _("Title, Text and Image")


class FeatureBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, label=_('Title'), )
    icon = IconChooserBlock(label=_("Icon"))
    description = blocks.CharBlock(max_length=150, label=_('Description'), )


def get_dataset_categories():
    return [(cat.pk, cat.title) for cat in Category.objects.all()]


class DatasetCategoryBlockStructValue(StructValue):
    @cached_property
    def category_obj(self):
        category_pk = self.get("category")
        try:
            category = Category.objects.get(pk=category_pk)
            if category:
                return category
        except Exception:
            pass

        return None


class DatasetCategoryBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, label=_('Title'), )
    category = blocks.ChoiceBlock(
        choices=get_dataset_categories,
        label=_("Select Category"),
    )

    class Meta:
        value_class = DatasetCategoryBlockStructValue
