import csv, math

rowCount, sum, time, rtt_time, sent_pkt, recived_pkt, tcp_pkt, udp_pkt = 0, 0, 0, 0, 0, 0, 0, 0
file_path = 'Captured_Packets/Evening Data.csv'

with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        
        if 'Client Hello' in row[6]:
            rtt_time = -float(row[1])
        elif 'Server Hello' in row[6]:
            rtt_time += float(row[1])
            
        if row[2] == '192.168.0.0':
            sent_pkt += 1
        else:
            recived_pkt +=1
        
        if row[4] == 'TCP':
            tcp_pkt += 1
        elif row[4] == 'UDP':
            udp_pkt += 1

        rowCount +=1                                                                         # count of rows
        sum += int(row[5])
        time += float(row[1])
    
    avg_size = sum/rowCount                                                                  # avg packety size
    avg_time = time/rowCount                                                                 # avg time
    avg_througput = avg_size/avg_time   
    pkt_loss_percentage = (abs(sent_pkt - recived_pkt)/rowCount)*100
    avg_response_for_one_packet = sent_pkt/recived_pkt
    if avg_response_for_one_packet < 1:
        avg_response_for_one_packet = 1
    
    print(f'Avg Throughput : {avg_througput.__round__(3)}\n')                               # average throughput rounded to 3 decimal places
    print(f'Avg RTT : {rtt_time.__round__(3)} sec\n')                                       # average RTT rounded to 3 decimal places
    print(f'Avg Packet Size is {avg_size.__round__(3)}\n')                                  # average packet size
    print(f'Packet Loss Percentage : {pkt_loss_percentage.__round__(3)}%\n')                # packet loss percentage rounded to 3 decimal places
    print(f'No. of TCP Packets : {tcp_pkt}\nNo. of UDP Packets : {udp_pkt}\n')              # no. of TCP and UDP packets
    print(f'Avg Response for one packet : {math.ceil(avg_response_for_one_packet)}\n')      # average response for one packet rounded to 3 decimal places
    



with open(file_path, 'a') as file:
    file.write(f'\n,,,,,,Avg. Throughput: {avg_througput.__round__(3)}\n')
    file.write(f',,,,,,RTT : {rtt_time.__round__(3)} sec\n')
    file.write(f',,,,,,Avg. Packet Size : {avg_size.__round__(3)}\n')
    file.write(f',,,,,,Packet Loss Percentage : {pkt_loss_percentage.__round__(3)}\n')
    file.write(f',,,,,,No. of TCP Packets : {tcp_pkt}\n,,,,,,No. of UDP Packets : {udp_pkt}\n')
    file.write(f',,,,,,Avg Response for one packet : {math.ceil(avg_response_for_one_packet)}\n')
    file.write('\n')
