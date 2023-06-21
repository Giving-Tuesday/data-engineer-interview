from etl.test_job import TestJob

if __name__ == '__main__':
  test_job = TestJob(init_conf={'path': None})
  test_job.launch()