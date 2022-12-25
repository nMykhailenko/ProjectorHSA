# Send events to Google Analytics

## Run app
```
Replace tid in app.py file for your own 'UA-XXXXXXXXX-X'
docker build -t currency_exchange
docker run currency_exchange
```

```
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 756, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'CHF-UAH', 'ev': '39.3465'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 818, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'EGP-UAH', 'ev': '1.4774'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 826, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'GBP-UAH', 'ev': '44.1292'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 840, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'USD-UAH', 'ev': '36.5686'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 933, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'BYN-UAH', 'ev': '13.2919'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 944, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'AZN-UAH', 'ev': '21.5515'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 946, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'RON-UAH', 'ev': '7.9167'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 949, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'TRY-UAH', 'ev': '1.9571'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 960, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'XDR-UAH', 'ev': '48.6877'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 975, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'BGN-UAH', 'ev': '19.8537'}
<Response [200]>
{'v': '1', 'tid': 'UA-252690406-1', 'cid': 978, 't': 'event', 'ec': 'currency', 'ea': 'exchange', 'el': 'EUR-UAH', 'ev': '38.834'}
<Response [200]>
```

## Real Time Events in Google Analytics
![Real-time](https://user-images.githubusercontent.com/11583344/209483842-a1920e8e-591a-4b81-a7a4-ba1680eaf8b8.png)

## USD-UAH currency
![Exchange](https://user-images.githubusercontent.com/52753625/188312892-a06b9119-06bd-4c49-b19a-fe2236ea3cbe.PNG)
