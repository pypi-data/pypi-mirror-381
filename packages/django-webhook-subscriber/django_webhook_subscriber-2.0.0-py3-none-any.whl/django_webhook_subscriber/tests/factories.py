import factory


class ContentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "contenttypes.ContentType"
        django_get_or_create = ("app_label", "model")

    app_label = factory.Faker("word")
    model = factory.Faker("word")


class WebhookSubscriberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "django_webhook_subscriber.WebhookSubscriber"
        django_get_or_create = ("target_url",)

    name = factory.Faker("company")
    description = factory.Faker("sentence")
    content_type = factory.SubFactory(ContentTypeFactory)
    target_url = factory.Faker("url")
    secret = factory.Faker("sha256")


class WebhookSubscriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "django_webhook_subscriber.WebhookSubscription"
        django_get_or_create = ("subscriber", "event_name")

    subscriber = factory.SubFactory(WebhookSubscriberFactory)
    event_name = factory.Faker("word")


class WebhookDeliveryLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "django_webhook_subscriber.WebhookDeliveryLog"

    subscription = factory.SubFactory(WebhookSubscriptionFactory)
    payload = factory.Faker("json")
    delivery_url = factory.Faker("url")
