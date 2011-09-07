from django.template.defaultfilters import slugify

def _slugify_attr(sender, instance, attr):
    """
    Slugify an attribute of the sender
    """
    if not instance.pk:
        instance.slug = temp = instance.slug if instance.slug else slugify(getattr(instance, attr))
        i = 1
        while sender.objects.filter(slug=instance.slug).count():
            instance.slug = '%s%d' % (temp, i)
            i += 1

def slugify_name(sender, instance, *args, **kwargs):
    """
    create a slug based o the property name of the model
    """
    _slugify_attr(sender, instance, 'name')