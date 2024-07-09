
age = int(input('Enter your age in years: '))
low_intensity = 0.50
high_intensity = 0.85

number_of_heartbeats = int(input('Enter your number of heartbeat: '))

resting_heart_rate = number_of_heartbeats * 2
print('your resting heart rate is', resting_heart_rate, 'BPM')

maximum_heart_rate = 220 - age
print('your maximum heart rate is', maximum_heart_rate, 'BPM')

target_heart_rate_low = (maximum_heart_rate - resting_heart_rate) * low_intensity + resting_heart_rate
print('your lowest target heart rate is', target_heart_rate_low, 'BPM')

target_heart_rate_high = (maximum_heart_rate - resting_heart_rate) * high_intensity + resting_heart_rate
print('your highest target heart rate is', target_heart_rate_high, 'BPM')

