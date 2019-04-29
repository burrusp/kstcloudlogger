import datetime
import json


class KSTCloudLogger:

    def log_entry(SourceProcessName, CorrelationID, logSeverity, log_detail, context, Additional = None):
        logstream = context.log_stream_name
        loggroup = context.log_group_name
        requestid = context.aws_request_id
        logMessage = '{"SourceProcessName": "' + SourceProcessName + '", "log_timestamp_utc": "' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '", "log_severity": "' + logSeverity + '", "CorrelationID": "' + CorrelationID + '", "log_stream_name": "' + logstream + '", "log_group_name": "' + loggroup + '", "log_request_id": "' + requestid + '", "log_detail": "' + log_detail + '"}'
        json.loads(logMessage)
        if Additional != None:
            for item in Additional:
                logMessage[item] = Additional[item]
        print(logMessage)        

