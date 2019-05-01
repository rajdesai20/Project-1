Project 2 Readme
This project is based on using Hadoop Map-Reduce to find minimum, maximum and average temperatures from the given weather data. Also the coldest and hottest temperature are in output with their station codes.
Steps for the project:
1.	Created two files mapper.py and reducer.py.
2.	Creating the Hadoop jar file by following command: 
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file /home/desairj/map1.py -mapper map1.py -file /home/desairj/reduce1.py -reducer reduce1.py -input /user/tatavag/weather/* -output raj3_output
3.	Get output from Hadoop:
hadoop fs -get /user/desairj/raj3_output .
The output generated is represented as tabular form in report. 
