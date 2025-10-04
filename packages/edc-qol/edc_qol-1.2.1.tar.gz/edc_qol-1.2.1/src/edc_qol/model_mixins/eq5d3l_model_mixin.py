from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from ..choices import (
    ANXIETY_DEPRESSION,
    MOBILITY,
    PAIN_DISCOMFORT,
    SELF_CARE,
    USUAL_ACTIVITIES,
)


class Eq5d3lModelMixin(models.Model):
    mobility = models.CharField(verbose_name="Mobility", max_length=45, choices=MOBILITY)

    self_care = models.CharField(verbose_name="Self-care", max_length=45, choices=SELF_CARE)

    usual_activities = models.CharField(
        verbose_name=_("Usual activities"),
        max_length=45,
        help_text=_("Example. work, study, housework, family or leisure activities"),
        choices=USUAL_ACTIVITIES,
    )

    pain_discomfort = models.CharField(
        verbose_name=_("Pain / Discomfort"), max_length=45, choices=PAIN_DISCOMFORT
    )

    anxiety_depression = models.CharField(
        verbose_name=_("Anxiety / Depression"),
        max_length=45,
        choices=ANXIETY_DEPRESSION,
    )

    health_today_score_slider = models.CharField(
        verbose_name=_("Visual score for how your health is TODAY"),
        max_length=3,
    )

    health_today_score_confirmed = models.IntegerField(
        verbose_name=mark_safe(  # noqa: S308
            _(
                "<B><font color='orange'>Interviewer</font></B>: "
                "please confirm the number on the scale indicated from above."
            )
        ),
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=mark_safe(  # noqa: S308
            _(
                "This scale is numbered from 0 to 100. "
                "100 means the <U>best</U> health you can imagine"
                "0 means the <U>worst</U> health you can imagine."
            )
        ),
    )

    class Meta:
        abstract = True
        verbose_name = _("EuroQol EQ-5D-3L Instrument")
        verbose_name_plural = _("EuroQol EQ-5D-3L Instrument")
