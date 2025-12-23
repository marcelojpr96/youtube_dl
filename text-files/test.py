test_list = [{'key1':'value1', 'key2':'value2'},{'key3':'value3', 'key4':'value4'}]
test_list.copy();
#print(test_list[0].index("key2"))
print(test_list)
for entry in test_list.copy():
    if "value1" in entry.values():
        # print(entry)
        test_list.remove(entry)
print(test_list)


##########
# The above is working for the test, lets test it now with raw data
##########

raw_test_data = [{'_type': 'url',
  'ie_key': 'Youtube',
  'id': 'h0-MlJ38BXw',
  'url': 'https://www.youtube.com/watch?v=h0-MlJ38BXw',
  'title': 'Jailbreaking the Amazon Echo',
  'description': None,
  'duration': 1028,
  'channel_id': 'UCXOSur_wiS9TK0WUhJrYrlA',
  'channel': 'Dammit Jeff',
  'channel_url': 'https://www.youtube.com/channel/UCXOSur_wiS9TK0WUhJrYrlA',
  'uploader': 'Dammit Jeff',
  'uploader_id': '@DammitJeff',
  'uploader_url': 'https://www.youtube.com/@DammitJeff',
  'thumbnails': [{'url': 'https://i9.ytimg.com/vi/h0-MlJ38BXw/hqdefault_custom_1.jpg?sqp=CKDQqcoG-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLCYad4AwpK9pei6b1sRElbLyk9Hhg',
                  'height': 94,
                  'width': 168},
                 {'url': 'https://i9.ytimg.com/vi/h0-MlJ38BXw/hqdefault_custom_1.jpg?sqp=CKDQqcoG-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBPrvzTMagTID_Ze_S1WBHfmi_zzg',
                  'height': 110,
                  'width': 196},
                 {'url': 'https://i9.ytimg.com/vi/h0-MlJ38BXw/hqdefault_custom_1.jpg?sqp=CKDQqcoG-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCywLNruINkVWTlXsM-bj0MYzmj0w',
                  'height': 138,
                  'width': 246},
                 {'url': 'https://i9.ytimg.com/vi/h0-MlJ38BXw/hqdefault_custom_1.jpg?sqp=CKDQqcoG-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCpj8YhGlZBl-KKsGST-FrYnGskfg',
                  'height': 188,
                  'width': 336}],
  'timestamp': None,
  'release_timestamp': None,
  'availability': None,
  'view_count': 31000,
  'live_status': None,
  'channel_is_verified': None,
  '__x_forwarded_for_ip': None},
 {'_type': 'url',
  'ie_key': 'Youtube',
  'id': 'UWlrodHF1EE',
  'url': 'https://www.youtube.com/watch?v=UWlrodHF1EE',
  'title': 'Is This the ULTIMATE Home Cloud Solution? OMV + CasaOS',
  'description': None,
  'duration': 1343,
  'channel_id': 'UCgdTVe88YVSrOZ9qKumhULQ',
  'channel': 'Hardware Haven',
  'channel_url': 'https://www.youtube.com/channel/UCgdTVe88YVSrOZ9qKumhULQ',
  'uploader': 'Hardware Haven',
  'uploader_id': '@HardwareHaven',
  'uploader_url': 'https://www.youtube.com/@HardwareHaven',
  'thumbnails': [{'url': 'https://i.ytimg.com/vi/UWlrodHF1EE/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLAsxV4Z776F_9UpHXu21rnAkm0ihA',
                  'height': 94,
                  'width': 168},
                 {'url': 'https://i.ytimg.com/vi/UWlrodHF1EE/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBul3qKxqxANlfzb9gtnLiyGnpjXA',
                  'height': 110,
                  'width': 196},
                 {'url': 'https://i.ytimg.com/vi/UWlrodHF1EE/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDIEewHJO3Ft2el5RF30hOgG10pBg',
                  'height': 138,
                  'width': 246},
                 {'url': 'https://i.ytimg.com/vi/UWlrodHF1EE/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBDk_jKJxO9jZofN_XKwANthefIqw',
                  'height': 188,
                  'width': 336}],
  'timestamp': None,
  'release_timestamp': None,
  'availability': None,
  'view_count': 259000,
  'live_status': None,
  'channel_is_verified': None,
  '__x_forwarded_for_ip': None}]

raw_compare_data = raw_test_data.copy()

for entry in raw_test_data :
    with open("test.txt", 'w') as file :
        file.write(f"{entry['title']}\n")

print(entry['title'])

with open("test.txt","r") as file :
    for line in file :
        for entry in raw_test_data.copy() :
            if entry['title'].strip() == line.strip() :
                raw_test_data.remove(entry)

print(raw_test_data == raw_compare_data)