#!/usr/sbin/nft -f

#rename file as .nft instead of .sh

table inet trusted_table {
				set trusted {
								type ipv4_addr
								elements = { 10.22.0.50, 10.22.0.251, 10.22.0.252,}
				}

				chain input {
							type filter hook input priority filter 0;
							ip protocol icmp ip saddr @trusteds accept
							tcp dport 22 ip saddr @trusted accept
							tcp dport {  http, https } ip saddr @trusted accept
							udp dport {  http, https } ip saddr @trusted accept
							ip saddr != @trusted drop
				}
	
				chain forward {
							type filter hook forward priority filter 0;
				}

				chain output {
							type filter hook output priority filter 0;
				}
}