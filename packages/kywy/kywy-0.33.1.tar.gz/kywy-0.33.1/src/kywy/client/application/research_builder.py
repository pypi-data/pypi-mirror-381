from datetime import datetime

from .app_model import DataModel
from .app_reporter import Reporter
from .report_builder import ReportBuilder


class ResearchBuilder:

    def __init__(self, kawa_client, name, unique_tag=None):
        self._k = kawa_client
        self._tag = unique_tag or f'#{name}'
        self._name = name
        self._reporter = Reporter(name=name)
        self._models = []
        self._results = []
        self._report = None

    def publish_models(self):
        for model in self._models:
            model.sync()

    def publish_results(self, title, df):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entity_name = f'{title}  ({now})'
        loader = self._k.new_data_loader(
            df=df,
            datasource_name=entity_name
        )
        loader.create_datasource()
        loader.load_data(
            reset_before_insert=True,
            create_sheet=True
        )
        sheet_id = self._k.entities.sheets().get_entity_id(entity_name)
        return self.register_model(model_id=sheet_id)

    def register_result(self, title, df, description=None):
        self._results.append({
            'title': title,
            'description': description,
            'df': df,
        })

    def register_model(self, model_id):
        sheet = self._k.entities.sheets().get_entity_by_id(model_id)
        if not sheet:
            raise Exception(f'Sheet with id={model_id} not found')
        model = DataModel(
            kawa=self._k,
            reporter=self._reporter,
            name=sheet['displayInformation']['displayName'],
            sheet=sheet
        )
        self._models.append(model)
        return model

    def report(self):
        self._report = ReportBuilder(
            kawa_client=self._k,
            name=self._name,
            unique_tag=self._tag,
        )
        return self._report

    def _sync(self):
        for model in self._models:
            model.sync()
