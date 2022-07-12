# Corona

import corona


def layout(arr):
    for i in range(len(arr)):
        print(corona.data[i]["state"])
        print(corona.data[i]['cases'])
        print(corona.data[i]['recovered'])
        print(corona.data[i]['active'])
        x = corona.data[0]['recovered']
        y = corona.data[0]['state']
    if x < corona.data[i]['recovered']:
                x = corona.data[i]['recovered']
                y = corona.data[i]['state']
    print(f'The state with the most recoverd is {y} : {x}')
    if x > corona.data[i]['recovered']:
                x = corona.data[i]['recovered']
                y = corona.data[i]['state'] 

    print(f'The state with the least recoverd is {y} : {x}')


layout(corona.data)


