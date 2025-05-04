import requests
import logging

critical_logger = logging.getLogger('critical')
critical_handler = logging.FileHandler('check_status_txt.log')
critical_formatter = logging.Formatter('[%(asctime)s - %(levelname)s - line:%(lineno)d] - %(message)s')
critical_handler.setFormatter(critical_formatter)
critical_logger.addHandler(critical_handler)
critical_logger.setLevel(logging.CRITICAL)

info_logger = logging.getLogger('info')
info_handler = logging.FileHandler('check_status_txt.log')
info_formatter = logging.Formatter('[%(asctime)s - line:%(lineno)d] - %(message)s')
info_handler.setFormatter(info_formatter)
info_logger.addHandler(info_handler)
info_logger.setLevel(logging.INFO)

def check_status():
    filename = input("Enter a txt file which be checked for urls in format 'txt.txt': ")
    info_logger.info(f"Filename='{filename}'")

    try:
        with open(filename, 'r') as file:
            urls = file.readlines()
            info_logger.info('Links were imported successfully')
            for url in urls:
                try:
                    response = requests.get(url)
                except requests.exceptions.InvalidSchema:
                    print("Check out your links for right format, maybe they are doesn't exist")
                    critical_logger.critical('InvalidSchema error')
                    info_logger.info('End of working...')
                except requests.exceptions.ConnectionError:
                    print('Please check out your internet connection, something went wrong...')
                    critical_logger.critical('ConnectionError error')
                    info_logger.info('End of working...')
                except requests.exceptions.Timeout:
                    print('Timeout has been occured')
                    critical_logger.critical('Timeout error')
                    info_logger.info('End of working...')
                print(f'Code of response from resource: {response.status_code}')
                info_logger.info(f'Successfully printed code of response from {url}')
    except FileNotFoundError:
        print("Txt file haven't been found, please check the file for existence")
        critical_logger.critical('FileNotFoundError error')
        info_logger.info('End of working...')

check_status()