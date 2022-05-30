###Use case: Suppose you have a list of IP addresses that you want to check to make sure none of them are on your
#blacklist; if they are, find them and add them to a new file.
all_iplist = "test/test2.txt"
mal_iplist = "test/test3.txt"
finding_list = "test/test4.txt"
with open(all_iplist) as files_object2:
    with open(mal_iplist) as files_object:
        for ip in files_object:
            for ip2 in files_object2:
                if ip == ip2:
                    print(f"{ip2} is malicious")
                    with open(finding_list, 'w') as files_object3:
                        files_object3.write(ip)
                else:
                    print(f"No bad ip is found in {all_iplist}")

