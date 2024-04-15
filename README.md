# Настройка телеграм бота - расписания

### https://ramziv.com/article/38
### https://habr.com/ru/companies/ruvds/articles/786014/
 

```
pip install virtualenv
```
```
virtualenv venv
```
```
source venv/bin/activate
```
```
pip install -U aiogram
```

## Перезапуск службы после изменения файла
```
sudo systemctl restart bot_schedule
```


## Авто запуск и перезапуск телеграм бота

/var/www/bot_schedule

```
sudo nano /lib/systemd/system/bot_schedule.service
```
или
```
sudo mcedit /lib/systemd/system/bot_schedule.service
```

```
[Unit]
Description=botvenom schedule
After=syslog.target
After=network.target

[Service]
Type=simple
WorkingDirectory=/var/www/bot_schedule/
ExecStart=/var/www/bot_schedule/venv/bin/python3 /var/www/bot_schedule/main.py
RestartSec=60
Restart=always
Environment="PATH=/var/www/bot_schedule/venv/bin"
Environment="PYTHONPATH=/var/www/bot_schedule/venv/lib/python3.10/site-packages"

[Install]
WantedBy=multi-user.target
```

## Выполните эти две команды что бы запустить службу

```
sudo systemctl enable bot_schedule
```
```
sudo systemctl start bot_schedule
```

## Перезапуск службы после изменения файла
```
sudo systemctl restart bot_schedule
```


