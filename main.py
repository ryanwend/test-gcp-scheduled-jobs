#%%
from doh_tools.custom_logging import set_logging, send_log_over_email
import os

#%% Set up Logging
log_email = os.environ['gmail_user']
task_name = 'Test GCP Scheduled Jobs'
email_flag = 'LogLabel15'

subject_success = f'Success -- {task_name} Ran -- {email_flag}'
subject_error   = f'Error -- {task_name} Failed -- {email_flag}'

logger = set_logging(log_console=False, log_email=True)


#%% Add some logs
try:

    for i in range (1, 5):
        logger.info(f'Test Line {i}')
   

    send_log_over_email(
            logger,
            fromaddr=log_email,
            toaddr=log_email,
            subject=subject_success
        )

except Exception as e:
    logger.info(f'Process failed with error: {e}')
    send_log_over_email(
        logger,
        fromaddr=log_email,
        toaddr=log_email,
        subject=subject_error
    )

