import csv

from winsys import event_logs

csv.writer (open ("06.csv", "wb")).writerows (
  (event.record_number, event.time_generated, event.event_id, event.message) for
    event in event_logs.event_log ("system")
)
