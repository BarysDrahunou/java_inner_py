import threading
import queue

from readers.TrialReader import TrialReader
from readerwriterfactory import TrialReaderFactory, TrialWriterFactory
from utils.ReaderWriterConstants import CONFIG_FILE_NAME, READER_WRITER_GROUP, \
    READER_IN_CONFIG, WRITER_IN_CONFIG, \
    QUEUE_SIZE

from writers.TrialWriter import TrialWriter

blocking_queue = queue.Queue(QUEUE_SIZE)
trial_dao = TrialReaderFactory.get_trial_dao(CONFIG_FILE_NAME,
                                             READER_WRITER_GROUP, READER_IN_CONFIG)
trial_consumer = TrialWriterFactory.get_consumer(CONFIG_FILE_NAME,
                                                 READER_WRITER_GROUP, WRITER_IN_CONFIG)
trial_reader = TrialReader(blocking_queue, trial_dao)
trial_writer = TrialWriter(blocking_queue, trial_consumer)
threading.Thread(target=trial_reader.run).start()
trial_writer.go()
