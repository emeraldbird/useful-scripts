#!/usr/bin/python3
from datetime import datetime, timedelta
from typing import List, Tuple
import ssl
import OpenSSL


DAYS = 30

HOSTS = [
    'google.com',
    'yandex.ru',
    'duckduckgo.com',
  # Add your hosts there
]

UP_TO_DATE: List[Tuple[str, datetime]] = []
ALMOST_EXPIRED: List[Tuple[str, datetime]] = []
EXPIRED: List[Tuple[str, datetime]] = []
ERRORS: List[Tuple[str, Exception]] = []


def check():

    date_format, encoding = '%Y%m%d%H%M%SZ', 'ascii'

    for host in HOSTS:
        try:
            cert = ssl.get_server_certificate((host, 443))
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

            not_after = datetime.strptime(x509.get_notAfter().decode(encoding), date_format)

        except ssl.SSLError as error:
            ERRORS.append((host, error))
            continue

        else:
            expires_in = not_after - datetime.now()

            if not_after < datetime.now():
                EXPIRED.append((host, not_after))

            elif expires_in < timedelta(days=DAYS):
                ALMOST_EXPIRED.append((host, not_after))

            else:
                UP_TO_DATE.append((host, not_after))

def main():
    check()

    for key, value in {
            'UP TO DATE': UP_TO_DATE,
            'ALMOST EXPIRED': ALMOST_EXPIRED,
            'EXPIRED': EXPIRED,
            'ERRORS': ERRORS
        }.items():
        print(f'[{key}]')
        for host_tuple in value:
            print('  ', *host_tuple)
        print()


if __name__ == '__main__':
    main()
