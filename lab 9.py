import numpy as np
sensor=np.array([22.4,22.7,23.1,30.5,23.0,22.8,31.2,22.9])
print(sensor)
avg=sum(sensor)/len(sensor)
print("avg before replace",avg)
high_sensor=sensor[sensor>30]
print(high_sensor)
hsensor=sensor[sensor>30]
print(len(hsensor))

wsensor=np.where([sensor>30])
# msensor=wsensor.replace(30)
sensor[sensor>30]=30
print(sensor)
avgs=sum(sensor)/len(sensor)
print("avrage after mean" ,avgs)

