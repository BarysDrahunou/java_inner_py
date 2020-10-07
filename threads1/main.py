import threading
from configparser import NoOptionError

from TrialBuffer.TrialBuffer import TrialBuffer
from readers.TrialReader import TrialReader
from readerwriterfactory import TrialReaderFactory, TrialWriterFactory
from utils.ExceptionHandling import get_logger_
from utils.ReaderWriterConstants import CONFIG_FILE_NAME, READER_WRITER_GROUP, \
    READER_IN_CONFIG, WRITER_IN_CONFIG

from writers.TrialWriter import TrialWriter

logger = get_logger_()
buffer = TrialBuffer()
try:
    trial_dao = TrialReaderFactory.get_trial_dao(CONFIG_FILE_NAME,
                                                 READER_WRITER_GROUP, READER_IN_CONFIG)
    with TrialWriterFactory.get_consumer(CONFIG_FILE_NAME,
                                         READER_WRITER_GROUP, WRITER_IN_CONFIG) \
            as trial_consumer:
        trial_reader = TrialReader(buffer, trial_dao)
        trial_writer = TrialWriter(buffer, trial_consumer)
        threading.Thread(target=trial_reader.run).start()
        trial_writer.go()
except (FileNotFoundError, ValueError, NoOptionError) as e:
    logger.error(e)
