from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django_audit_fields.admin import audit_fieldset_tuple

eq5d3l_description = """
<H5><B><font color="orange">Interviewer to read</font></B></H5>
<p>We would like to know how good or bad your health is TODAY.
<ul><li>This scale is numbered from 0 to 100;</li>
<li>100 means the <U>best</U> health you can imagine;</li>
<li>0 means the <U>worst</U> health you can imagine;</li>
<li>Drag the slider on the line below at the point
showing how your health is TODAY</li></ul>
<BR><BR>
</p>
"""


def eq5d3l_fieldsets():
    return [
        (
            "Describe your health TODAY ...",
            {
                "description": (
                    "Under each heading, please tick the ONE box "
                    "that best describes your health TODAY."
                ),
                "fields": (
                    "mobility",
                    "self_care",
                    "usual_activities",
                    "pain_discomfort",
                    "anxiety_depression",
                ),
            },
        ),
        (
            "How is your health TODAY?",
            {
                "description": format_html(
                    "{}",
                    mark_safe(eq5d3l_description),  # nosec B308, B703  # noqa: S308
                ),
                "fields": (
                    "health_today_score_slider",
                    "health_today_score_confirmed",
                ),
            },
        ),
    ]


def eq5d3l_radio_fields():
    return {
        "mobility": admin.VERTICAL,
        "self_care": admin.VERTICAL,
        "usual_activities": admin.VERTICAL,
        "pain_discomfort": admin.VERTICAL,
        "anxiety_depression": admin.VERTICAL,
    }


class Eq5d3lModelAdminMixin:
    form = None

    fieldsets = (
        (None, {"fields": ("subject_identifier", "report_datetime")}),
        *eq5d3l_fieldsets(),
        audit_fieldset_tuple,
    )

    radio_fields = eq5d3l_radio_fields()
