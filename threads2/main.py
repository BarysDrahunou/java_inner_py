import queue
from concurrent.futures.thread import ThreadPoolExecutor
from configparser import NoOptionError
from readers.TrialReader import TrialReader
from readerwriterfactory import TrialWriterFactory
from readerwriterfactory.TrialReadersFactory import TrialReadersFactory
from utils.ExceptionHandling import get_logger_
from utils.ReaderWriterConstants import CONFIG_FILE_NAME, READER_WRITER_GROUP, \
    READER_IN_CONFIG, WRITER_IN_CONFIG, QUEUE_SIZE
from writers.TrialWriter import TrialWriter

logger = get_logger_()
blocking_queue = queue.Queue(QUEUE_SIZE)
try:
    all_trial_dao = TrialReadersFactory().get_trial_dao(CONFIG_FILE_NAME,
                                                        READER_WRITER_GROUP, READER_IN_CONFIG)
    with TrialWriterFactory.get_consumer(CONFIG_FILE_NAME, READER_WRITER_GROUP,
                                         WRITER_IN_CONFIG) as trial_consumer, \
            ThreadPoolExecutor(max_workers=len(all_trial_dao)) as e:
        for trial_dao in all_trial_dao:
            trial_reader = TrialReader(blocking_queue, trial_dao)
            e.submit(trial_reader.run)
        trial_writer = TrialWriter(blocking_queue, trial_consumer, len(all_trial_dao))
        trial_writer.go()
except (FileNotFoundError, ValueError, NoOptionError) as e:
    logger.error(e)
