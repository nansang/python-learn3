### python常用模块及命令

- os.system():执行系统命令
- sys.argv[]:获取命令参数
- crontab -e:定时任务---[crontab](http://www.cnblogs.com/kaituorensheng/p/4494321.html#_label1)
	
		/var/log/cro:查看crontab是否在运行
	
- ps aux:当前进程状态


02 2 * * * root run-parts /etc/cron.daily

scp -r /Users/hackMarshal/desktop/douyu_gifts root@192.168.0.3:/home/work_tv/tv/python/douyu/

scp -r root@192.168.0.3:/var/www/html/tv/log/ /Users/hackMarshal/desktop/tv/log/