from django.db import models


class ProfessionGalleryManager(models.Manager):
    def profession_gallery(self, item_id):
        return (
            self.get_queryset()
                .filter(item__id=item_id)
                .select_related('item')
                .order_by('item')
        )
