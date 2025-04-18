from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        from django.conf import settings
        from django.db.models.signals import post_save
        from django.dispatch import receiver
        from rest_framework.authtoken.models import Token
        from accounts.models import User

        @receiver(post_save, sender=User)
        def create_auth_token(sender, instance=None, created=False, **kwargs):
            if created:
                Token.objects.create(user=instance)
