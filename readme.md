# Creating 3 cronjobs based on the API
0 8 * * * cd ~/Documents/GitHub/crontab && python3 crontab.py
2 2 * * SUN cd ~/Documents/GitHub/crontab && python3 crontab.py
0 0 1 */3 * cd ~/Documents/GitHub/crontab && python3 crontab.py