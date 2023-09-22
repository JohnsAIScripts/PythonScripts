# This script gathers and analyzes data from a malfunctioning
# network component

# TITLE
print("")
print("===== NETWORK CONFLICT TEST =====")
print("")


import psutil
import time

# Gather network data every 5 seconds for 1 minute
start_time = time.time()
data = []
while time.time() - start_time < 60:
    net_io_counters = psutil.net_io_counters()
    data.append((net_io_counters.bytes_sent, net_io_counters.bytes_recv))
    time.sleep(5)

# Calculate statistics for the data
bytes_sent = [d[0] for d in data]
bytes_recv = [d[1] for d in data]
avg_sent = sum(bytes_sent) / len(bytes_sent)
avg_recv = sum(bytes_recv) / len(bytes_recv)
max_sent = max(bytes_sent)
max_recv = max(bytes_recv)

# Determine the root cause of the issue
if max_sent > avg_sent * 2 or max_recv > avg_recv * 2:
    print("The root cause of the issue is high network traffic.")
else:
    print("The root cause of the issue is unknown.")



"""
This script uses the psutil library to gather network data
every 5 seconds for 1 minute, storing the number of bytes
sent and received in a list. After the data has been collected,
the script calculates the average and maximum number of bytes
sent and received during the measurement period.

Finally, the script compares the maximum number of bytes sent
and received to twice the average number of bytes sent and
received. If either value is more than twice the average,
the script concludes that the root cause of the issue is
high network traffic. Otherwise, the script concludes that
the root cause of the issue is unknown.

Note that this script assumes that high network traffic is
the only possible root cause of the issue. Depending on the
specifics of the malfunctioning network component, there may
be other root causes that need to be considered.
"""
