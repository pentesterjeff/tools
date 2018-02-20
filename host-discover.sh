for ip in $(seq 1 254); do
    ping -c 1 10.0.0.$ip | grep "bytes from" &
done
