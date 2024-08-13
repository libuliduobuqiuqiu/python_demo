"""
    :Date: 2024-8-13
    :Author: linshukai
    :Description: About Set WSL Proxy script.
"""

from socket import AF_INET
import psutil
import ipaddress
import argparse

PROXYPORT = 7890


# 设置wsl代理
def get_wsl_proxy(proxy_port):
    net_if_addrs = psutil.net_if_addrs()

    for iface, infos in net_if_addrs.items():
        if iface != "lo":
            for i in infos:
                if i.family == AF_INET:
                    network_address = ipaddress.IPv4Network(
                        f"{i.address}/{i.netmask}", strict=False
                    )
                    default_gateway = network_address.network_address + 1

                    if proxy_port:
                        print(f"{default_gateway}:{proxy_port}")
                    else:
                        print(f"{default_gateway}:{PROXYPORT}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get WSL gateway.")
    parser.add_argument("--port", "-p", help="proxy port(default: 7890)")
    args = parser.parse_args()
    get_wsl_proxy(args.port)
