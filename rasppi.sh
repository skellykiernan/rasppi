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
    echo " help\t display this help"
    echo ""
    echo "example:"
    echo " sudo ./rasppi.sh start"
    echo " sudo ./rasppi.sh stop"
    echo ""
}


start_rasppi() {
    # start dhcpd
    chown root /var/lib/dhcp/dhcpd.leases
    dhcpd
    echo "PARTLY IMPLEMENTED"
    # list possible ip addresses in menu
    # select ip address
    # start a shell and connect
    #function_boy
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
    help)
        help
        ;;
    *)
        # the command is required
        echo "unknown command try \"$script_name help\""
        ;;
esac
