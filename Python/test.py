import json

if __name__ == "__main__":
    d = {
        "xd":"xddd",
        "xdddddddd":"sdfdsgd"
    }
    json.dump( d, open( "myfile.json", 'w' ) )
    print(json.load( open( "myfile.json" ) ))

    # for i in range(11):
    #     convert(i)
        