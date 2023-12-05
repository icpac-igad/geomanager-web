# Generated by Django 4.2.7 on 2023-12-05 12:16

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailiconchooser.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='feature_blocks',
            field=wagtail.fields.StreamField([('feature', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Title', max_length=100)), ('icon', wagtailiconchooser.blocks.IconChooserBlock(label='Icon')), ('description', wagtail.blocks.CharBlock(label='Description', max_length=150))], label='Feature'))], blank=True, null=True, use_json_field=True, verbose_name='Features'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='info_blocks',
            field=wagtail.fields.StreamField([('info', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Section title', label='Section Title', max_length=100)), ('description', wagtail.blocks.CharBlock(label='Section Description', max_length=150, required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Item', max_length=150), label='Items')), ('image', wagtail.images.blocks.ImageChooserBlock())], label='Info'))], blank=True, null=True, use_json_field=True, verbose_name='Info Section'),
        ),
    ]
