from abc import ABC, abstractmethod
import logging
from argparse import ArgumentParser
import pathlib
import sys
import yaml

class Task(ABC):

  def __init__(self, init_conf=None):
    self.logger = self._prepare_logger()
    if init_conf:
      self.conf = init_conf
    else:
      self.conf = self._provide_config()

  def _prepare_logger(self):
    return logging.getLogger(self.__class__.__name__)

  def _provide_config(self):
    self.logger.info("Reading configuration from --conf-file job option")
    conf_file = self._get_conf_file()
    if not conf_file:
      self.logger.info(
        "No conf file was provided, setting configuration to empty dict."
        "Please override configuration in subclass init method"
      )
      return {}

    self.logger.info(f"Conf file was provided, reading configuration from {conf_file}")
    return self._read_config(conf_file)

  @staticmethod
  def _get_conf_file():
    parser = ArgumentParser()
    parser.add_argument("--conf-file", required=False, type=str)
    namespace = parser.parse_known_args(sys.argv[1:])[0]
    return namespace.conf_file

  @staticmethod
  def _read_config(conf_file):
    config = yaml.safe_load(pathlib.Path(conf_file).read_text("UTF-8"))
    return config


  @abstractmethod
  def launch(self):
    """
    Main method of the job.
    :return:
    """