# import json
#
# f = open('./static/config.json', 'r')
# content = f.read()
# config = json.loads(content)
# f.close()
# config['resources_list']["GroupData1"] =  ["./static/DATA/GroupData", "QQNum,QunNum"]
# b = json.dumps(config)
# f2 = open('./static/config.json', 'w')
# f2.write(b)
# f2.close()
import cchardet as chardet
def get_encoding(filename):
    """
    Returns the file encoding format
    """
    with open(filename, 'rb') as f:
        print(chardet.detect(f.read()))
        return chardet.detect(f.read())['encoding']

if __name__ =="__main__":
    get_encoding("./DATA/GroupData/GroupData01.csv")