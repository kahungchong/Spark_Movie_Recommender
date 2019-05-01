# This is course project for MSBD5003
## Tools required
- MySQL 8
- Spark
- Jupyter Notebook
## Start spark with jupyter notebook
1. Use terminal and cd into spark . if you used `HomeBrew` to install spark, it should be in:

                /usr/local/Cellar/apache-spark/2.4.0/
            
2. Change env path:    

                export PYSPARK_DRIVER_PYTHON='jupyter'
                export PYSPARK_DRIVER_PYTHON_OPTS='notebook'

3. Start pyspark:

                ./bin/pyspark

4. Then enjoy pyspark with jupyter. Notice that if you want to connect with mysql, change the `sql_password` variable declared at the first line to your own password.



## Tips for configuration
- As spark needs jdbc to connect with mysql, a driver jar file should be download and referred by spark.  
To do this:  
    1. Find out the environment configuration file. If you used `HomeBrew` to install spark, then the file should be in  

                /usr/local/Cellar/apache-spark/2.4.0/libexec/conf/spark-env.sh  

        Notice that by default, you will see a `spark-env.sh.template` file, rename it to `spark-env.sh`.
    2. Open `spark-env.sh`, add the following two lines:  

                export SPARK_HOME="/usr/local/Cellar/apache-spark/2.4.0/libexec"  
                export CLASSPATH=$SPARK_HOME/jars/mysql-connector-java-5.1.45-bin.jar
    
    3. Notice that the file path may differ between computers, change them accordingly.
- As currently jdbc can only connect to mysql with native password, the password of mysql should be change to native plugin. 
To do this:
    1. Start mysql server with the following command:

                mysql.server start
    
    2. Connect to mysql server:

                mysql -u root -p
        
        If you haven't set the password for root, just press `enter`. Otherwise enter your password.
    
    3. After connecting to mysql, change password with the following sql:
        
                alter user root@localhost identified with mysql_native_password by 'password';
        
        Where `password` is your new password.
    
    4. DO NOT FORGET THE PASSWORD! 
        - To [reset root password](https://www.jianshu.com/p/6095fb874178). (Unfortunately it may not work as the password plugin has been changed to native type. You can use `flush privileges` to put updated user information into cache so that the new password can take effect without rebooting.)
        - To [reinstall mysql](https://blog.csdn.net/Sarahhuangzht/article/details/51508112). (Try this if you forget the password and fail to reset)

- To load data into mysql: 
    1. Start mysql server with the following command:

                mysql.server start

    2. Type the following sql:

                source /PROJECT_PATH/data/sql/MovieDB.sql
    
    3. The above file works with mysql 8. If you are using mariaDB, try to install mysql otherwise it needs many modification.

    4. [Deal with `secure-file-priv` problem](https://blog.csdn.net/qq_42142315/article/details/84973970)

    5. Find location of my.cnf
                mysql --help --verbose