@setlocal

@echo "Setting up env variables"
@set JAVA_HOME=C:\Java\jdk-11
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HADOOP_COMMON_HOME=C:\Hadoop\hadoop-3.3.0
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HADOOP_HDFS_HOME=C:\Hadoop\hadoop-3.3.0
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HADOOP_CONF_DIR=C:\Hadoop\hadoop-3.3.0\etc\hadoop
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HADOOP_YARN_HOME=C:\Hadoop\hadoop-3.3.0
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HADOOP_MAPRED_HOME=C:\Hadoop\hadoop-3.3.0
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HADOOP_TOKEN_FILE_LOCATION=/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0001/container_1741395786741_0001_01_000002/container_tokens
@if %errorlevel% neq 0 exit /b %errorlevel%
@set CONTAINER_ID=container_1741395786741_0001_01_000002
@if %errorlevel% neq 0 exit /b %errorlevel%
@set NM_PORT=50992
@if %errorlevel% neq 0 exit /b %errorlevel%
@set NM_HOST=MysteryMachine
@if %errorlevel% neq 0 exit /b %errorlevel%
@set NM_HTTP_PORT=8042
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LOCAL_DIRS=/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0001
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LOCAL_USER_DIRS=/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LOG_DIRS=C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002
@if %errorlevel% neq 0 exit /b %errorlevel%
@set USER=ellie
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LOGNAME=ellie
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HOME=/home/
@if %errorlevel% neq 0 exit /b %errorlevel%
@set PWD=/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0001/container_1741395786741_0001_01_000002
@if %errorlevel% neq 0 exit /b %errorlevel%
@set MALLOC_ARENA_MAX=$MALLOC_ARENA_MAX
@if %errorlevel% neq 0 exit /b %errorlevel%
@set NM_AUX_SERVICE_mapreduce_shuffle=AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
@if %errorlevel% neq 0 exit /b %errorlevel%
@set PATH=;C:\Hadoop\hadoop-3.3.0\bin
@if %errorlevel% neq 0 exit /b %errorlevel%
@set STDOUT_LOGFILE_ENV=C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002/stdout
@if %errorlevel% neq 0 exit /b %errorlevel%
@set SHELL=/bin/bash
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HADOOP_ROOT_LOGGER=INFO,console
@if %errorlevel% neq 0 exit /b %errorlevel%
@set CLASSPATH=C:/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0001/container_1741395786741_0001_01_000002/classpath-4739150133151008215.jar;C:\Hadoop\hadoop-3.3.0/share/hadoop/mapreduce/lib/*;job.jar/*;job.jar/lib/*;/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0001/container_1741395786741_0001_01_000002/*
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LD_LIBRARY_PATH=%PWD%
@if %errorlevel% neq 0 exit /b %errorlevel%
@set STDERR_LOGFILE_ENV=C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002/stderr
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HADOOP_CLIENT_OPTS=
@if %errorlevel% neq 0 exit /b %errorlevel%
@echo "Setting up job resources"
@C:\Hadoop\hadoop-3.3.0\bin\winutils.exe symlink "job.xml" "\tmp\hadoop-ellie\nm-local-dir\usercache\ellie\appcache\application_1741395786741_0001\filecache\13\job.xml"
@if %errorlevel% neq 0 exit /b %errorlevel%
@C:\Hadoop\hadoop-3.3.0\bin\winutils.exe symlink "job.jar" "\tmp\hadoop-ellie\nm-local-dir\usercache\ellie\appcache\application_1741395786741_0001\filecache\11\job.jar"
@if %errorlevel% neq 0 exit /b %errorlevel%
@echo "Copying debugging information"
rem Creating copy of launch script
copy "launch_container.cmd" "C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002/launch_container.cmd"
rem Determining directory contents
@echo "dir:" > "C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002/directory.info"
dir >> "C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002/directory.info"
@echo "Launching container"
@call %JAVA_HOME%/bin/java -Djava.net.preferIPv4Stack=true -Dhadoop.metrics.log.level=WARN   -Xmx820m -Djava.io.tmpdir=%PWD%/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog org.apache.hadoop.mapred.YarnChild 192.168.68.106 51628 attempt_1741395786741_0001_m_000000_0 2 1>C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002/stdout 2>C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0001/container_1741395786741_0001_01_000002/stderr 
@if %errorlevel% neq 0 exit /b %errorlevel%
