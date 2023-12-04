from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtailcache.cache import WagtailCacheMixin
from wagtailmetadata.models import MetadataPageMixin

from home.blocks import InfoBlock, FeatureBlock, DatasetCategoryBlock


class HomePage(MetadataPageMixin, WagtailCacheMixin, Page):
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("Banner Image"),
        help_text=_("A high quality banner image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    banner_title = models.CharField(max_length=255, verbose_name=_('Banner Title'))
    banner_subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Banner Subtitle'))

    intro_text = RichTextField(blank=True, null=True, features=["bold"], verbose_name=_('Introduction text'),
                               help_text=_("Introduction section description"))
    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_("Introduction Image"),
        help_text=_("A high quality image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    info_blocks = StreamField(
        [
            ("info", InfoBlock(label=_("Info"))),

        ],
        null=True,
        blank=True,
        use_json_field=True,
        verbose_name=_("Info Section"),
    )

    feature_blocks = StreamField(
        [
            ("feature", FeatureBlock(label=_("Feature")),),

        ],
        null=True,
        blank=True,
        use_json_field=True,
        verbose_name=_("Features"),
    )

    dataset_blocks = StreamField(
        [
            ("category", DatasetCategoryBlock(label=_("Dataset Category")),),

        ],
        null=True,
        blank=True,
        use_json_field=True,
        verbose_name=_("Available Datasets"),
    )

    content_panels = Page.content_panels + [

        MultiFieldPanel(
            [
                FieldPanel('banner_title'),
                FieldPanel('banner_subtitle'),
                FieldPanel('banner_image'),
            ],
            heading=_("Banner Section"),
        ),

        MultiFieldPanel(
            [
                FieldPanel('intro_text'),
                FieldPanel('intro_image'),
            ],
            heading=_("Introduction Section"),
        ),

        FieldPanel('info_blocks'),
        FieldPanel('feature_blocks'),
        FieldPanel('dataset_blocks'),
    ]
