from django import forms
from edc_crf.crf_form_validator import CrfFormValidator
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_model.widgets import SliderWidget

from ..models import Eq5d3l


class Eq5d3lFormValidator(CrfFormValidator):
    def clean(self) -> None:
        self.confirm_scores_match()

    def confirm_scores_match(self):
        confirmed = self.cleaned_data.get("health_today_score_confirmed")
        if (
            confirmed is not None
            and int(self.cleaned_data.get("health_today_score_slider", "0")) != confirmed
        ):
            raise forms.ValidationError(
                {"health_today_score_confirmed": "Does not match visual scale above."}
            )


class Eq5d3lForm(CrfModelFormMixin, forms.ModelForm):
    form_validator_cls = Eq5d3lFormValidator

    health_today_score_slider = forms.CharField(
        label="Health TODAY scale", widget=SliderWidget(attrs={"min": 0, "max": 100})
    )

    class Meta:
        model = Eq5d3l
        fields = "__all__"
