# Proxy Server

This configures the docker daemen to use proxy server

You can follow instrcutions here  <https://docs.docker.com/config/daemon/systemd/>

Or simplified steps here

Steps

    $ sudo mkdir -p /etc/systemd/system/docker.service.d

Create file <code>/etc/systemd/system/docker.service.d/http-proxy.conf</code> , that contains following (please replace the appropriate values)

    [Service]
    Environment="HTTP_PROXY=http://proxy.example.com:80/" "NO_PROXY=localhost,127.0.0.1,10.204."

Restart the services

    $ sudo systemctl daemon-reload
    $ sudo systemctl restart docker

Confirm it is reloaded

    $ systemctl show --property=Environment docker

All done
