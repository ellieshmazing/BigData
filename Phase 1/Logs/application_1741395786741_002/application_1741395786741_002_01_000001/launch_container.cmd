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
@set HADOOP_TOKEN_FILE_LOCATION=/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0002/container_1741395786741_0002_01_000001/container_tokens
@if %errorlevel% neq 0 exit /b %errorlevel%
@set CONTAINER_ID=container_1741395786741_0002_01_000001
@if %errorlevel% neq 0 exit /b %errorlevel%
@set NM_PORT=50992
@if %errorlevel% neq 0 exit /b %errorlevel%
@set NM_HOST=MysteryMachine
@if %errorlevel% neq 0 exit /b %errorlevel%
@set NM_HTTP_PORT=8042
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LOCAL_DIRS=/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0002
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LOCAL_USER_DIRS=/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LOG_DIRS=C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0002/container_1741395786741_0002_01_000001
@if %errorlevel% neq 0 exit /b %errorlevel%
@set USER=ellie
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LOGNAME=ellie
@if %errorlevel% neq 0 exit /b %errorlevel%
@set HOME=/home/
@if %errorlevel% neq 0 exit /b %errorlevel%
@set PWD=/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0002/container_1741395786741_0002_01_000001
@if %errorlevel% neq 0 exit /b %errorlevel%
@set MALLOC_ARENA_MAX=$MALLOC_ARENA_MAX
@if %errorlevel% neq 0 exit /b %errorlevel%
@set NM_AUX_SERVICE_mapreduce_shuffle=AAA0+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
@if %errorlevel% neq 0 exit /b %errorlevel%
@set APPLICATION_WEB_PROXY_BASE=/proxy/application_1741395786741_0002
@if %errorlevel% neq 0 exit /b %errorlevel%
@set SHELL=/bin/bash
@if %errorlevel% neq 0 exit /b %errorlevel%
@set CLASSPATH=C:/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0002/container_1741395786741_0002_01_000001/classpath-8368334402215555725.jar;C:\Hadoop\hadoop-3.3.0/share/hadoop/mapreduce/lib/*;job.jar/*;job.jar/lib/*;/tmp/hadoop-ellie/nm-local-dir/usercache/ellie/appcache/application_1741395786741_0002/container_1741395786741_0002_01_000001/*
@if %errorlevel% neq 0 exit /b %errorlevel%
@set APP_SUBMIT_TIME_ENV=1741397637581
@if %errorlevel% neq 0 exit /b %errorlevel%
@set LD_LIBRARY_PATH=%PWD%
@if %errorlevel% neq 0 exit /b %errorlevel%
@echo "Setting up job resources"
@C:\Hadoop\hadoop-3.3.0\bin\winutils.exe symlink "job.jar" "\tmp\hadoop-ellie\nm-local-dir\usercache\ellie\appcache\application_1741395786741_0002\filecache\11\job.jar"
@if %errorlevel% neq 0 exit /b %errorlevel%
@C:\Hadoop\hadoop-3.3.0\bin\winutils.exe symlink "job.xml" "\tmp\hadoop-ellie\nm-local-dir\usercache\ellie\appcache\application_1741395786741_0002\filecache\13\job.xml"
@if %errorlevel% neq 0 exit /b %errorlevel%
@if not exist "jobSubmitDir" mkdir "jobSubmitDir"
@if %errorlevel% neq 0 exit /b %errorlevel%
@C:\Hadoop\hadoop-3.3.0\bin\winutils.exe symlink "jobSubmitDir\job.splitmetainfo" "\tmp\hadoop-ellie\nm-local-dir\usercache\ellie\appcache\application_1741395786741_0002\filecache\10\job.splitmetainfo"
@if %errorlevel% neq 0 exit /b %errorlevel%
@if not exist "jobSubmitDir" mkdir "jobSubmitDir"
@if %errorlevel% neq 0 exit /b %errorlevel%
@C:\Hadoop\hadoop-3.3.0\bin\winutils.exe symlink "jobSubmitDir\job.split" "\tmp\hadoop-ellie\nm-local-dir\usercache\ellie\appcache\application_1741395786741_0002\filecache\12\job.split"
@if %errorlevel% neq 0 exit /b %errorlevel%
@echo "Copying debugging information"
rem Creating copy of launch script
copy "launch_container.cmd" "C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0002/container_1741395786741_0002_01_000001/launch_container.cmd"
rem Determining directory contents
@echo "dir:" > "C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0002/container_1741395786741_0002_01_000001/directory.info"
dir >> "C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0002/container_1741395786741_0002_01_000001/directory.info"
@echo "Launching container"
@call %JAVA_HOME%/bin/java -Djava.io.tmpdir=%PWD%/tmp -Dlog4j.configuration=container-log4j.properties -Dyarn.app.container.log.dir=C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0002/container_1741395786741_0002_01_000001 -Dyarn.app.container.log.filesize=0 -Dhadoop.root.logger=INFO,CLA -Dhadoop.root.logfile=syslog  -Xmx1024m org.apache.hadoop.mapreduce.v2.app.MRAppMaster 1>C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0002/container_1741395786741_0002_01_000001/stdout 2>C:/Hadoop/hadoop-3.3.0/logs/userlogs/application_1741395786741_0002/container_1741395786741_0002_01_000001/stderr 
@if %errorlevel% neq 0 exit /b %errorlevel%
