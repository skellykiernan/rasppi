#!/usr/bin/env sh


#~##############################################################################
# Command handlers
#~##############################################################################
help() {
    echo "My Raspberry Pi Helper command-line interface"
    echo ""
    echo "commands:"
    echo " start\t start services to connect to rasppi"
    echo " stop\t stop services assoicated with rasppi"
    echo " sync_to\t sync source code to the rasppi"
    echo " help\t display this help"
    echo ""
    echo "example:"
    echo " sudo ./rasppi.sh start"
    echo " ./rasppi.sh sync_to"
    echo " sudo ./rasppi.sh stop"
    echo ""
}


start_rasppi() {
    # start dhcpd
    chown root /var/lib/dhcp/dhcpd.leases
    dhcpd

    rasppi_ip_addr=""
    while [ -z $rasppi_ip_addr ]; do
        echo "scanning - Ensure Rasppi is Powered On and connected"
        echo ""
        rasppi_ip_addr=$(nmap -nsP 10.42.0.10-100 2>/dev/null -oG - | grep "Up$" | awk '{printf "%s ", $2}')
    done

    echo 'rasppi_ip_addr="'"$rasppi_ip_addr"'"' > rasppi_ip_addr.file
    echo "think rasppi_ip_addr is $rasppi_ip_addr"
    gnome-terminal -e "sshpass -p raspberry ssh pi@$rasppi_ip_addr"
}

sync_to_rasppi() {
    rasppi_ip_addr="10.42.0.80"
    if [ -e "./rasppi_ip_addr.file" ]; then
        . ./rasppi_ip_addr.file
        # strip blanks in the variable
        rasppi_ip_addr=$(echo $rasppi_ip_addr | sed 's/ //g')
    fi

    echo "think rasppi_ip_addr is $rasppi_ip_addr"
    rsync -avz -e ssh src/ pi@${rasppi_ip_addr}:wkspace/
    echo "PARTLY IMPLEMENTED"
}

stop_rasppi() {
    # Kill the rasspi shell

    # Stop dhcpd
    pkill dhcpd
    echo "PARTLY IMPLEMENTED"
}

#~##############################################################################
# Start of Execution
#~##############################################################################
script_name=$(basename $0)
command=$1
case $command in
    start)
        start_rasppi
        ;;
    stop)
        stop_rasppi
        ;;
    sync_to)
        sync_to_rasppi
        ;;
    help)
        help
        ;;
    *)
        # the command is required
        echo "unknown command try \"$script_name help\""
        ;;
esac
