import requests
import logging

critical_logger = logging.getLogger('critical')
critical_handler = logging.FileHandler('check_status.log')
critical_formatter = logging.Formatter('[%(asctime)s - %(levelname)s - line:%(lineno)d] - %(message)s')
critical_handler.setFormatter(critical_formatter)
critical_logger.addHandler(critical_handler)
critical_logger.setLevel(logging.CRITICAL)

info_logger = logging.getLogger('info')
info_handler = logging.FileHandler('check_status.log')
info_formatter = logging.Formatter('[%(asctime)s - line:%(lineno)d] - %(message)s')
info_handler.setFormatter(info_formatter)
info_logger.addHandler(info_handler)
info_logger.setLevel(logging.INFO)

def check_status():
    url = input('Copy and paste url here for check: ')
    info_logger.info(f"Url={url}")

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Please check internet connection and try again...')
        critical_logger.critical('ConnectionError error')
        info_logger.info('End of working...')
    except requests.exceptions.Timeout:
        print('Timeout has been occured')
        critical_logger.critical('Timeout error')
        info_logger.info('End of working...')
    except requests.exceptions.InvalidSchema:
        print('Invalid URL or Unsupported URL, try something else')
        critical_logger.critical('InvalidSchema error')
        info_logger.info('End of working...')
    except requests.exceptions.MissingSchema:
        print('No scheme supplied, invalid format of URL')
        critical_logger.critical('MissingSchema error')
        info_logger.info('End of working...')
    except requests.exceptions.InvalidURL:
        print('Invalid URL has not been founded')
        critical_logger.critical('InvalidURL error')
        info_logger.info('End of working...')
    else:
        print(f'Response code from resource: {response.status_code}')
        info_logger.info('Successfully printed a code from url')

check_status()