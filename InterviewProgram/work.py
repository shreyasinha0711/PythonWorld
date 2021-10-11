import json

final_shreyaGoodsandMilitaryList_dict = {}
shreyaGoodsandMilitaryList_dict = {}
regulationlist_list = []
regulationlist_commondata_dict = {}
goodsInformation_data_dict = {}
goodsInformation_list = []
goodsInformation_list_dict = {}


#GoodsInformation block
with open('eee_data2.txt', 'r') as data:
    for line in data:
        line = line.strip()
        ldata = line.split('|')
        goodsInformation_data_dict = {
            'DetailNumber':ldata[3],
            'Description':ldata[4],
            'RegEffDate':ldata[5],
            'RegExpDate':ldata[6]
        }
        goodsInformation_list.append(goodsInformation_data_dict)

goodsInformation_list.pop(0)

#creating goods information dictonary
goodsInformation_list_dict = {
    "GoodsInformation" : goodsInformation_list
}

#regulation list common data
with open('eee_data2.txt', 'r') as regulationlist_commondata:
    regulationlist_commondata.readline()
    regulationlist_commondata_line = regulationlist_commondata.readline().split('|')

    regulationlist_commondata_dict = {
        'RegListName':regulationlist_commondata_line[0],
        'RegListID':regulationlist_commondata_line[1],
        'CountryCode':regulationlist_commondata_line[2]
    }

#merge goodsInformation_list_dict and  regulationlist_commondata_dict dictonaries
regulationlist_commondata_dict.update(goodsInformation_list_dict)


#regulationlist_list--convert to list
regulationlist_list.append(regulationlist_commondata_dict)

#dictonary regulation list block
shreyaGoodsandMilitaryList_dict = {
    "RegulationList": regulationlist_list
}

final_shreyaGoodsandMilitaryList_dict = {
    "shreyaGoodsandMilitaryList" : shreyaGoodsandMilitaryList_dict
}

with open('text_to_json_a_output_1.json', 'w') as fp:
    json.dump(final_shreyaGoodsandMilitaryList_dict, fp, indent=7)

from pprint import pprint
pprint(final_shreyaGoodsandMilitaryList_dict)
