import datetime
import json


class KSTCloudLogger:

    def log_entry(SourceProcessName, CorrelationID, logSeverity, log_detail, context = None, Additional = None):
        logMessage = None
        if context != None:
            logstream = context.log_stream_name
            loggroup = context.log_group_name
            requestid = context.aws_request_id
            if Additional != None:
                Additional = str(Additional)
                Additional = Additional.replace("{",", ")
                Additional = Additional.replace("}","")
                Additional = Additional.replace("'","\"")
                logMessage = '{"SourceProcessName": "' + SourceProcessName + '", "log_timestamp_utc": "' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '", "log_severity": "' + logSeverity + '", "CorrelationID": "' + CorrelationID + '", "log_stream_name": "' + logstream + '", "log_group_name": "' + loggroup + '", "log_request_id": "' + requestid + '", "log_detail": "' + log_detail + '"' + Additional + '}'
            else:
                logMessage = '{"SourceProcessName": "' + SourceProcessName + '", "log_timestamp_utc": "' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '", "log_severity": "' + logSeverity + '", "CorrelationID": "' + CorrelationID + '", "log_stream_name": "' + logstream + '", "log_group_name": "' + loggroup + '", "log_request_id": "' + requestid + '", "log_detail": "' + log_detail + '"}'
            json.loads(logMessage)
            print(logMessage)
        else:
            if Additional != None:
                Additional = str(Additional)
                Additional = Additional.replace("{",", ")
                Additional = Additional.replace("}","")
                Additional = Additional.replace("'","\"")
                logMessage = '{"SourceProcessName": "' + SourceProcessName + '", "log_timestamp_utc": "' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '", "log_severity": "' + logSeverity + '", "CorrelationID": "' + CorrelationID + '", "log_detail": "' + log_detail + '"' + Additional + '}'
            else:
                logMessage = '{"SourceProcessName": "' + SourceProcessName + '", "log_timestamp_utc": "' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '", "log_severity": "' + logSeverity + '", "CorrelationID": "' + CorrelationID + '", "log_detail": "' + log_detail + '"}'
            json.loads(logMessage)
            print(logMessage)            

