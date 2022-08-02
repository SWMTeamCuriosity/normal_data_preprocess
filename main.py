import json

possible_word = ['고객질문(요청)', '상담사질문(요청)', '고객답변', '상담사답변']
result = {}
with open("./data/4th.json") as f:
    data = json.load(f)
    for i in data :
        if(result.get(i['대화셋일련번호']) == None) :
            result[i['대화셋일련번호']] = []

        #print(type(result[i['대화셋일련번호']]))
        for j in possible_word :
            if i[j] != '' :
                result[i['대화셋일련번호']].append(i[j])

with open("./result/4th.json", 'w') as f:
    json.dump(result, f, ensure_ascii= False, indent = 4)
