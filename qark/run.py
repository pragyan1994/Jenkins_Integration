import os
x = os.environ['JENKINS_HOME']+'/jobs/'+os.environ['JOB_NAME']+'/workspace/goatdroid.apk'
print x
os.system("python qark/qarkMain.py --source 1 --pathtoapk "+x+" --exploit 1 --install 1");
print "Done"
