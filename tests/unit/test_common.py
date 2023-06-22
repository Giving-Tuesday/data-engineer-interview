from etl.common import Task


def test_task():
    class FakeTask(Task):
        output = None

        def launch(self):
            self.logger.info('Launching a fake job!')
            with open(self.conf['raw_data_path'], 'r') as f:
                raw_data = f.readlines()
                self.output = len(raw_data)

    task = FakeTask(init_conf={'raw_data_path': 'tests/fixtures/raw.csv'})
    task.launch()
    assert task.output == 3
