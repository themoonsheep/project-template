import datetime

from moonsheep.tasks import AbstractTask
from moonsheep import verifiers

from .forms import *
from .models import *


class TaskWithForm(AbstractTask):
    # task_template = 'task.html'
    task_form = SimpleForm
    # task_form_template = 'tasks/simple.html'

    # verify_page = EqualsVerifier
    #
    # def verify_party_name(self, values):
    #     return values[0], 1
    #
    # def save_verified_data(self, verified_data):
    #     party, created = PoliticalParty.objects.get_or_create(
    #         name=verified_data['party_name'],
    #         legal_id=verified_data['party_legal_id']
    #     )
    #     Report.objects.get_or_create(
    #         report_date=datetime.datetime.strptime(verified_data['report_date'], "%Y-%m-%d"),
    #         party=party,
    #         document_page_start=verified_data['page']
    #     )
    #
    # def after_save(self, verified_data):
    #     self.create_new_task(GetTransactionTask, **verified_data)

    def get_presenter(self):
        """
        Choosing how to render document to transcribe.

        If defined overrides the default behaviour that choose document based on:
        1. Known url templates for YouTube, Vimeo, etc.
        2. Url file extension: .pdf, .png, etc.

        :return: {
            'template': 'presenters/fancy.html',
            'url': self.url,
            'other_presenter_option': 'width: 110px'
        }
        """
        return super(TaskWithForm, self).get_presenter()


class TaskWithTemplate(AbstractTask):
    # task_template = 'task.html'
    # task_form = SimpleForm
    task_form_template = 'tasks/with_template.html'

    # verify_title = verifiers.equals
    # verifiers.GeoProximity(10, "lat", "long")  # TODO
