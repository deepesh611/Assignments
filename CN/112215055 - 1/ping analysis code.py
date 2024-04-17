
import pylab as pl, re
from statistics import median

def analyze_ping(path):
    rtt_time = []
    cntx = 'rtt min/avg/max/mdev = '
    f = open(path,'rb')
    for i in f.readlines():
        if cntx in str(i):
            min, avg, max, mdev = str(i)[len(cntx)+2:-13].split('/')
        elif '1000 packets' in str(i):
            pkt_transmitted, pkt_recived, pkt_loss, time = str(i)[2:-5].split(',')
        else:
            time_match = re.search(r'time=([\d.]+)\sms', str(i))
            if time_match:
                time_value = float(time_match.group(1))
                rtt_time.append(time_value)
                            
    f.close()
    pl.plot(rtt_time)
    pl.show()
    
    
    print('Packets Transmitted: ', pkt_transmitted)
    print('Packets Recived: ', pkt_recived)
    print('Packets Loss: ', pkt_loss)
    print('Time: ', time[5:],'ms\n')
    print('Minimum: ', min,'ms')
    print('Average: ', avg,'ms')
    print('Maximum: ', max,'ms')
    print('Median: ', median(rtt_time),'ms')
    print('Mdev: ', mdev,'ms')





print('Latency Analysis for ping1.txt')
analyze_ping('./ping1.txt')
print('\n\n\nLatencyAnalysis for ping2.txt')
analyze_ping('./ping1.txt')
