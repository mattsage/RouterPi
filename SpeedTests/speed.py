from speedtest import Speedtest
from time import sleep

st = Speedtest()

while True:
    st.get_best_server()

    down = st.download()
    if down > 60000000:  # 60Mb
        print ("good")
    if down > 40000000:  # 40Mb
        print ("meh")
    if down > 20000000:  # 20Mb
        print ("bad")

    up = st.upload()
    if up > 60000000:  # 6Mb
        print ("good")
    if up > 4000000:  # 4Mb
        print ("meh")
    if up > 2000000:  # 2Mb
        print ("bad")

    sleep(60*10)  # check every 10 minutes
