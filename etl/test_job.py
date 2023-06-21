from etl.common import Task


class TestJob(Task):

    def launch(self):
        self.logger.info('Launching a test job!')
        with open('data_lake/raw/raw.csv', 'r') as f:
            raw_data = f.readlines()
        for row in raw_data:
            print(row.rstrip().split(','))
